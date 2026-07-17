# NAS Publication Network — `src/`

Two standalone, static HTML pages that visualize the NAS Section's co-authorship
network and publication list. No build step — open the files directly in a browser
(or serve the repo root as a static site) and they fetch their data client-side.

- **[`network.html`](network.html)** — interactive network graph of researchers and their co-authorships.
- **[`table.html`](table.html)** — sortable/filterable table of every paper.

Both pages link to each other via the "Network" / "Table" tabs at the top, and
share a single **light/dark theme** that persists across both pages.

## Data dependencies

Both files fetch spreadsheets at runtime via `fetch()`, relative to their own
location (`../data/...`). They must be served over `http(s)://`, not opened via
`file://`, since `fetch()` on a local file is blocked by the browser in most
setups.

| File | Used by | Contents |
|---|---|---|
| `../data/source_people_new.xlsx` | `network.html` | One row per known researcher: name, abbreviation(s), position/status, profile URL, picture. |
| `../data/source_papers.xlsx` | `network.html`, `table.html` | One row per paper: title, authors (comma-separated), year, journal, DOI. |

`network.html` cross-references the two files: every author string in the papers
sheet that doesn't match a known person becomes an "external researcher" node.

---

## `network.html`

### What it shows

Each **node** is a person; each **edge** is a co-authored paper (edges thicken/darken
with the number of shared papers). Node color encodes category, node size encodes
publication count:

| Color | Category | Size multiplier |
|---|---|---|
| Blue | Current NAS employee | ×1.34 |
| Red | Former NAS employee | ×1.16 |
| Gold | Former NAS Master student | ×1.0 |
| Green | External researcher (anyone in the papers sheet not in the people sheet) | ×1.0 |

Base size follows `sqrt(numPapers)`.

### Layout: one spiral per category

Nodes are **not** force-simulated — positions are deterministic so the same
filters always produce the same layout. Each of the four categories above is
laid out along its own continuous Archimedean-style spiral (`layoutCategoryShells()`):

- Nodes are ordered by **descending paper count** (ties broken by degree, then
  name), so the biggest/most-published nodes sit closest to the spiral's start
  and taper outward — matching the fact that node *size* is also driven by
  paper count.
- The spiral grows outward continuously (not as independent rings that reset
  their start angle), so degree order reads smoothly from center to edge
  instead of resetting at each ring boundary.
- Spacing is based on the *largest* node in the category rather than the
  average, so a run of same-sized nodes adjacent on the spiral still can't
  overlap.
- The four categories start at 0°/90°/180°/270° so their spirals are visually
  distinguishable, and each category's spiral begins outside the previous
  one's outer radius.
- In **"NAS only"** mode, hidden categories are parked far outside the visible
  area (`placeRing()`) rather than removed, so toggling back doesn't require a
  relayout.

### Interactions

- **Hover** a node → fades everything except it and its collaborators,
  enlarges its label (normal weight).
- **Click** a node → pins the same highlight and opens the **detail panel**
  (top-left: photo, position, paper count, latest papers, clickable
  collaborator list). Pinned label is enlarged **and bold**. Click empty
  canvas, or the panel's ✕, to unpin.
- **Search box** — autocomplete dropdown; picking a result pins that node.
  Typing without picking a result also highlights all matches + their edges.
- **Filters** — min. shared papers per edge, min. papers per author, "NAS
  only" toggle (current employees only, others parked off-screen).
- **Show/Hide labels** — toggles all name labels; the focused/hovered node's
  label always shows regardless of this setting.
- **Reset** — clears search, pin, and hover state.
- **Pan/zoom** — standard drag + scroll/pinch (d3-zoom); the view auto-fits
  to the visible nodes on every redraw, biased slightly above vertical center
  so the graph sits closer to the controls bar.
- **Download network ▾** — exports the *currently visible/filtered* graph as
  JSON, an edge-list CSV, or a node-list CSV.

### Hover performance note

Hover/click focus updates (`applyFocusNode()`/`clearStyles()`) are
**diff-based**, not a full re-scan: they track which nodes/edges were
touched by the *previous* call and only mutate the symmetric difference
between old and new state (via direct `classList`/`setAttribute` calls
through name→DOM-element lookup maps, bypassing D3's per-call selection
filtering). Moving the mouse from node A to node B touches roughly
`degree(A) + degree(B)` elements instead of sweeping all ~700 visible nodes
on every mouse event — this was a deliberate fix for hover feeling sluggish
in Chromium-based browsers. The DOM is intentionally **not** reordered
(no z-order "raise" on focus) — an earlier version did this and it triggered
a Chromium hover-tracking bug where `mouseleave` stopped firing after a
node was reparented mid-hover, making hovering appear to "get stuck" until
a click forced a hit-test refresh.

### Data export field notes

`institutions` is only populated in exports for **current** NAS members
(`isUniversity === 1`). For former employees/students and external
researchers, the underlying `position`/institutions text is a free-form
description (e.g. "Former PhD student, now Postdoc at TU Delft") that isn't
a clean institution name, so it's intentionally left blank in the exported
JSON/CSV even though it may still show under a person's name in the detail
panel.

---

## `table.html`

A flat, sortable, filterable table of every row in `source_papers.xlsx`
(Title / Authors / Year / Journal / Link-to-DOI). Click a column header to
sort (click again to reverse). Free-text filters per column, combined with
AND. "Download all papers as CSV" exports the current filtered+sorted view.

---

## Shared theming

Both pages read/write the same `localStorage` key, **`nas-network-theme`**
(`"light"` or `"dark"`), applied via a `data-theme` attribute on `<html>`
*before* first paint (an inline IIFE at the top of each `<script>`) to avoid
a flash of the wrong theme. All themeable colors are CSS custom properties
declared once in `:root` (light) and overridden under `:root[data-theme="dark"]`.
A handful of values used by inline SVG/JS styling (D3-drawn text/strokes,
plus two `<span>`s injected into the detail panel) read the live CSS
variable at render time via a small `cssVar()` helper, so they follow theme
switches too. Toggling the "Dark theme"/"Light theme" button next to the
page tabs updates the other page's theme the next time it's loaded, since
both read the same stored preference on load.

## Known limitations

- Requires the pages be served over HTTP — `fetch()` of the local `.xlsx`
  files will fail under `file://`.
- `network.html`'s deterministic spiral layout assumes each category is
  reasonably size-homogeneous within short spans of the spiral; extreme
  outliers (a handful of massively over-published nodes) can still cause
  local crowding.
- No automated tests — both pages are hand-verified in-browser (Chrome,
  Edge, Firefox).
