import requests as rq

news_api = 'f74721da87c742d89c767d6c6f2b7976'
url = (f'https://newsapi.org/v2/everything?q=tesla&from=2023-07-17'
       f'&sortBy=publishedAt&apiKey={news_api}')

# Making the request
request = rq.get(url)

# Get the data in JSON format
content = request.json()
articles = content['articles']

# List article titles and descriptions
for article in articles:
    print(article['title'])
    print(article['description'])
