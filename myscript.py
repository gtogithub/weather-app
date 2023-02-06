from myKey import API_key
import requests
import os
import datetime as dt


def clear():
    os.system('cls')


userChoice = "Y"

while userChoice.upper() == "Y":
    clear()
    print("***** CURRENT WEATHER APP *****\n")
    print("Find current weather for desiderable place. Enter you choice, preferably in English.")
    city = input("City name: ")

    url = "http://api.weatherstack.com/current"

    params = {
        "access_key": API_key,
        "query": city
    }

    try:
        content = requests.get(url, params=params).json()
        with open(r"c:\temp\weatherAPP_stats.txt", "a") as file:
            file.write("Request from weather APP was sent on {}\n".format(dt.datetime.now()))

        # pprint.pprint(content)

        temp = content['current']['temperature']
        prec = content['current']['precip']
        pres = content['current']['pressure']
        desc = content['current']['weather_descriptions']
        ccov = content['current']['cloudcover']
        hmdt = content['current']['humidity']
        wdir = content['current']['wind_dir']
        wspd = content['current']['wind_speed']

        country = content['location']['country']
        city = content['location']['name']
        ltime = content['location']['localtime']
        latd = content['location']['lat']
        long = content['location']['lon']

        result = """\n
Current ({}) weather in {} ({}):
description: {}
temperature: {} *C
pressure: {} hPa
clouds: {} %
precipitation: {} mm
humidity: {} %
wind: {} km/h ({})
""".format(ltime, city, country, desc[0], temp, pres, ccov, prec, hmdt, wspd, wdir)

        print(result)

    except:
        print("\nSomething went wrong")

    finally:
        userChoice = input("Would you like to check another city? Y/N: ")
