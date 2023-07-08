from urllib.request import urlopen
from dataclasses import dataclass
import json

@dataclass(slots = True, frozen = True)
class Coordinates:
    latitude: float
    longitude: float

    @staticmethod
    def get_coordinates():
        """Returns current coordinates using IP address"""
        data = Coordinates._get_ip_data()
        latitude = data["loc"].split(",")[0]
        longitude = data['loc'].split(',')[1]

        return Coordinates(latitude = latitude, longitude = longitude)

    @staticmethod
    def _get_ip_data() -> dict:
        url = "http://ipinfo.io/json"
        response = urlopen(url)
        return json.load(response)
