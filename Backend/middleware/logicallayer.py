from configuration.config import IniConfigReader
from api.calendars import CalendarApi
from api.location import LocationApi
from api.news import NewsApi
from api.weather import WeatherApi

config = IniConfigReader('configuration/config.ini')

latitude = config.get_float('latitude')
latitude = latitude if latitude else 0

longitude = config.get_float('longitude')
longitude = longitude if longitude else 0

weather = WeatherApi(config.get_var('weather_key'), latitude, longitude)
location = LocationApi(latitude, longitude)
news = NewsApi(config.get_var('news_key'), pageSize=50)
calendar = CalendarApi()


def get_news():
    global news
    newsArticles = news.get_articles()
    if newsArticles:
        newsArticles = list(map(lambda a: a.__dict__, newsArticles))
    return newsArticles


def get_weather():
    global weather
    weatherReport = weather.get_weather()
    if weatherReport is not None:
        weatherReport = list(map(lambda w: w.__dict__, weatherReport))
    return weatherReport


def get_location():
    global location
    loc = location.get_location()
    if loc is not None:
        loc = loc.__dict__
    return loc


def get_events():
    global calendar
    events = calendar.get_events()
    if events is not None:
        events = list(map(lambda e: e.__dict__, events))
    return events
