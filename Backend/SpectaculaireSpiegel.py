from cachetools import TTLCache, cached
from flask import Flask, jsonify, abort
from flask_cors import CORS
import middleware.logicallayer as logic

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


class SpectaculaireSpiegel:
    global app

    CACHE_SIZE = 1
    NEWS_TTL = 900  # 15 minutes
    WEATHER_TTL = 3600  # 1 hour

    @staticmethod
    @app.route("/news", methods=['GET'])
    @cached(cache=TTLCache(maxsize=CACHE_SIZE, ttl=NEWS_TTL))
    def get_news():
        news = logic.get_news()
        if news is not None:
            return _corsify_actual_response(news)
        else:
            return abort(503, "Service Unavailable")

    @staticmethod
    @app.route("/weather", methods=['GET'])
    @cached(cache=TTLCache(maxsize=CACHE_SIZE, ttl=WEATHER_TTL))
    def get_weather():
        weather = logic.get_weather()
        if weather is not None:
            return _corsify_actual_response(weather)
        else:
            return abort(503, "Service Unavailable")

    @staticmethod
    @app.route("/location", methods=['GET'])
    @cached(cache={})
    def get_location():
        location = logic.get_location()
        if location is not None:
            return _corsify_actual_response(location)
        else:
            return abort(503, "Service Unavailable")

    @staticmethod
    @app.route("/calendar", methods=['GET'])
    def get_events():
        events = logic.get_events()
        if events is not None:
            return _corsify_actual_response(events)
        else:
            return abort(503, "Service Unavailable")


def _corsify_actual_response(response):
    response = jsonify(response)
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response
