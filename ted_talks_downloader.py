import requests #getting content of the TED Talk page

from bs4 import BeautifulSoup #web scraping

import re #Regular Expression pattern matching

import json #json processing
url = 'https://www.ted.com/talks/malcolm_gladwell_choice_happiness_and_spaghetti_sauce/'
r = requests.get(url)

print("Download about to start")
r.content
r.status_code
soup = BeautifulSoup(r.content, "html.parser")
next_data_script = soup.find(id="__NEXT_DATA__")
next_data_script
data_json = next_data_script.string
data_json
player_data = json.loads(data_json)['props']['pageProps']['videoData']['playerData']
player_data
url_content = json.loads(player_data)['resources']['h264'][0]['file']
#url_content[0]['file']
#mp4_url = json.loads(player_data)['resources']['h264'][0]['file']
url_content
mp4_response = requests.get(url_content)
mp4_response.status_code
file_name = 'ted_talk_video.mp4'
with open(file_name,'wb') as f:
  f.write(mp4_response.content)