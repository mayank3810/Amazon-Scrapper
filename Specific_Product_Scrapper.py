from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
## CHANGE URL HERE##

amazon_page ='https://bluelimelearning.github.io/my-fav-quotes/'

#*******************
uClient = urlopen(quotes_page)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
#quotes = page_soup.findAll("div", {"class": "quotes"})
Produt_name = page_soup.find("span" , {"id": "productTitle"})

'''for quote in quotes:
    fav_authors = quote.findAll("p" , {"class": "author"})
    author = fav_authors[0].text.strip()

    print(author)'''