
import requests
import json

def request():

    api_key = {"api_key": "c714df39f180cce5586ae9609569bb08"}


    r = requests.get('https://api.themoviedb.org/3/trending/movie/day', params=api_key)

    resp = r.text

    dict = json.loads(resp)

    res = dict['results']


    titles = []
    rate = []
    description = []
    release_date = []

    for i in range(len(res)):

        raw = res[i]
        title = raw["title"]
        titles.append(title)
        vote_average = raw['vote_average']
        rate.append(vote_average)
        overview = raw['overview']
        description.append(overview)
        release = raw['release_date']
        release_date.append(release)
