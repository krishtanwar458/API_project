import requests

api_key = 'ab5768aedd8340c99cec0f3c5e3fc7c5'

# Make request to the News API
request = requests.get('https://newsapi.org/v2/everything?' \
'q=tesla&from=2025-05-30&' \
'sortBy=publishedAt&apiKey=ab5768aedd8340c99cec0f3c5e3fc7c5')

# Get a dictionary with data
content = request.json()

# Acess the article titles and description
for i in content['articles']:
    print(i['title'])
    print(i['description'])