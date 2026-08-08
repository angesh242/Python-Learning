#first open this link:https://newsapi.org/ 
# copy Get url from there copy it and paste it.
#for taking api click on link: https://newsapi.org/pricing as a Developer
#api key geeting: Your API key is: 290b12f4637a4f48be21a97c1bbcc42c
#Need to install from terminal: pip install requests

import requests
query="Artificial Intelligence"
api="290b12f4637a4f48be21a97c1bbcc42c"
url=f"https://newsapi.org/v2/everything?q={query}&from=2026-07-03&sortBy=publishedAt&apiKey={api}"
print(url)
response = requests.get(url)
#print(response.json())


data = response.json()
articles = data['articles']
#print(f"Total articles found: {len(articles)}")
for article in articles:
    print(article['title'], article['url'])
    print("\n-------------------------------------------------------\n")