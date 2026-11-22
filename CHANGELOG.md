# Changelog

## 1.2.0

**New**
- **Tiles 2.0:** an emoji before the link becomes the tile's icon, `*italic*` text after it becomes the subtitle, and an embedded image (`![[cover.jpg]]`) becomes a cover with a gradient under the title.
- New tile options: `list` (compact rows), `wide` (first tile spans the row), `plain` (one neutral colour), `mono` (accent only) and `cols-5`.
- **Note layouts** via `cssclasses`: `wide`, `max`, `table-wide`, `img-grid` (image gallery), `cards` (Dataview tables as cards) and `no-topo`.
- **Wood "Ash":** neutral charcoal in dark mode and stone paper in light mode, for anyone who prefers no brown.
- **Heading colour** setting: ink (default), accent title & H1, accent, or earth tones (each level its own colour).
- **Higher contrast** setting: stronger muted text, borders and checkboxes in every wood and mode.
- **Quiet interface** setting: ribbon, status bar, view actions and inactive tabs fade until you hover them.
- **PDF export:** white paper, no shadows or contour lines, compact tiles without images, and headings that don't end up alone at the bottom of a page.
- **Mobile:** tighter quotes, callouts, tables and tiles on phones; two-column tiles and cards; no hover lift on touch screens.
- Syntax colours from the palette, a small language label on code blocks, footnotes with accent numbers, embedded notes as soft cards and images with rounded corners.
- Visible keyboard focus rings in the accent colour.
- Plugin styling for Kanban, Banners, Iconize, Outliner and Omnisearch.
- `demo/Umbria Showcase.md`: one note with every element, to try the theme or check a release.

**Fixed**
- The large quotation mark on quotes and quote callouts was cut off at the top since 1.1.0. It is visible again.

**Changed**
- Link text in light mode is a little darker, so it meets WCAG AA (4.5:1) on every paper.
- Long tile titles wrap between words, with hyphenation, instead of anywhere.

**Heads-up:** tile subtitles are now written in `*italic*` after the link. Plain text after a line break, as in 1.1, is now shown in the large icon size. Change `[[Note]]<br>Subtitle` to `[[Note]] *Subtitle*`.

## 1.1.0

**New**
- Every wood tone now has a light paper too: Ember → linen, Pine → sage, Autumn → clay.
- Contour lines take on your accent colour (and theme.css is about 100 KB smaller).
- `[!tiles]` callout: turn a list of links into a grid of clickable cards.
- New callouts `[!memento]` and `[!journal]`; task states `[?]` question and `[*]` star.
- Canvas, Graph view and Bases (tables, cards, kanban) styled in the Umbria palette.

**Heads-up:** Style Settings IDs were renamed to English. If you had changed Umbria settings (wood, headings, contour lines, divider, plain quotes, line width, animations), they are back to their defaults; please set them again once.
The German callout aliases (`[!zitat]`, `[!stoa]`, `[!reflexion]`, `[!praxis]`, `[!gedanke]`, `[!dankbar]`) were removed; use the English names.

## 1.0.1

- Recognisable MIT licence, README without placeholders, smaller theme.css.

## 1.0.0

- First release.
