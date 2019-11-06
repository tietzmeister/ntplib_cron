#!/usr/bin/python

import time
import os
import sys

# Append a system path to module for ntplib #
sys.path.append("/usr/local/lib/python2.7/dist-packages/")

try:
  import ntplib
  client = ntplib.NTPClient()
  response = client.request('pool.ntp.org')
  response = time.strftime('%m%d%H%M%Y',time.localtime(response.tx_time))
  print response
  newtime = os.system('sudo date ' + response)
  print newtime
 except:
  print('Could not update time')
