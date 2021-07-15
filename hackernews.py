import json
import requests



BASE_URL = "https://hacker-news.firebaseio.com/v0/"
NEW_STORIES = "newstories.json"


item_ids = requests.get(BASE_URL + NEW_STORIES)

i = item_ids.json() # list of new story ID's #
newest_story = ''

for item in i:

  x = requests.get(BASE_URL + 'item/' + str(item) + '.json')
  y = x.json()
  
  if y['type'] == 'story':
    newest_story = str(item)
    break



r = requests.get(BASE_URL + 'item/' + newest_story + '.json')

d = r.json()

print( '\n\nTitle: ' + d['title'] + '\nAuthor: ' + d['by'] + '\nLink: ' + d['url'] + '\n\n')