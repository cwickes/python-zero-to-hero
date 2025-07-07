import requests
from bs4 import BeautifulSoup

res = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(res.text, 'html.parser')

authors = soup.find_all(itemprop='author')
authors = {author.text for author in authors}

quotes = soup.find_all(itemprop='text')
quotes = [quote.text for quote in quotes]

tags_box = soup.find(class_='tags-box')
tags = tags_box.find_all(class_='tag')
tags = [tag.text for tag in tags]

base_url = 'http://quotes.toscrape.com'
href = ''
authors = set()
while True:
    res = requests.get(base_url + href)
    soup = BeautifulSoup(res.text, 'html.parser')
    author_tags = soup.find_all(itemprop='author')
    authors.update([author.text for author in author_tags])
    next_tag = soup.find(class_='next')
    if next_tag is None:
        break
    href = next_tag.a['href']
print(authors)