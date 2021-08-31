import datetime as dt
from time import sleep
import functions as func
from plyer import notification as ntf

def restart_host_file(filename, blocked_websites):
    print("\nFinished!\n")
    with open(filename, 'r+') as fo:
        lines = fo.readlines()
        fo.seek(0)

        for line in lines:
            if not any(website in line for website in blocked_websites):
                fo.write(line)
            
        fo.truncate()

    

def start_productive_time(redirect, filename, blocked_websites, deadline):
    # The main code to start working time
    try:
        while True:
            # To compare the current time and deadline
            if dt.datetime.now() < deadline:
                func.print_working()
                with open(filename, 'r+') as fo:
                    contents = fo.read()

                    for website in blocked_websites:
                        if website not in contents:
                            fo.write(redirect + ' ' + website + '\n')

                sleep(1)
        
            else:
                restart_host_file(filename, blocked_websites)
                break
        
    except KeyboardInterrupt:
        restart_host_file(filename, blocked_websites)

    finally:
        ntf.notify(title = 'Website Blocket', message = 'Time is up, Baby!', app_name = 'run_this', timeout = 5)
    
