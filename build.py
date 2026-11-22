#!/usr/bin/env python3
"""Build theme.css for Umbria: embed fonts, generate the contour-line SVG, fill in the source.

Usage:  python3 build.py                 -> writes ./theme.css
        python3 build.py --install VAULT -> also copies theme.css + manifest.json into VAULT/.obsidian/themes/Umbria
"""
import base64, math, random, re, shutil, sys, pathlib, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src" / "theme.src.css"
OUT = ROOT / "theme.css"

TOPO_SEED = 44
LATIN = ("U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, "
         "U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD")


def face(family, style, weight, file):
    data = base64.b64encode((ROOT / "fonts" / file).read_bytes()).decode()
    return (f'@font-face{{font-family:"{family}";font-style:{style};font-weight:{weight};font-display:swap;'
            f'unicode-range:{LATIN};src:url(data:font/woff2;base64,{data}) format("woff2");}}')


# ---------- Contour lines (marching squares, then simplified) ----------
def rdp(pts, eps):
    if len(pts) < 3:
        return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy) or 1e-9
    i, dmax = 0, 0.0
    for k in range(1, len(pts) - 1):
        d = abs(dy * pts[k][0] - dx * pts[k][1] + x2 * y1 - y2 * x1) / n
        if d > dmax:
            i, dmax = k, d
    if dmax > eps:
        return rdp(pts[: i + 1], eps)[:-1] + rdp(pts[i:], eps)
    return [pts[0], pts[-1]]


def smooth(pts):
    """Polyline as a Catmull-Rom curve (cubic Béziers) instead of corners."""
    f = lambda v: f"{round(v, 1):g}"
    if len(pts) < 3:
        return "M" + " ".join(f"{f(x)} {f(y)}" for x, y in pts[:1]) + "L" + " ".join(f"{f(x)} {f(y)}" for x, y in pts[1:])
    closed = pts[0] == pts[-1]
    out = [f"M{f(pts[0][0])} {f(pts[0][1])}"]
    n = len(pts)
    for i in range(n - 1):
        p0 = pts[i - 1] if i > 0 else (pts[-2] if closed else pts[0])
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < n else (pts[1] if closed else pts[-1])
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        out.append(f"C{f(c1[0])} {f(c1[1])} {f(c2[0])} {f(c2[1])} {f(p2[0])} {f(p2[1])}")
    return "".join(out)


def topo_svg(w=720, h=480, step=2, levels=26, seed=TOPO_SEED, out_w=3840, nb=16):
    # Many smaller hills and hollows instead of a few large ones: evenly spread lines
    r = random.Random(seed)
    bumps = [(r.random() * w, r.random() * h, (0.07 + r.random() * 0.15) * max(w, h),
              (0.4 + r.random() * 0.6) * (1 if r.random() < 0.65 else -1)) for _ in range(nb)]
    cols, rows = w // step + 1, h // step + 1
    F = [[0.0] * cols for _ in range(rows)]
    for j in range(rows):
        for i in range(cols):
            x, y = i * step, j * step
            v = 0.08 * math.sin(x / 47 + y / 83) + 0.06 * math.cos(y / 39 - x / 121)
            for bx, by, s, a in bumps:
                v += a * math.exp(-((x - bx) ** 2 + (y - by) ** 2) / (s * s))
            F[j][i] = v
    mn = min(map(min, F)); mx = max(map(max, F))
    groups = {"thin": [], "thick": []}
    for L in range(1, levels):
        lv = mn + (mx - mn) * L / levels
        segs = []
        for j in range(rows - 1):
            for i in range(cols - 1):
                a, b, c, d = F[j][i], F[j][i + 1], F[j + 1][i + 1], F[j + 1][i]
                x, y = i * step, j * step
                pts = []
                for v1, v2, p1, p2 in ((a, b, (x, y), (x + step, y)), (b, c, (x + step, y), (x + step, y + step)),
                                       (c, d, (x + step, y + step), (x, y + step)), (d, a, (x, y + step), (x, y))):
                    if (v1 < lv) != (v2 < lv):
                        t = (lv - v1) / (v2 - v1)
                        pts.append((round(p1[0] + (p2[0] - p1[0]) * t, 1), round(p1[1] + (p2[1] - p1[1]) * t, 1)))
                for k in range(0, len(pts) - 1, 2):
                    segs.append((pts[k], pts[k + 1]))
        # Chain segments into polylines
        adj = {}
        for s in segs:
            for p in s:
                adj.setdefault(p, []).append(s)
        used = set()
        for s in segs:
            if id(s) in used:
                continue
            used.add(id(s))
            line = [s[0], s[1]]
            for end in (1, 0):
                while True:
                    tip = line[-1] if end else line[0]
                    nxt = next((t for t in adj.get(tip, []) if id(t) not in used), None)
                    if not nxt:
                        break
                    used.add(id(nxt))
                    q = nxt[1] if nxt[0] == tip else nxt[0]
                    if end:
                        line.append(q)
                    else:
                        line.insert(0, q)
            line = rdp(line, 0.12)
            if len(line) < 2:
                continue
            d = smooth(line)
            groups["thick" if L % 4 == 0 else "thin"].append(d)
    # Large intrinsic size so it is never upscaled; coordinates stay compact in the viewBox
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' width='{out_w}' height='{out_w * h // w}' viewBox='0 0 {w} {h}'>"
           f"<g fill='none' stroke='black' stroke-linecap='round' stroke-linejoin='round'>"
           f"<path stroke-width='0.4' stroke-opacity='0.85' d='{''.join(groups['thin'])}'/>"
           f"<path stroke-width='0.6' d='{''.join(groups['thick'])}'/></g></svg>")
    return "data:image/svg+xml," + urllib.parse.quote(svg, safe=" /:=',.-")


def minify(css):
    """Drop comments (except the header and the Style Settings block) and indentation."""
    css = re.sub(r"/\*(?!\s*@settings)(?! Umbria \d).*?\*/", "", css, flags=re.S)
    out, in_settings = [], False
    for line in css.splitlines():
        if "/* @settings" in line:
            in_settings = True
        if in_settings:
            out.append(line)
            in_settings = "*/" not in line
        elif line.strip():
            out.append(line.strip())
    return "\n".join(out) + "\n"


GERMAN = re.compile(r"\b(zitat|stoa|reflexion|praxis|gedanke|dankbar|holz|farbe|ueberschrift|hoehenlinie|kachel\w*)\b", re.I)


def check(src):
    """Catch mistakes before they ship."""
    settings = re.search(r"/\* @settings(.*?)\*/", src, re.S)
    assert settings, "@settings block missing"
    ids = re.findall(r"^\s+id: (\S+)", settings.group(1), re.M)
    dup = {i for i in ids if ids.count(i) > 1}
    assert not dup, f"duplicate Style Settings ids: {dup}"
    body = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    body = re.sub(r'"(?:[^"\\]|\\.)*"', '""', body)
    assert body.count("{") == body.count("}"), f"unbalanced braces: {body.count('{')} {{ vs {body.count('}')} }}"
    hit = GERMAN.search(body)
    assert not hit, f"German identifier in CSS: {hit.group(0)!r}"
    for cls in re.findall(r"value: (umbria-[\w-]+)", settings.group(1)) + \
               [i for i, t in re.findall(r"id: (umbria-[\w-]+)\n.*?type: (\S+)", settings.group(1), re.S) if t == "class-toggle"]:
        defaults = re.findall(r"default: (umbria-[\w-]+)", settings.group(1))  # defaults need no CSS of their own
        assert re.search(r"\." + re.escape(cls) + r"(?![\w-])", body) or cls in defaults, f"setting class .{cls} is never used"


def main():
    css = SRC.read_text()
    check(css)
    fonts = "\n".join([
        face("Inter", "normal", "100 900", "inter.woff2"),
        face("Literata", "normal", "200 900", "literata.woff2"),
        face("Literata", "italic", "200 900", "literata-italic.woff2"),
        face("Cinzel", "normal", "400 900", "cinzel.woff2"),
    ])
    topo = topo_svg()
    # One black SVG, used as a mask: the CSS paints it in the accent colour of each mode
    css = css.replace("/*@@FONTS@@*/", fonts).replace("@@TOPO@@", topo)
    assert "@@" not in css, "placeholder left over"
    css = minify(css)
    OUT.write_text(css)
    print(f"{OUT}: {len(css)/1024:.0f} KB (contour lines {len(topo)/1024:.0f} KB)")
    if "--install" in sys.argv:
        dest = pathlib.Path(sys.argv[sys.argv.index("--install") + 1]).expanduser() / ".obsidian" / "themes" / "Umbria"
        dest.mkdir(parents=True, exist_ok=True)
        shutil.copy(OUT, dest / "theme.css")
        shutil.copy(ROOT / "manifest.json", dest / "manifest.json")
        print(f"installed to {dest}")


if __name__ == "__main__":
    main()
