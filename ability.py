import requests
import json
def ability(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
    response = requests.get(url)
    data = json.loads(response.text)
    abilities = []
    for i in range(len(data['abilities'])):
        s = data['abilities'][i]['ability']['name']
        abilities.append(str(s))
    return(abilities)
