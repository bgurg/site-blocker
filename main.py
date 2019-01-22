import time # for sleep method
from datetime import datetime as dt
from datetime import date as date # for isoweekday method

# hosts file information
hostsfiles = {'test' : 'hosts_test_file',
              'windows' : r'C:\Windows\System32\drivers\etc\hosts',
              'linux' : '/etc/hosts'}
hostsfile = hostsfiles['test']
redirect = '127.0.0.1'

# how long to sleep between checks
sleep_duration_in_seconds = 1

# list of sites to block during work hours
sitelist = ['www.facebook.com','facebook.com',
            'finance.yahoo.com','www.yahoo.com', 'yahoo.com',
            'news.google.com', 'finance.google.com']

# work hours (e.g. 8:30 to 16:30)
start_hr = 8
start_min = 30
end_hr = 16
end_min = 30

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
                print(f'.../{dt.now()}: In working hours - distracting sites blocked in "{hostsfile}"')
                contents = f.read()
                for site in sitelist:
                    if site not in contents:
                        f.write(f'{redirect}   {site}\n')                    
            else: 
                # remove lines containing sites in sitelist from hostfile
                print(f'.../{dt.now()}: Off work - surf all you want')
                contents = f.readlines()
                f.seek(0)
                for line in contents:
                    if not any(site in line for site in sitelist):
                        f.write(line)
                f.truncate()
    
        print(f'.../Going to sleep for {sleep_duration_in_seconds} seconds\n')
        time.sleep(sleep_duration_in_seconds)
