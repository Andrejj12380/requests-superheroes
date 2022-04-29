# coding=utf-8
import requests


def intelligence(names):
    intelligence_dict = {}
    smartest = ''
    for name in names:
        search_name = f'https://superheroapi.com/api/2619421814940190/search/{name}'
        name_json = requests.get(search_name).json()
        intelligence_dict[name] = int(name_json['results'][0]['powerstats']['intelligence'])
    max_intelligence = max(intelligence_dict.values())
    for character_name, intellect in intelligence_dict.items():
        if intellect == max_intelligence:
            smartest = character_name
    return print(f'Самый умный - {smartest} с интеллектом {max_intelligence}')


intelligence(['Hulk', 'Thanos', 'Captain America'])

