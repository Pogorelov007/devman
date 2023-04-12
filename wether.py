import requests

places = ('Лондон', 'svo', 'Череповец')
for place in places:
    url_template = f'https://wttr.in/{place}?{{}}&lang=ru'
    url = url_template.format('nTMqm')
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)

