from bs4 import BeautifulSoup
import codecs

raw_html = codecs.open("test.html", 'r').read()
soup = BeautifulSoup(raw_html, features="html.parser")

#print(soup.title.text)

table = soup.find("table", attrs={"border": ""})
table_data = table.tbody.find_all("tr")
#print(table_data)

headings = []
for td in table_data[0].find_all("td"):
    headings.append(td.text.replace('\n', ' ').strip())
print(headings)