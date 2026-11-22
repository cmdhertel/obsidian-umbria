---
cssclasses:
  - img-grid
---

This note shows every element Umbria styles. Put it and `umbria-hills.svg` into any vault and open it in Reading view and Live Preview, in dark and light mode.

# Heading one
## Heading two
### Heading three
#### Heading four
##### Heading five

Body text in Literata with a [[wiki link]], an [external link](https://obsidian.md), `inline code`, ==a highlight==, **bold**, *italic* and ~~struck~~ text. A footnote sits here.[^1]

---

## Quotes

> It is not that we have a short time to live, but that we waste a lot of it.

> [!quote] Seneca · On the Shortness of Life
> Life is long if you know how to use it.

## Callouts

> [!stoic] The obstacle
> What stands in the way becomes the way.

> [!reflection] Evening review
> What went well today? What would I do differently?

> [!practice] Morning walk
> Twenty minutes, no phone.

> [!thought]
> An idea worth keeping.

> [!gratitude]
> Warm bread, a clear sky, a long call with an old friend.

> [!journal] 22 November
> Quiet day. Read, cooked, walked.

> [!memento] Memento mori
> You could leave life right now.

> [!note]
> The built-in callouts (note, tip, warning, danger, …) use the same earth palette.

## Tiles

Icons, subtitles and colours:

> [!tiles|cols-4]
> - 🌱 [[Garden]] *Beds and seeds*
> - 📚 [[Reading]] *12 books this year*
> - 🏠 [[Home]]
> - 🥋 [[Training]] #tile/plum *Tuesday · Friday*

Image covers, the first tile spanning the full row:

> [!tiles|cols-3 wide]
> - ![[umbria-hills.svg]] [[Travel]] *Umbria, autumn*
> - ![[umbria-hills.svg]] [[Photos]]
> - 🎧 [[Music]] *Playlists*

Compact list:

> [!tiles|list]
> - 🌱 [[Garden]] *Beds and seeds*
> - ![[umbria-hills.svg]] [[Travel]] *Umbria*
> - 📚 [[Reading list]]
> - ✍️ [[Journal]] *daily*

Small, plain and five columns:

> [!tiles|cols-5 small plain]
> - [[Inbox]]
> - [[Projects]]
> - [[Areas]]
> - [[Resources]]
> - [[Archive]]

## Tasks

- [ ] To do
- [x] Done
- [/] In progress
- [!] Important
- [?] Question
- [*] Star
- [-] Cancelled
- [>] Deferred

## Table

| Wood | Dark | Light |
|---|---|---|
| Ember | espresso | linen |
| Pine | forest | sage |
| Autumn | red-brown | clay |
| Ash | charcoal | stone |

## Code

```js
// Walk the hills at dusk
const hills = ["Assisi", "Spello", "Montefalco"];
for (const town of hills) {
  console.log(`Arrived in ${town}`);
}
```

## Images

With `cssclasses: img-grid`, several images in one paragraph form a gallery:

![[umbria-hills.svg]] ![[umbria-hills.svg]] ![[umbria-hills.svg]]

## Embeds

An embedded section of this note:

![[#Quotes]]

## Note layouts

Add these to `cssclasses` in a note's properties:

- `wide`: wider than the readable line length
- `max`: the full width of the pane
- `table-wide`: tables stretch to full width
- `img-grid`: images in one paragraph become a gallery
- `cards`: Dataview tables turn into a card grid (first column is the title, an image column becomes the cover)
- `no-topo`: no contour lines behind this note

[^1]: Footnotes are small and muted, with accent-coloured numbers.
