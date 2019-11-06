#!/usr/bin/python

import time
import os
import sys

sys.path.append("/usr/local/lib/python2.7/dist-packages/")

#try:
import ntplib
client = ntplib.NTPClient()
response = client.request('lovebug.pasco.k12.fl.us')
response = time.strftime('%m%d%H%M%Y',time.localtime(response.tx_time))
print response
newtime = os.system('sudo date ' + response)
print newtime
#except:
#    print('Could not sync with time server.')

print('Done.')
