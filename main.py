# https://gitlab.com/-/snippets/2039434
# https://myanimelist.net/forum/?topicid=1973077
# https://myanimelist.net/apiconfig/references/api/v2#operation/anime_season_year_season_get

import requests
from enum import Enum

CLIENT_ID = 'd12ba4518806e3a371c980a88035cf00'

class Season(Enum):
	winter = 1
	spring = 2
	summer = 3
	fall = 4

def get_anime_season_info(offset: int, year: int, season: Season) -> dict:
	header = { 'X-MAL-CLIENT-ID' : CLIENT_ID }
	response = requests.get(f'https://api.myanimelist.net/v2/anime/season/{year}/{season}?limit={offset}', headers = header)

	response.raise_for_status()
	animesInfo = response.json()
	response.close
	print(animesInfo)
	print('\n')
	for a in animesInfo['data']:
		print(a)
		print('\n')

get_anime_season_info(10, 2018, Season.spring.name)