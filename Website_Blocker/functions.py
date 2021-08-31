import os
import json
from time import sleep
import ctypes

def isAdmin():
    return ctypes.windll.shell32.IsUserAnAdmin()

    
def MENU(websites_file, blocked_websites):
    menu = """1 --> Set timer for productive working
2 --> See the list of websites you prohibited
3 --> Change your websites list
q --> Finish the program
"""

    # IndexError
    # KeyboardError
    # ValueError
    while True:
        print(menu)
        answer = input('>>> ').strip()
            
        while answer not in {'1', '2', '3', 'q'}:
            answer = input("Input 1/2/3/q again >>> ").strip()

        if answer == '1':
            # If True is returned, while loop get start in 'run_this'
            condition = True
            return blocked_websites, condition
        
        elif answer == '2':
            print(blocked_websites)

        elif answer == '3':
            blocked_websites = create_websites_list(websites_file)

        else:
            # If False is returned, while loop doesn't get start in 'run_this'
            condition = False
            return blocked_websites, condition
        
        print()


# Printing message during time span the user defined 
def print_working():
    for symbol in 'Working...':
        print(symbol, end = '')
        sleep(0.4)
    print()
    
# Check if file exists in the directory
def check_file_exists(websites_file):
    return os.path.exists(websites_file)

# Create a new blocked website list
def create_websites_list(websites_file):
    print("Write down the website names with spaces between them like github.com youtube.com ")
    blocked_websites = input(">>> ").split()
    blocked_websites = extend_websites_list(blocked_websites)
    
    with open(websites_file, 'w') as fo:
        json.dump(blocked_websites, fo, indent = 6)

    return blocked_websites

# To get the ready-made blocket website list
def get_websites(websites_file):
    with open(websites_file) as fo:
        blocked_websites = json.load(fo)

    return blocked_websites

############ Calculations ############
def calculate_hour(listed_time, hour, input_hour):
    _index = listed_time.index(input_hour)
    hour += float(listed_time[_index - 1])
    return hour

def calculate_minute(listed_time, minute, input_minute):
    _index = listed_time.index(input_minute)
    minute += float(listed_time[_index - 1])
    return minute
######################################

def get_time():
    time = input('How much time you need to work? (Go back --> q) >>> ').strip()
    
    if time == 'q':
        return False

    # If there is no input or the user types down only spaces, we recall input() to ask the user for time
    while not time.split():
        time = input('How much time you need to work? (Go back --> q) >>> ').strip()
        if time == 'q':
            return False

    return time

# A function to make 'working time' input clear for Python interpreter
def get_minute():

    while True:
        try:
            # Asking how much time the user need to work
            time = get_time()

            # If time is False, it is restarted
            if not time:
                break
            
            listed_time = time.split()

            hour = 0
            minute = 0

            if 'hour' in listed_time:
                hour = calculate_hour(listed_time, hour, 'hour')
                
            # When the user inputs both 'hour' and 'hours', one of them should be ignored. That's why elif statement is essential in this case.
            elif 'hours' in listed_time:
                hour = calculate_hour(listed_time, hour, 'hours')
                
            if 'minute' in listed_time:
                minute = calculate_minute(listed_time, minute, 'minute')
                
            # When the user inputs both 'minute' and 'minutes', one of them should ignored. That's why elif statement is essential in this case.
            elif 'minutes' in listed_time:
                minute = calculate_minute(listed_time, minute, 'minutes')
                
            else:
                minute = float(listed_time[0])

            return hour * 60 + minute

        except ValueError:
            print("\nYour input is inaccurate. Try again.")
        
# Adding 'http', 'https', and 'www', to each website in a list
def extend_websites_list(blocked_websites):
    # Copying websites list
    additional_websites_list = blocked_websites.copy()
    
    for website in blocked_websites:
        if 'www' not in website:
            additional_websites_list.append('www.' + website)

        if 'http' not in website:
            if 'www' not in website:
                additional_websites_list.append('http://www.' + website)
                additional_websites_list.append('http://' + website)

        if 'https' not in website:
            if 'www' not in website:
                additional_websites_list.append('https://www.' + website)
                additional_websites_list.append('https://' + website)
    
    return additional_websites_list

