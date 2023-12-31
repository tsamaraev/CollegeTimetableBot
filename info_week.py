from http import HTTPStatus

from bs4 import BeautifulSoup
import requests

url = "https://timetable.gstou.ru/"
response = requests.get(url)

week_info = []

if response.status_code == HTTPStatus.OK:
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    ul = soup.find("ul", class_="infoForUser")
    for li in ul:
        if li.text.strip():
            week_info.append(li.text)



