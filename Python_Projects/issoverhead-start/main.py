import requests
from datetime import datetime
import pprint as pp
import math as m

# Pune IN
MY_LAT = 18.520430  # Your latitude
MY_LONG = 73.856743  # Your longitude

def iss_overahead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    # pp.pprint(data)
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    print(f"iss at {iss_latitude}\n My Lat Range {MY_LAT-5} \n To {MY_LAT+5}")
    return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG -5 <=iss_longitude <= MY_LONG +5)

def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # pp.pprint(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)
    sunrise = (sunrise + 5.5) % 24
    sunset = (sunset + 5.5) % 24

    time_now = datetime.now()

    print(f"sunrise time {sunrise}\n Sunset time {sunset}\nCurrent Time {time_now.hour}")
    return sunset <= time_now.hour or time_now.hour <=sunrise

if is_night() and iss_overahead():
    print("Send Mail")

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
