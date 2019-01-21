# site-blocker
Idea of program is to run continually in the background and periodically wake up to check whether the current time is in working hours.  If so, add a list of distracting sites to the hosts file (if not already there) to be blocked.  Otherwise, remove these sites from the hosts file (if they are present) so that they become reachable again.  
 
The intention is to remove distractions by blocking the user from being able to access a list of distracting sites during working hours.

NOTE: To run this for real (i.e. instead of with a test hosts file),
- Backup the hosts file
- Rename script from .py to .pyw so it runs in background
- Make sure hostsfile includes full path where hosts file is located:
   - Winows = C:\Windows\System32\drivers\etc\hosts
   - Linux  = /etc/hosts
- Run .pyw file with administrator priviledges so that it is able to modify the hosts file

Written for Udemy Course:
- The Python Mega Course: Build 10 Real World Applications
- Section 10: Application 3 - Build a Website Blocker
