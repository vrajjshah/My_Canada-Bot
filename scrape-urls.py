from bs4 import BeautifulSoup
import requests

#The Website from which you want to scrape the URl's
html = requests.get('https://www.bac-lac.gc.ca/eng/discover/Pages/a-z-index.aspx').text
bs = BeautifulSoup(html,"html.parser")

#The File on which you want to write the URL's scraped
file1 = open("articles.txt", "a")

#CSS Class of all the links that I wanted to scrape
for possible_links in bs.select(".margin-bottom-medium"):
    for link in possible_links:
        if link.has_attr('href'):
            temp = link.attrs['href']
            if(temp.find("http://www.bac-lac.gc.ca") != -1):
                file1.write(link.attrs['href']+'\n')

file1.close() 
    