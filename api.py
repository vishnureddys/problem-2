# Importing the required modules
import requests, json
import datetime

# The URL to access the given JSON file
url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
response = requests.get(url)

# Data is parsed into a JSON and is available now. 
jsonRes = response.json()

# Accepting the date from the user
def getdate():
    print("Please enter the date and time in this format YYYY MM DD HH MM SS.")
    date_entry = input()
    year, month, day, hour, minute, second = map(int, date_entry.split())
    date = datetime.datetime(year,month, day, hour, minute, second)
    epoch = datetime.datetime.utcfromtimestamp(0)
    seconds_since_epoch = (date - epoch).total_seconds()
    return seconds_since_epoch

# Now performing the main task
while(True):
    flag = 0
    print("\n")
    print("1. Get Weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("Enter 0 to quit.")

    n = int(input())
    if n == 1:
        date = int(getdate())
        for i in jsonRes['list']:
            if i['dt'] == date:
                flag = 1
                print("The temperature is" , i['main']['temp'], "Kelvin")
                break
        if flag == 0:
            print("Sorry the temperature for this date and time is not known. ")
    elif n == 2:
        date = int(getdate())
        for i in jsonRes['list']:
            if i['dt'] == date:
                flag = 1
                print("The wind speed is" , i['wind']['speed'])
                break
        if flag == 0:
            print("Sorry the wind speed for this date and time is not known. ")
    elif n == 3:
        date = int(getdate())
        for i in jsonRes['list']:
            if i['dt'] == date:
                flag = 1
                print("The pressure is" , i['main']['pressure'])
                break
        if flag == 0:
            print("Sorry the pressure for this date and time is not known. ")
    elif n == 0:
        break
print("Thank you. Visit again. ")
