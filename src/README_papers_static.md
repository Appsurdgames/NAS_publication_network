# NAS Publication Network – `papers_static.html`

An interactive, self-contained visualisation of the NAS research group's co-authorship network. It runs entirely in the browser with no build step or backend required.

---

## Overview

The page renders a **radial node-link diagram** where each author is a circle placed on one of three concentric rings, and lines between them represent shared publications. All data is loaded at runtime from two Excel files, so updating the network requires only updating the spreadsheets.

---

## Data sources

| File | Description |
|------|-------------|
| `../data/source_people.xlsx` | One row per person — columns used: `name_abbrev`, `position`, `institutions`, `url` |
| `../data/source_papers.xlsx` | One row per paper — columns used: `authors` (comma-separated `name_abbrev`), `title`, `year`, `doi` |

Authors listed in the papers file but absent from the people file are automatically added as **external collaborators**.

---

## Layout

Authors are placed on three rings using their `position` field:

| Ring | Radius | Colour | Criteria |
|------|--------|--------|----------|
| Inner | 180 px | Blue `#18A8D5` | Current NAS members |
| Middle | 300 px | Orange `#D54518` | Former NAS members |
| Outer | 420 px | Green `#52c9a4` | External collaborators |

Node size scales with number of papers (square-root scale, 3–16 px radius). Link thickness scales linearly with the number of co-authored papers.

---

## Controls

| Control | Effect |
|---------|--------|
| **Min. shared papers** slider | Hides links below the chosen co-authorship count |
| **Min. papers per author** slider | Hides nodes with fewer papers than the threshold |
| **Search box** | Highlights a specific author with live autocomplete |
| **Show labels** | Toggles author name labels on/off |
| **NAS only** | Restricts the view to current NAS members |
| **Reset** | Clears all highlights and filters |

---

## Interaction

- **Hover** a node → highlights its direct connections; collaborators get an orange ring, links turn orange.
- **Click** a node → pins the tooltip (shows name, position, institution, paper count, collaborator count, and up to 3 recent papers with DOI links); the selected node gets a thicker orange ring.
- **Drag** a pinned tooltip to reposition it; click the × to close it.
- **Scroll / pinch** to zoom; **drag** the canvas to pan. Zoom is clipped to the SVG viewport so it does not overlap the controls bar.
- Clicking outside the chart dismisses any active highlight.

---

## Key constants (top of `<script>`)

```js
const WIDTH  = 1300;   // SVG width in pixels
const HEIGHT = 900;    // SVG height in pixels
const R_NAS    = 180;  // inner ring radius
const R_FORMER = 300;  // middle ring radius
const R_EXT    = 420;  // outer ring radius
```

Adjust these to resize or rebalance the diagram.

---

## Dependencies (CDN, no install needed)

- [D3.js v6](https://d3js.org/) — layout, rendering, zoom
- [SheetJS (xlsx)](https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.16.9/xlsx.full.min.js) — Excel parsing
