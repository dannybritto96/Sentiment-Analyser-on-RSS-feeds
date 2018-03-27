# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:16:47 2018

@author: danieb
"""
import feedparser
import html2text
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#       Loading Data
raw_rss = [
        'http://bitcoin.worldnewsoffice.com/rss/category/1',
        'https://www.coindesk.com/feed/',
        'https://99bitcoins.com/feed',
        'https://bitcoin.org/en/rss/blog.xml',
        'https://blog.spectrocoin.com/en/feed/',
        'https://bitcoin.stackexchange.com/feeds?format=xml',
        'https://bitcoinmagazine.com/feed',
        ]

posts = list()
for url in raw_rss:
    feed = feedparser.parse(url)
    for post in feed.entries:
        posts.append(post.summary)

#       Cleaning Data

h = html2text.HTML2Text()
clean_text = lambda x: h.handle(x)
clean_br = lambda x: re.sub(r'\<br \/\>','',x)
clean_url = lambda x: re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','',x)
posts = [clean_text(item) for item in  posts]
posts = [item.lstrip() for item in posts]
posts = [clean_br(item) for item in posts]
posts = [clean_url(item) for item in posts]

#       Sentiment Analysis

sid = SentimentIntensityAnalyzer()
positive = negative = 0
for item in posts:
    print(item)
    ss = sid.polarity_scores(item)
    print(ss)
    if ss['pos'] > ss['neg']:
        positive = positive + 1
    if ss['neg'] > ss['pos']:
        negative = negative + 1
    
    
