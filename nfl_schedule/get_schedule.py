import requests
from bs4 import BeautifulSoup


r = requests.get('http://nfl.com/schedules')
r.raise_for_status
#dev class='list-matchup-row-center'

soup = BeautifulSoup(r.text, 'html.parser')

for tag in soup.find_all("div", class_="list-matchup-row-team"):
  print(tag,"\n")
