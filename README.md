# NAS publication network

This repository contains a publication network related to the NAS department at TU Delft. Each node represents a current NAS employee, former NAS employee or external collaborator. Nodes are connected if at least one paper is written together. Clicking on a node shows an overview of node properties and the latest three published paper of that person.

## Content

- `data/source_people.xlsx`: list of current and former employees of the NAS department.
Also includes position, topic, institution and url.

- `data/source_papers.xlsx`: list of papers written in the NAS department.

- `src/papers.html`: web page using d3 Javascript library to visualise a network with people as nodes.

- `src/worker.js`: Additional helper Javascript file for heavy network computations such as the clustering coefficient. TODO to be removed.

All papers have been checked on title in the Scopus database, also see `data/_verify_papers.py`
`data/_check_validity_authors_journals`: helps to identify whether the current list of papers is complete/correct.

(There is an additional script `scr/people.html` which is unused)

## Planning

### January 2026

~1a. Investigate current infeastructure~

~1b. Collect wishes of webpage~

~2a. Make planning (all)~

~2b. Arrange access (liza)~

~3. Make GitHub (Massimo)~

~4a. Update website PHP \& Joomla version (Liza)~

~4b. Upload Excel files (Massimo)~

### February 2026

~5a. Make network less cluttered (Matteo)~

~5b. Make separate detail pane on publications page (Massimo)~

### March 2026

~6a. Check removal of banner on top of website page (Roberto)~

~6b. Update people.xlsx with current and former NAS members (Massimo)~

~6c. (Nice to have) For NAS members, add their picture (Matteo)~

~6d. Collect Piet's feedback (Roberto)~

~6e. Add 2024-2025-2026 papers to list (Massimo)~

### Now

7a. Create new tab with table of publications. Columns: Authors, Title, DOI/URL (Roberto)

7b. Optimise network edge highlighting (Matteo)

7c. Make NAS nodes bigger (Matteo)

7d. Add downloadable bibtex (Matteo)

7e. Make network downloadable (possibly in different formats) (Matteo)

7f. Make network fits exactly on the laptop screen (no scrolling required) (Matteo)

7g.  Make simple network statistics (#nodes and #edges) better visible (and also #papers ?) (Matteo)

7h. Researcher detail pane: (1) show more papers than 3? (2) also show collaborators, (3) be able to click on collaborators and navigate to their node (Matteo)

7i. Make it mobile-friendly (Roberto)

7j. Clicking or hovering over a node causes not just its neighbours to get highlighted, but it seems highlighting is based on papers rather than node neighbours (Matteo)

7k. Now nodal info appears twice; once in the left-top when clicked on a node and also when hovered over a node. Show this only once. Also, the top-left popup is moveable, is that intended? (Matteo)

7l. Make NAS and former NAS nodes to be spread out more evenly (Matteo)

7m. Check: Changing the slider "Min. shared papers" causes the number of collaborators of nodes to change (mostly to zero). Is this intentional/desired? (Matteo)

7n. Check: The button "NAS-only" barely does anything, as the NAS people are very visible already. (Matteo)

### Later

- Discuss next steps: is another round of modifications required before beta version? (+- April 2026)

- Beta version: collect feedback from NAS group (+- April 2026)

- Final steps (features \& bugfixing) (+- May 2026)

- Live! (+- June 2026)

### Known bugs:

- current implementation of papers only distinguishes between names. People with similar first letters and last name will be (incorrectly) aggregated together. From the list of papers, this is very complicated to add to without completely manually going over this paper by paper.

## Joomla settings

Confirmed working in Joomla 6.0.2 with PHP 8.4.17.

In Joomla, Excel files are not uploadable by default. They should be enabled first.

In the left navigation bar, go to "Content" -> "Media". Click "Options" in the top-right corner.


## Old requirement list

### Development

- Show a network (with 3dJS) with people as nodes and connect people if they wrote a paper together (Mh)
- Website hosts an Excel file from which the network is built (Mh)
- Excel should be easily editable by webmaster (Mh)
- Excel should be editable by everyone (Ch)
- Visualisation should match NAS colours (Mh)
- Less cluttered visualization (Sh)
- You should be able to interact with the network (drag \& click on nodes) (Mh)
- Clicking a node shows node information (Mh)
- Node should have different colours for NAS, ex-NAS and others (Sh)
- When a node is selected should become orange (not red which indicates former NAS employees) (Sh)
- Color gradient for seniority (Ch)
- Search function for names (Sh)
- Visualisation should have a toggle to show names (tbd)
- Visualisation should have toggle to show only NAS members (tbd)
- Network should be downloadable in various formats (Sh)
- List of papers should be downloadable as bib (Ch)
- Calculate and show network statistics (Ch)
- The visualization can also show, on the right of the full network, a subgraph of the selected node

### After development before live:
- Carefully check papers for correctness (Mh)
- Update people list with current and former NAS members (Mh)
- Update paper list (Mh)

### When live
- Constantly add new papers by website admin (Mh)
Allowed extensions: Add "xlsx"

Legal Document Extensions (File Types): Add "xlsx"

Legal MIME Types: Add "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

