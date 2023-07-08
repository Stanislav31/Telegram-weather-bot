from typing import Literal, TypeAlias
from urllib.request import urlopen
from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
import json

from coord import Coordinates
import config

Celsius: TypeAlias = float


class WindDirection(IntEnum):
    North = 0
    Northeast = 45
    East = 90
    Southeast = 135
    South = 180
    Southwest = 225
    West = 270
    Northwest = 315

@dataclass(slots = True, frozen = True)
class Weather:
    location: str
    temperature: Celsius
    temperature_feeling: Celsius
    description: str
    wind_speed: float
    wind_direction: str
    sunrise: datetime
    sunset: datetime
    humidity: float

def get_weather(coordinates = Coordinates) -> Weather:
    """Requests the weather in OpenWeather API and returns it"""
    openweather_response = _get_openweathe_response(
        longitude = coordinates.longitude, latitude = coordinates.latitude
    )

    weather = _parse_openweather_response(openweather_response)
    return weather

def _get_openweathe_response(latitude: float, longitude: float) -> str:
    url = config.CURRENT_WEATHER_API_CALL.format(latitude = latitude, longitude = longitude)
    return urlopen(url).read()

def _parse_openweather_response(openweather_response: str) -> Weather:
    openweather_dict = json.loads(openweather_response)
    return Weather(
    location = openweather_dict["name"],
    temperature = openweather_dict["main"]["temp"],
    temperature_feeling = openweather_dict["main"]["feels_like"],
    description = str(openweather_dict["weather"][0]["description"].capitalize()),
    sunrise = datetime.fromtimestamp(openweather_dict["sys"]["sunrise"]),
    sunset = datetime.fromtimestamp(openweather_dict["sys"]["sunset"]),
    wind_speed = openweather_dict["wind"]["speed"],
    wind_direction = _parse_wind_direction(openweather_dict),
    humidity = openweather_dict["main"]["humidity"]
    )

def _parse_wind_direction(openweather_dict: dict) -> str:
    degrees = openweather_dict["wind"]["deg"]
    degrees = round(degrees / 45) * 45
    if degrees == 360:
        degrees = 0

    return WindDirection(degrees).name
