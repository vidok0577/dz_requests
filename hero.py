import requests

def compare_heroes(compare_heroes):
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    all_heroes = requests.get(url).json()
    find_hero = list(filter(lambda x: x['name'] in compare_heroes, all_heroes))
    max_intell = all_heroes[0]
    for hero in find_hero:
        max_intell = hero if hero['powerstats']['intelligence'] > max_intell['powerstats']['intelligence'] else max_intell
    return f"Победил {max_intell['name']}, его интеллект равен {max_intell['powerstats']['intelligence']}"

if __name__ == '__main__':
    print(compare_heroes(['Hulk', 'Captain America', 'Thanos']))
