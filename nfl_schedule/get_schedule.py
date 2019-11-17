import requests
from bs4 import BeautifulSoup


r = requests.get('http://nfl.com/schedules')
r.raise_for_status

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
