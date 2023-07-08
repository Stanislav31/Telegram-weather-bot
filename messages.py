from coord import Coordinates
from api_service import get_weather

def weather() -> str:
    """Returns a message about the temperature and weather description"""
    wthr = get_weather(Coordinates.get_coordinates())
    return f"{wthr.location}, {wthr.description}\nTemperature is {wthr.temperature}°C, feels like {wthr.temperature_feeling}°C\nHumidity: {wthr.humidity}%"

def wind() -> str:
    """Returns a message about wind direction and speed"""
    wthr = get_weather(Coordinates.get_coordinates())
    return f"{wthr.wind_direction} wind {wthr.wind_speed} m/s"

def sun_time() -> str:
    """Returns a message about the time of sunrise and sunset"""
    wthr = get_weather(Coordinates.get_coordinates())
    return f'Sunrise: {wthr.sunrise.strftime("%H:%M")}\n' \
           f'Sunset: {wthr.sunset.strftime("%H:%M")}\n'
