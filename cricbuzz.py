from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.cricbuzz.com').text

soup = BeautifulSoup(source, 'lxml')

parent = soup.find('div', class_='cb-col cb-col-25 cb-mtch-blk')

# print(parent.prettify())
# Use tag.text to get text and tag.get_text() to get None if text d.n.e
# Use tag['attribute'] to get attribute and tag.get('attribute') to get None if attribute d.n.e

title = parent.find('a').get('title')
print(title)

batting = parent.find('a').find('div', class_='cb-hmscg-bat-txt cb-ovr-flo ')
bowling = parent.find('a').find('div', class_='cb-hmscg-bwl-txt ')

batting_team = batting.find_all('div')[0].get_text()
batting_score = batting.find_all('div')[1].get_text()

bowling_team = bowling.find_all('div')[0].get_text()
bowling_score = bowling.find_all('div')[1].get_text()

print(f'{batting_team}	{batting_score}')
print(f'{bowling_team}	{bowling_score}')

try:
    status = parent.find('div', class_=' cb-ovr-flo cb-text-live').text
    print("Match Live!\n" + status)
except:
    status = parent.find('div', class_=' cb-ovr-flo cb-text-complete').text
    print("Match Complete!\n" + status)
