from bs4 import BeautifulSoup
import requests

# fill in the URL here
url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

# Create a GET request to fetch the raw HTML content, representing it in a variable.
content = requests.get(url).text

# Parse the HTML content
soup = BeautifulSoup(content, "html.parser")
for link in soup.find_all("a"):
    print("Inner Text: {}".format(link.text))
    print("Title: {}".format(link.get("title")))
    print("href: {}".format(link.get("href")))
