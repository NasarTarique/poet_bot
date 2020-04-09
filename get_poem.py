import requests
import html5lib
from bs4 import BeautifulSoup
import random
from langdetect import detect

# URL = "https://allpoetry.com/classics/famous_by/"
URL = "https://allpoetry.com"


def poem():
    url = "https://allpoetry.com/classics/famous_by/" + chr(random.randrange(1,27,1) + 64)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    table = soup.find('div' , attrs = { 'class': 'items tiny users one-line fixed-width' })
    authors_list = table.findAll('div' , attrs = {'div' , 'itm'})
    num = random.randrange(0,len(authors_list),1)
    author_url = URL + authors_list[num].a['href']
    print(author_url)
    req = requests.get(author_url)
    soup2 = BeautifulSoup(req.content, 'html5lib')
    table2 = soup2.find('div', attrs={'class': 't_main'})
    # print(table2.prettify())
    poem_list = table2.findAllNext()
    print(poem_list[0])


if __name__ == "__main__":
    poem()