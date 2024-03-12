import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")

souped = BeautifulSoup(res.text, 'html.parser')

# CSS Selectors
# . for class
# # for id

links = souped.select('.titleline')
# OR links = souped.select('.titleline > a')
subtext = souped.select('.subtext')
# print(votes[0])
# print(votes[0].get('id'))
# print(links)

def create_custom_hn(links, subtext):
    hn = []
    for index, item  in enumerate(links):
        
        title = links[index].getText()
        
        # get all links inside a tag with id -> href
        href = links[index].find('a')['href']
        
        # get vote(score) from subtext class
        vote = subtext[index].select('.score')
        
        # if has vote
        if len(vote):
            # return points data with removed strings and convert to integer
            points = int(vote[0].getText().replace(" points", ""))
            
            if points > 99:
            
                hn.append({
                    "title": title,
                    "link": href,
                    "points": points
                })
    return hn

pprint.pprint(create_custom_hn(links, subtext), sort_dicts=False)