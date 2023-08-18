import os

import requests as rq
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()

news_api = os.getenv('APP5_NEWS_API_KEY')
news_topic = 'tesla'
url = (f'https://newsapi.org/v2/everything?q={news_topic}&language=en'
       f'&sortBy=publishedAt&apiKey={news_api}')

# Making the request
request = rq.get(url)

# Get the data in JSON format
content = request.json()
articles = content['articles']

# List article titles and descriptions
body = f'Subject: Today\'s news about {news_topic}\n'
for article in articles[:21]:
    if article['title'] is not None:
        body = (body
                + article['title'] + '\n'
                + article['description'] + '\n'
                + article['url'] + '\n\n')

body = body.encode('utf-8')
send_email(message=body)
