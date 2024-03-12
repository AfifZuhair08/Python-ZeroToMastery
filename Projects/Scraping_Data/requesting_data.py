import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")

souped = BeautifulSoup(res.text, 'html.parser')

# print(souped.body.contents) # all contents
# print(souped.find_all('a')) # find all with a tag
print(souped.title) # site title