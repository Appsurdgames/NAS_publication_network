# NAS publication network

This repository contains two networks related to the NAS department at TU Delft.



Part 1: People network

people.xlsx: list of current and former employees of the NAS department.

Also includes position, topic, institution and url.

people.html: show an interactive network with currently employed researchers in NAS, connected by topic and institution.



Part 2: Publication network

NAS\_papers\_v4.xlsx: list of papers written in the NAS department.

All papers have been checked on title in the Scopus database, also see verifyPapers.py

verifyPapers.xlsx: Allows for automatically filling in details about papers based on

their title using the Scopus database. Not all papers will be findable, and will receive

a separate tag.

check\_validity\_authors\_journals: helps to identify whether the current list of papers is complete/correct.

papers.html: web page using d3 Javascript library to visualise a network with people as nodes. Nodes are connected if two nodes wrote a published paper together. Clicking on a node shows an overview of node properties and the latest three published paper of that person.

worker.js: Additional helper Javascript file for heavy network computations such as the clustering coefficient.



Wishes:

\- Show a network (with 3dJS) with people as nodes and connect people if they wrote a paper together (Mh)

\- Website hosts an Excel file from which the network is built (Mh)

\- Excel should be easily editable by webmaster (Mh)

\- Excel should be editable by everyone (Ch)

\- Visualisation should match NAS colours (Mh)

\- Less cluttered visualization (Sh)

\- You should be able to interact with the network (drag \& click on nodes) (Mh)

\- Clicking a node shows node information (Mh)

\- Node should have different colours for NAS, ex-NAS and others (Sh)

\- When a node is selected should become orange (not red which indicates former NAS employees) (Sh)

\- Color gradient for seniority (Ch)

\- Search function for names (Sh)

\- Visualisation should have a toggle to show names (tbd)

\- Visualisation should have toggle to show only NAS members (tbd)

\- Network should be downloadable in various formats (Sh)

\- List of papers should be downloadable as bib (Ch)

\- Calculate and show network statistics (Ch)



After development before live:

\- Carefully check papers for correctness (Mh)

\- Update people list with current and former NAS members (Mh)

\- Add new papers (Mh)



Known bugs:

\-  current implementation of papers only distinguishes between names. People with similar first letters and last name will be (incorrectly) aggregated together. From the list of papers, this is very complicated to add to without completely manually going over this paper by paper.



Steps (Oct 2025)

1a. (DONE) Investigate current infeastructure

1b. (DONE) Collect wishes of webpage

2a. Divide wishes into must-haves, should-haves and could-haves

2b. (DONE) Arrange access

3\. Build Must-haves into current webpage format (who?)

4\. Discuss next steps

5a. Build should-haves \& bugfixing

5b. Assemble final paper list \& employee list

6\. Beta version, collect feedback

7\. Final steps (features \& bugfixing)

8\. Live!



Plan: (Jan 2026)

1\. Make GitHub (Massimo)

2a. Update website PHP \& Joomla version (Liza)

2b. Upload Excel file (Massimo)

3a. Create new tab with table of publications (Roberto)

Columns: Authors, Title, DOI/URL

3b. Make network less cluttered (Mattia)

3c. Make separate detail page (Massimo)



After release:

\- Updating Excel file by admin



Data is collected from the NAS website, subpage Publications.

Code is created by Massimo Achterberg, 2024.

Last changed: 2025-10-17

