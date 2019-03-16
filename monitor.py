# monitor.py
# Monitor buses movement in real time.
#

import time
import urllib
from xml.etree.ElementTree import parse

candidates = ['1770', '1861', '1864', '1921']
office_lat = 41.980262

def distance(lat1, lat2):
    'Return distance between two lats'
    return 69*abs(lat1-lat2)

def monitor ():
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    doc = parse(u)
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if busid in candidates:
            lat = float(bus.findtext('lat'))
            dis = distance(lat, office_lat)
            print (busid, dis, 'miles')
    print ('-'*10)
    
abort_after = 60
start = time.time()

while True:
    monitor()
    time.sleep(5)
    delta = time.time() - start
    if delta >= abort_after:
        break

