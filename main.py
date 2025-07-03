import requests
from send_email1_copy import send_email

api_key = 'ab5768aedd8340c99cec0f3c5e3fc7c5'

topic = 'tesla'
# Make request to the News API
request = requests.get('https://newsapi.org/v2/everything?' \
f'q={topic}&from=2025-06-03&' \
'sortBy=publishedAt&apiKey=ab5768aedd8340c99cec0f3c5e3fc7c5' \
'&language=en')

# Get a dictionary with data
content = request.json()

# Acess the article titles and send them in an email
email_body = "Subject: Today's News \n\n"
for index, i in enumerate(content['articles'][:20]):
    if i['title'] is not None:
        email_body += f" {index + 1}. {i['title']}\n {i['description']}\n \
        {i['url']} \n\n"

send_email(message=email_body)