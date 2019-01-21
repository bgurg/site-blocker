# Idea of program is to run continually in the background and periodically 
# wake up to check whether the current time is in working hours.  If so,
# add a list of distracting sites to the hosts file (if not already there) to
# be blocked.  Otherwise, remove these sites from the hosts file (if they are 
# present) so that they become reachable again.  
# 
# The intention is to remove distractions by blocking the user from being able
# to access a list of distracting sites during working hours.
#
# NOTE: To run this for real (i.e. instead of with a test hosts file),
#       1) Backup the hosts file
#       2) Rename script from .py to .pyw so it runs in background
#       3) Make sure hostsfile includes full path where hosts file is located:
#             - Winows = C:\Windows\System32\drivers\etc\hosts
#             - Linux  = /etc/hosts
#       4) Run .pyw file with administrator priviledges so that it is able
#          to modify the hosts file

import time # for sleep method
from datetime import datetime as dt
from datetime import date as date # for isoweekday method

# hosts file information
hostsfile = 'hosts_test_file'
redirect = '127.0.0.1'

# list of sites to block during work hours
sitelist = ['www.facebook.com','facebook.com','www.yahoo.com','yahoo.com']

# work hours (e.g. 8:30 to 16:30)
start_hr = 8
start_min = 30
end_hr = 16
end_min = 30

# how long to sleep between checks
sleep_duration_in_seconds = 1

def in_working_hours(now_dt):
    y, m, d = now_dt.year, now_dt.month, now_dt.day

    # if Sat-Sun, not in work hours
    if date(y, m, d).isoweekday() in [6,7]:
        return False

    # if Mon-Fri, return whether currently between 8:30am and 4:30pm
    else:
        return dt(y, m, d, 8, 30) <= now_dt <= dt(y, m, d, 16, 30)

if __name__ == "__main__":
    while True:
        with open(hostsfile, 'r+') as f:
            if in_working_hours(dt.now()):
                # add sites in sitelist to end of hostfile if not already there
                print(f'.../{dt.now()}: In working hours.  Distracting sites blocked.')
                contents = f.read()
                for site in sitelist:
                    if site not in contents:
                        f.write(f'{redirect}   {site}\n')                    
            else: 
                # remove lines containing sites in sitelist from hostfile
                print(f'.../{dt.now()}: Off work.  Surf all you want.')
                contents = f.readlines()
                f.seek(0)
                for line in contents:
                    if not any(site in line for site in sitelist):
                        f.write(line)
                f.truncate()
    
        print(f'.../Going to sleep for {sleep_duration_in_seconds} seconds\n')
        time.sleep(sleep_duration_in_seconds)
