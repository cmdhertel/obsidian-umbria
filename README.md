# Umbria

*Umbrian hills at dusk: carved letters, quiet contour lines, the warmth of espresso.*

Umbria is a warm, calm Obsidian theme for everyday notes, journaling and reading.
Dark mode is the heart of it; light mode is soft paper in the same wood.

![Umbria](preview.png)

## Features

- **One accent, earth tones.** Amber accent with moss, rust, slate, plum and honey for everything else. All headings share one colour and differ only in size and weight.
- **Three wood tones, each with a dark and a light paper:** Ember (espresso / linen, default), Pine (forest / sage), Autumn (deep red-brown / clay).
- **Contour lines.** A topographic map behind the editor, in empty tabs and in the stoic callout. It fades towards the text, stays sharp on Retina and 5K displays, and takes on your accent colour.
- **Quotes as the centrepiece.** Blockquotes and quote callouts get large serif text and a typographic quotation mark. The callout title is shown as the source underneath the quote.
- **Typography.** Literata for notes, Inter for the interface, Cinzel "inscription" headings (switchable). All fonts are embedded, so nothing is loaded from the internet.
- **Divider ornaments:** contour lines, an hourglass (memento mori), a wave, or none.
- **Task states:** `[/]` in progress, `[!]` important, `[?]` question, `[*]` star, `[-]` cancelled, `[>]` deferred.
- **Canvas, Graph and Bases** in the same palette: warm dot grid and soft cards, amber for the active node, Bases tables and cards matching note tables and callouts.
- **Plugin styling** for Dataview, Tasks, Calendar, Day Planner, Excalidraw, Spaced Repetition and Notebook Navigator.
- Optional *Memento mori* in the status bar, and a "no animations" switch.

## Custom callouts

| Callout | Icon | Colour |
|---|---|---|
| `[!quote]` / `[!cite]` | quote | amber, large serif |
| `[!stoic]` | landmark | amber, with contour lines |
| `[!reflection]` | moon | slate |
| `[!practice]` | sprout | moss |
| `[!thought]` | lightbulb | plum |
| `[!gratitude]` | flame | honey |
| `[!journal]` | notebook-pen | slate |
| `[!memento]` | hourglass | stone, inscription title |

```markdown
> [!quote] Seneca · On the Shortness of Life
> It is not that we have a short time to live, but that we waste a lot of it.
```

## Tiles

Turn a plain list of links into a grid of cards, no JavaScript needed:

```markdown
> [!tiles]
> - [[Fitness]]
> - [[Reading]]
> - [[Home]] #tile/rust
```

The whole tile is clickable. Colours cycle through moss, slate, amber, rust, honey and plum; give a single tile its own colour with a tag `#tile/moss`, `#tile/slate`, `#tile/amber`, `#tile/rust`, `#tile/honey`, `#tile/plum` or `#tile/stone` (the tag is hidden inside the tile). Text after a line break becomes a small subtitle.
Options go after a pipe, e.g. `> [!tiles|cols-3 small]`: `cols-2`, `cols-3`, `cols-4` for a fixed number of columns, `small` for lower tiles.

## Settings

Install the [Style Settings](https://github.com/mgmeyers/obsidian-style-settings) plugin to change:
the wood tone, accent / moss / rust / slate colours, heading style, note and interface font,
line width (560–1600 px, when *Readable line length* is on), plain quotes, contour lines on/off
and their strength, the divider ornament, memento mori and animations.

## Good to know

- **Fonts:** if you have set your own text or interface font under *Settings → Appearance*, it overrides Umbria's fonts. Clear those fields to see Literata and Inter.

## Installation

- **Community themes:** open *Settings → Appearance → Themes → Manage*, search for *Umbria* and install it.
- **Manually:** download `theme.css` and `manifest.json` from the latest release into the folder `.obsidian/themes/Umbria/` inside your vault, then pick *Umbria* under *Settings → Appearance → Themes*.

## Building from source

`theme.css` is generated. Edit `src/theme.src.css`, then run:

```sh
python3 build.py                     # writes theme.css
python3 build.py --install ~/Documents/Notes # also copies it into the vault at that path
```

The build embeds the fonts from `fonts/` and generates the contour-line SVG (Python 3 standard library only).

## Licence

Theme: [MIT](LICENSE). Fonts: Inter, Literata and Cinzel under the SIL Open Font License 1.1, see [fonts/OFL.md](fonts/OFL.md).
