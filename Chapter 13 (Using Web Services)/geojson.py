import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceceurl = 'https://nominatim.openstreetmap.org/search?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter locarion: ')
    if len(address) < 1: break

    parms = dict()
    parms['q'] = address
    parms['format'] = 'geocodejson'

    print(parms)

    url = serviceceurl + urllib.parse.urlencode(parms)

    print(url)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    print(json.dumps(js, indent=4))

    lat = js['features'][0]['geometry']['coordinates'][1]
    lng = js['features'][0]['geometry']['coordinates'][0]

    print('lat: ', lat, ', lng: ', lng)

    location = js['features'][0]['properties']['geocoding']['label']

    print(location, '\n')