import csv
from bs4 import BeautifulSoup

infoNA = ['NA'] * 14

start = ['title', 'intro', 'plot', 'film_name', 'director', 'producer', 'writer', 'starring', 'music', 'release date',
         'runtime', 'country', 'language', 'budget']

infoVar = ['Directed by', 'Produced by', 'Written by', 'Starring', 'Music by', 'Release date', 'Running time',
           'Country', 'Language', 'Budget']



def parse(bf):
    info = infoNA
    infobox = bf.table.find_all('tr')
    info[:4] = [bf.title.text, bf.find_all('p')[0].text, bf.find_all('p')[1].text, infobox[0].text]
    
    for j in range(len(infoVar)):
        for i in range(2, len(infobox)):
                if infobox[i].th is not None and infoVar[j] == infobox[i].th.text:
                    info[j + 4] = infobox[i].td.text  
                break
        return info


for i in range(9999):
    #if i == 54:
        #continue
    f = open('/home/giorgio/ADM/Homework3/Pages/article_%d.html' % i).read()
    bf = BeautifulSoup(f, 'html.parser')
    infoNA = parse(bf)

    with open('/home/giorgio/ADM/Homework3/PagesTSV/output_%d.tsv' % i, 'w') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow(start)
        tsv_writer.writerow(infoNA)
