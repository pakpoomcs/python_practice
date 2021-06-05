from bs4 import BeautifulSoup
import urllib.request
import csv
url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

response = urllib.request.urlopen(url)
soup = BeautifulSoup(response)
for link in soup.find_all("a"):
    print("Inner Text: {}".format(link.text))
    print("Title: {}".format(link.get("title")))
    print("href: {}".format(link.get("href")))
