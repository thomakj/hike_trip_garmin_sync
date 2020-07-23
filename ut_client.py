import requests
import json


def get_trip_gpx(id):
    url_trip_gpx = 'https://ut.no/api/trip/{}/gpx'.format(id)
    r = requests.get(url_trip_gpx)
    with open('trip.gpx', 'wb') as f:
        f.write(r.content)


