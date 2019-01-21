# site-blocker
- Idea of program is to run continually in the background and periodically wake up to check whether the current time is in working hours.  If so, add a list of distracting sites to the hosts file (if not already there) to be blocked.  Otherwise, remove these sites from the hosts file (if they are present) so that they become reachable again.  
 
- To run against actual host file, make sure hostsfile includes full path where hosts file is located:
    - Winows = C:\Windows\System32\drivers\etc\hosts
    - Linux  = /etc/hosts

- To run in background, change extension from .py to .pyw and run with pythonw
- To be able to modify real hosts file, run with administrator priviledges

- Written for Python Mega Course: Build 10 Real World Applications (Udemy)
  - Section 10 - App 3: Build a Website Blocker
