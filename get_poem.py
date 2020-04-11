import requests
from bs4 import BeautifulSoup
import random
from langdetect import detect


URL = "https://allpoetry.com"


def get_poem():
    url = "https://allpoetry.com/classics/famous_by/" + chr(random.randrange(1, 27, 1) + 64)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    table = soup.find('div', attrs={'class': 'items tiny users one-line fixed-width' })
    authors_list = table.findAll('div', attrs={'div', 'itm'})

    # selecting a random author
    num = random.randrange(0, len(authors_list), 1)
    author_url = URL + authors_list[num].a['href']
    author_name = authors_list[num].a['href']
    author_name = author_name.replace('/', '')
    author_name = author_name.replace('-', ' ')
    req = requests.get(author_url)

    # getting poem from author

    soup2 = BeautifulSoup(req.content, 'html5lib')
    table2 = soup2.find('div', attrs={'class': 't_main'})
    poem_list = table2.findAllNext()
    poem_title = poem_list[0].h1.get_text()
    poem = {
            'poem': poem_list[0].div.form.contents[2].contents[1].get_text(),
            'poem_title': poem_list[0].h1.get_text(),
            'author_name': author_name
    }

    if detect(poem['poem'])=='en':
        return poem
    else:
        return get_poem()

