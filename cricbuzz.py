from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.cricbuzz.com').text

soup = BeautifulSoup(source, 'lxml')

parent = soup.find('div', class_='cb-col cb-col-25 cb-mtch-blk')

# print(parent.prettify())

title = parent.a['title']
print(title)

batting = parent.a.find('div', class_='cb-hmscg-bat-txt cb-ovr-flo ')
bowling = parent.a.find('div', class_='cb-hmscg-bwl-txt ')

batting_team = batting.find('div', class_='cb-ovr-flo cb-hmscg-tm-nm').text
bowling_team = bowling.find('div', class_='cb-ovr-flo cb-hmscg-tm-nm').text

batting_score = batting.find('div', class_='cb-ovr-flo').text
bowling_score = bowling.find('div', class_='cb-ovr-flo').text

print(f'{batting_team}	{batting_score}')
print(f'{bowling_team}	{bowling_score}')

status = parent.find('div', class_=' cb-ovr-flo cb-text-live').text

print(status)
