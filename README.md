# ntplib_cron
Running a Python script ntplib.py time update from cron

1) Requires elevated privileges in crontab for sudo
2) Requires ntplib
  - pip install ntplib
  - sudo pip install ntplib

Simply add correctsystemtime.py file to any directory and add a cron task to fetch:
# Edit crontab for user #
> crontab -e

# Run every 20 minutes (or whatever length you would like #
> */20 * * * * /usr/bin/python /home/pi/correctsystemtime.py >> /tmp/logclock1.log 2>&1

# On reboot (if you want) #
> @reboot sudo /usr/bin/python /home/pi/correctsystemtime.py >> /tmp/logclockstartup.log 2>&1
