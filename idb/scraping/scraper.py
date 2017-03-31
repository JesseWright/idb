import requests
import json

url = "https://www.rijksmuseum.nl/api/en/collection"

page = 1

while True:
    r = requests.get(url, {'key': 'KRvsD9GG', 'format': 'json', 'ps': 10, 'p': page})
    r.encoding = 'utf-8-sig'
    data = r.json()
   
    #reached end of pages
    if not data['artObjects']:
        break
        
    print("PAGE: " + str(page))

    for artObject in data["artObjects"]:
        a = requests.get(url + "/"  + artObject["objectNumber"], {'key': 'KRvsD9GG', 'format': 'json'})
        a.encoding = 'utf-8-sig'
        print(a.url)
        w = a.json()["artObject"]
        
        print("artist: " + w["principalMaker"])
        print("title: " + w["title"])
        print("medium: " + w["physicalMedium"])
        print("year: " + str(w["dating"]["year"]))
        print("style: " + "TODO")
        print("size: " + str(w["dimensions"]))
        print("colors: " + str(w["colors"]))
        if w["webImage"]:
            print("image: " + w["webImage"]["url"])
        print("content: " + str(w["classification"]["iconClassDescription"]))
        print("")
        
    page += 1
