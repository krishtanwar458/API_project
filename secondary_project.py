import streamlit as st
import requests

api_key = 'A3oFsNtWwMrnioHO7fsnf9BqUj8PeHHun8VqP3hW'

request = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}')
content = request.json()

image = requests.get('https://apod.nasa.gov/apod/image/2507/V462Lupi_Pon_960_annotated.jpg')

with open('nasa.jpg', 'wb') as file:
    file.write(image.content)

st.title(content['title'])
st.image('nasa.jpg', width=700)
st.text(content['explanation'])