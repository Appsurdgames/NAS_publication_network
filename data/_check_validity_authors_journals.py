import numpy as np
import pandas as pd

df = pd.read_excel('NAS_papers_v4.xlsx')

# authors
names_total = []
authors = df['authors'].values
for al in authors:
    names = al.split(',')
    names_total.extend([name.strip() for name in names])

author_set = sorted(list(set(names_total)))
for name in names_total:
    if len(name) < 3:
        print("Error name: " + name)
print(len(author_set))
for a in author_set:
    print(a)
print("Author letters")
lst = []
for a in author_set:
    lst.extend(list(a))
author_letters = sorted(list(set(lst)))
print(author_letters)

# journals
journal_total = df['journal'].values
journal_set = sorted(list(set(journal_total)))
#for a in journal_set:
#    print(a, list(journal_total).count(a))
print("Journal letters")
lst = []
for a in journal_set:
    lst.extend(list(a))
journal_letters = sorted(list(set(lst)))
print(journal_letters)

# titles
title_total = df['title'].values
title_set = sorted(list(set(title_total)))
if len(title_total) != len(title_set):
    print(len(title_total), len(title_set))
    for title in title_set:
        if list(title_total).count(title) > 1:
            print("\nThis paper appears more than once:")
            print(title)
print("Title letters")
lst = []
for a in title_set:
    lst.extend(list(a))
title_letters = sorted(list(set(lst)))
print(title_letters)
