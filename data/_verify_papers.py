import pandas as pd
import requests
import numpy as np

def get_paper_info(title):
    url = "https://api.crossref.org/works"
    params = {
        'query.title': title,
        'rows': 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['message']['items']:
            return data['message']['items'][0]
        else:
            return None
    else:
        response.raise_for_status()

def ConvertFirstName(first_name):
    """ Convert first name in right format. """
    names = first_name.split(' ')
    out_name = ''
    for name in names:
        if name.count('.') == 0:
            out_name += name[0] + "."
        else:
            out_name += name
    return out_name

def CheckValue(val1, val2, name = ""):
    """ Verifies whether value1 is the same as value2.
        If not, a message is displayed. """
    if (type(val1) in [float, np.float64] and np.isnan(val1)):
        return True
    if (type(val2) in [float, np.float64] and np.isnan(val2)):
        return True
    if (type(val1) != type(val2)):
        print("\nTypes of ", name, ':', val1, val2, "are not the same!")
        print(type(val1))
        print(type(val2))
        return False
    else:
        if (val1 != val2):
            if type(val1) == str:
                print("\nDifferent string: ")
                a = []
                for i in range(min(len(val1), len(val2))):
                    if val1[i] == val2[i]:
                        a.append("1")
                    else:
                        a.append("0")
                print(val1)
                print(val2)
                print("".join(a))
                print([ord(l) for l in val1])
                print([ord(l) for l in val2])
                return True
            else:
                print("\nDifferent " + name + ":\n" + str(val1) + "\n" + str(val2))
                return True
        else:
            return False

def month_name(month):
    if (month == 1): return "Jan"
    if (month == 2): return "Feb"
    if (month == 3): return "Mar"
    if (month == 4): return "Apr"
    if (month == 5): return "May"
    if (month == 6): return "Jun"
    if (month == 7): return "Jul"
    if (month == 8): return "Aug"
    if (month == 9): return "Seo"
    if (month == 10): return "Oct"
    if (month == 11): return "Nov"
    if (month == 12): return "Dec"
    return ""

# Load the Excel file
file_path = 'pap.xlsx'
df = pd.read_excel(file_path)
titles = df['title']

# Loop over papers
row = 0
for title in titles:
    
    # print
    print("\nCurrent paper " + str(row+1) + ": " + title[0:min(25,len(title))] + "...")
    
    # based on the title, get information about the paper
    paper_info = get_paper_info(title)
    
    # init
    authors = ""
    title2 = ""
    year = np.float64('nan')
    journal = ""
    doi = ""
    article_type = ""
    volume = np.float64('nan')
    issue = np.float64('nan')
    pages = ""
    month = ""
    publisher = ""
    editor = ""
    
    # if info is obtained
    if paper_info:
        if 'author' in paper_info:
            authors = [ConvertFirstName(author['given']) + ' ' + author['family'] for author in paper_info['author'] if 'given' in author]
            authors = ", ".join(authors)
        else:
            row += 1
            continue
        
        if 'published' in paper_info:
            publication_date = paper_info['published']['date-parts'][0]
        elif 'published-print' in paper_info:
            publication_date = paper_info['published-print']['date-parts'][0]
        else:
            publication_date = [0, np.nan]
        title2 = paper_info['title'][0]
        year = np.int64(publication_date[0])
        article_type = paper_info.get('type', "")
        if (article_type == 'journal-article'):
            article_type = 'journal'
            journal = paper_info['container-title'][0]
        if (article_type == 'posted-content'):
            article_type = 'journal'
            journal = paper_info.get('group-title', '')
        if (article_type == 'book-chapter'):
            article_type = ''
            journal = ''
        if (article_type == 'proceedings-article'):
            article_type = 'conference'
            journal = paper_info['event']['name']
        doi = paper_info['DOI']
        volume = np.float64(paper_info.get('volume', 'nan'))
        if len(paper_info['issued']['date-parts'][0]) > 1:
            issue = np.float64(paper_info['issued']['date-parts'][0][1])
        else:
            issue = np.nan
        pages = paper_info.get('page', '')
        if (pages.count('-') == 1):
            pages = pages.replace('-', '--')
        if len(publication_date) > 1:
            month = month_name(publication_date[1])
        else:
            month = ""
        publisher = paper_info.get('publisher', '')
        
    
    # checks
    if df.loc[row, 'title'] != title2 and len(df.loc[row, 'title']) != len(title2):
        print("Paper passed - not found...")
        df.loc[row, 'notes'] = 'Not found on Scopus by title'
        row += 1
        continue
    
    if CheckValue(df.loc[row, 'authors'], authors, 'authors'):
        df.loc[row, 'authors'] = authors
    if CheckValue(df.loc[row, 'title'], title2, 'title'):
        df.loc[row, 'title'] = title2
    if CheckValue(df.loc[row, 'year'], year, 'year'):
        df.loc[row, 'year'] = year
    if CheckValue(df.loc[row, 'journal'], journal, 'journal'):
        df.loc[row, 'journal'] = journal
    if CheckValue(df.loc[row, 'doi'], doi, 'doi'):
        df.loc[row, 'doi'] = doi
    if CheckValue(df.loc[row, 'article_type'], article_type, 'article_type'):
        df.loc[row, 'article_type'] = article_type
    if CheckValue(df.loc[row, 'volume'], volume, 'volume'):
        df.loc[row, 'volume'] = volume
    if CheckValue(df.loc[row, 'issue'], issue, 'issue'):
        df.loc[row, 'issue'] = issue
    if CheckValue(df.loc[row, 'pages'], pages, 'pages'):
        df.loc[row, 'pages'] = pages
    if CheckValue(df.loc[row, 'month'], month, 'month'):
        df.loc[row, 'month'] = month
    if CheckValue(df.loc[row, 'publisher'], publisher, 'publisher'):
        df.loc[row, 'publisher'] = publisher
    
    # update row number
    row += 1


# Save the DataFrame back to an Excel file
output_file_path = 'pap2.xlsx'
df.to_excel(output_file_path, index=False)
