import datetime as dt
import functions as func
from main import start_productive_time as spt

# File names and host name
redirect = '127.0.0.1'
filename = 'C:\Windows\System32\drivers\etc\hosts' # host_path
websites_file = 'blocked_websites.json'


# Checking administrator rights
if func.isAdmin():

    # Checking if file exists
    if func.check_file_exists(websites_file):
        blocked_websites = func.get_websites(websites_file)
        
    else:
        # Creating a list of blocket websites
        blocked_websites = func.create_websites_list(websites_file)

    while True:
        # MENU
        blocked_websites, condition = func.MENU(websites_file, blocked_websites)

        # When 'q' is input, the loop is broken
        if not condition:
            break

        # 
        minutes = func.get_minute()
        
        # If minutes is False, we restart
        if not minutes:
            continue
        
        tdelta = dt.timedelta(minutes = minutes)
        deadline = tdelta + dt.datetime.now()

        spt(redirect, filename, blocked_websites, deadline)
    print('Good bye, Baby!')

else:
    print("You don't have administrator rights. Reopen Python Idle as an administrator.")
    


"""

# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost

"""
