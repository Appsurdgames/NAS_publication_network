# NAS Publication Network - papers_static_2.0.html

This document describes what was updated in papers_static_2.0.html compared to papers_static.html.

---

## Summary

papers_static_2.0.html keeps the same data sources and base radial network concept, but improves:

- interaction clarity,
- performance during hover/click highlighting,
- export/readout features,
- full-screen fit behavior,
- node-size transparency.

---

## Main updates vs papers_static.html

| Area | papers_static.html | papers_static_2.0.html |
|------|---------------------|--------------------------|
| Viewport/layout | Fixed SVG size (1300x900) with possible page scrolling | Dynamic chart sizing to fit viewport; no page scrolling in normal use |
| Network stats | Small single text line for nodes/links | Dedicated stats bar (nodes, edges, papers) plus footer summary |
| Node sizing | Radius by paper count (sqrt scale) | Radius by paper count (sqrt scale) plus group multipliers (NAS/former/external) |
| Sizing transparency | Not explicitly shown in UI | Footer explains exact sizing rule and multipliers |
| Hover behavior | Hover could show full tooltip info | Hover highlights neighborhood and shows node label only (no info panel) |
| Click behavior | Tooltip + highlight | Click pins detail panel and highlight; selected label shown and rendered on top |
| Duplicate info overlays | Could appear both as floating hover info and pinned state | Single detail panel model; no duplicate hover panel |
| Collaborator navigation | Not clickable from details | Collaborators listed as clickable links in detail panel to jump to node |
| Detail panel content | Up to 3 recent papers | Up to 10 recent papers, plus collaborator chips and counts |
| NAS-only mode | Limited visual impact | NAS-only layout is visually stronger/focused |
| Ring labels | Text labels on rings | Ring text removed; legend only |
| Export | No graph export buttons | Export buttons for JSON, edges CSV, nodes CSV |
| Highlight correctness | Reported confusion around over-highlighting | Neighbor/incident-edge based highlighting logic |

---

## New/changed controls

Additional buttons in 2.0:

- Download JSON
- Download edges CSV
- Download nodes CSV

Existing controls are preserved (threshold sliders, search, labels toggle, NAS-only, reset).

---

## Interaction model in 2.0

- Hover node:
  - highlights only direct neighborhood links/nodes,
  - shows only that node label if labels are otherwise hidden,
  - does not open the detail panel.
- Click node:
  - pins node selection,
  - opens detail panel,
  - keeps focused node label visible,
  - raises focused node group so label is not covered.
- Click collaborator in panel:
  - jumps to and pins that collaborator node.

---

## Performance-oriented updates

Compared to papers_static.html, 2.0 adds optimizations to reduce hover/click latency:

- precomputed visible-neighbor and visible-incident-edge maps,
- cached top-paper snippets per node,
- delegated click handling inside detail panel,
- requestAnimationFrame-based hover scheduling,
- avoids full redraw for simple pin/clear operations when possible.

---

## Data compatibility

Input files are unchanged:

- ../data/source_people.xlsx
- ../data/source_papers.xlsx

So migration from papers_static.html to papers_static_2.0.html does not require changing the spreadsheets.

---

## Current node-size formula in 2.0

Node radius is computed as:

radius = sqrtScale(numPapers) * groupFactor

Group factors:

- NAS: 1.34
- Former NAS: 1.16
- External: 1.00

(Here numPapers is publication count, not graph degree.)
