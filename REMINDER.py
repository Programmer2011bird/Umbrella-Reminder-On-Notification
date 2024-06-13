#-----------------------------#
#          6/11/2024          #
#-----------------------------#
import sys
from plyer import notification
import schedule
from bs4 import BeautifulSoup
import requests

def get_weather(city: str) -> str:
    try:
        # Configs
        city: str = city.lower()
        url: str = "https://www.google.com/search?q=" + "weather" + city
        # Browsing through the url
        Content: bytes = requests.get(url).content
        
        SOUP: BeautifulSoup = BeautifulSoup(Content, "html.parser")
        # Finding the div containing the weather info
        weather: str = SOUP.find( 
            'div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text 

        # Formatting the data
        weather: str = weather.split("\n")[1]
    
    # Handeling the errors for not founding the city 
    except IndexError:
        return "City Not Found Please Enter Another City"

    except AttributeError:
        return "City Not Found Please Enter Another City"

    # Handeling the errors for network connection
    except requests.exceptions.ConnectionError:
        return "Connection Lost, Try Reconnecting"
    
    else:
        return weather


# Sending system notification
def Send_Notification() -> None:
    notification.notify(
        title = f"Pick an Umberlla !",
        message= f"The weather is Rainy Please Pick an Umberlla" ,
        
        # displaying time
        timeout=None)

# Scheduling the system notification
def Schedule_Notification(time: str, city: str) -> None:
    WEATHER = get_weather(city)
    
    if WEATHER == "Rainy" or WEATHER == "Showers" or WEATHER == "Rain and Snow" or WEATHER == "Haze" or WEATHER == "Cloudy":
        schedule.every().day.at(time).do(Send_Notification)
        WEATHER = get_weather(city)  

    while True:
        schedule.run_pending()
        WEATHER = get_weather(city)
