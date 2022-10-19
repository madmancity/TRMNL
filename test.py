from bs4 import BeautifulSoup
import requests
import re
def regex(html_doc, case1,case2):
    x = re.search(case1, html_doc)
    x = re.search(case1, html_doc).group()
    y = re.search(case2, x)
    y = re.search(case2, x).group()
    #print(x)
    #print(y)
    return y
url = 'https://flightaware.com/live/flight/UAE523'
r = requests.get(url)
r.text
html = r.text







x = re.search("'origin', '....'", html).group()
#print(x)
y = re.search("[A-Z]...", x).group()
#print(y)
soup = BeautifulSoup(html, 'html.parser')


#print(soup.find_all("div", class_="flightPageCondensedSummary"))
#cls = soup.div
#print(cls)
