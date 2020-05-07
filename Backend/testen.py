from time import strftime, gmtime
from datetime import datetime

import requests
import basicfuctions as bf

if __name__ == '__main__':
    url = 'https://nominatim.openstreetmap.org/reverse?format=json&lat=52.680340&lon=5.026788'
    print('looking up')
    print(requests.get(url))
    print('gottem')


    print(datetime.now())
    print(datetime.now().utcoffset())
    print(strftime("%z", gmtime()))
    print(bf.get_system_time_offset())
