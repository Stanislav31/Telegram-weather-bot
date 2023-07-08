BOT_API_TOKEN = "Your bot token here"
WEATHER_API_KEY = "Your OpenWeather API key"

CURRENT_WEATHER_API_CALL = (
        "https://api.openweathermap.org/data/2.5/weather?"
        "lat={latitude}&lon={longitude}&"
        "appid=" + WEATHER_API_KEY + "&units=metric"
)
