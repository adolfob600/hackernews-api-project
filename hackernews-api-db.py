import json
import requests
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd


def make_a_dict(title, author, link):
  dict = {
  'Title': [title],
  'Author': [author],
  'Link': [link],

  }

  return dict


BASE_URL = "https://hacker-news.firebaseio.com/v0/"


def get_newest_story(BASE_URL):
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
  return newest_story
  

request = requests.get(BASE_URL + 'item/' + get_newest_story(BASE_URL) + '.json')
data = request.json()

author = data['by']
title = data['title']
link = data['url']

dict = make_a_dict(title, author, link)

df = pd.DataFrame.from_dict(dict)

engine = create_engine('mysql://root:codio@localhost/hackernews_api_db')
df.to_sql('hackernews_api_db', con=engine, if_exists='replace', index=False)