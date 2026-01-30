# NAS publication network

This repository contains a publication network related to the NAS department at TU Delft.

## Part 1: People

- people.xlsx: list of current and former employees of the NAS department.
Also includes position, topic, institution and url.

## Part 2: Publication network

- NAS\_papers.xlsx: list of papers written in the NAS department.

- papers.html: web page using d3 Javascript library to visualise a network with people as nodes. Nodes are connected if two nodes wrote a published paper together. Clicking on a node shows an overview of node properties and the latest three published paper of that person.

- worker.js: Additional helper Javascript file for heavy network computations such as the clustering coefficient. This should probably be omitted.

All papers have been checked on title in the Scopus database, also see _verify_papers.py
\_check\_validity\_authors\_journals: helps to identify whether the current list of papers is complete/correct.

# Requirements / wishes:

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

# After development before live:
- Carefully check papers for correctness (Mh)
- Update people list with current and former NAS members (Mh)
- Update paper list (Mh)

# When live
- Constantly add new papers by website admin (Mh)

# Known bugs:

-  current implementation of papers only distinguishes between names. People with similar first letters and last name will be (incorrectly) aggregated together. From the list of papers, this is very complicated to add to without completely manually going over this paper by paper.

# Planning

~1a. Investigate current infeastructure~

~1b. Collect wishes of webpage~

~2a. Make planning (all)~

~2b. Arrange access (liza)~

~3. Make GitHub (Massimo)~

4a. Update website PHP \& Joomla version (Liza)

4b. Upload Excel file (Massimo)

5a. Create new tab with table of publications. Columns: Authors, Title, DOI/URL (Roberto)

5b. Make network less cluttered (Mattia)

5c. Make separate detail page (Massimo)

6. Discuss next steps

7. Assemble final paper list \& employee list

8. Beta version, collect feedback

9. Final steps (features \& bugfixing)

10. Live!


