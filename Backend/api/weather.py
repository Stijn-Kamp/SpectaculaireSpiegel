from api.api_reader import ApiReader


class Weather:
    """base class to communicate with weather source"""
    def get_weather(self):
        raise NotImplementedError

    class WeatherReport:
        def __init__(self, tempMin, tempMax, icon):
            self.tempMin = tempMin
            self.tempMax = tempMax
            self.icon = icon


class WeatherApi(Weather):
    """Reads the weather using api"""
    def __init__(self, apiKey, latitude=None, longitude=None):
        latitude = latitude if latitude else 0
        longitude = longitude if longitude else 0
        self.weatherApiReader = ApiReader("https://api.darksky.net/forecast/%s/%f,%f" % (apiKey, latitude, longitude),
                                          exclude="currently,minutely,hourly,alerts,flags",
                                          units='auto')
        Weather.__init__(self)

    def get_weather(self):
        weather = self.weatherApiReader.get()
        weeklyWeather = weather.get('daily').get('data') if weather else []
        if weeklyWeather is None:
            return None
        weekReport = []
        for day in weeklyWeather:
            icon = day.get('icon')
            tempMin = day.get('temperatureMin')
            tempMax = day.get('temperatureMax')
            dayReport = self.WeatherReport(icon=icon, tempMax=tempMax, tempMin=tempMin)
            weekReport.append(dayReport)
        return weekReport
