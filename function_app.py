import logging
import requests
import azure.functions as func
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Your OpenWeather API Key
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.function_name(name="WeatherFunction")
@app.route(route="weather")
def weather(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Weather function processed a request.")

    # Support both city or coordinates
    city = req.params.get("city")
    lat = req.params.get("lat")
    lon = req.params.get("lon")

    if city:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    elif lat and lon:
        url = f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    else:
        return func.HttpResponse(
            json.dumps({"error": True, "message": "Please provide ?city=London OR ?lat=..&lon=.."}),
            mimetype="application/json",
            status_code=400
        )

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return func.HttpResponse(
                json.dumps({"error": True, "message": data.get("message", "Something went wrong")}),
                mimetype="application/json",
                status_code=response.status_code
            )

        result = {
            "error": False,
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"]  # ✅ send icon code
        }

        return func.HttpResponse(
            body=json.dumps(result),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse(
            json.dumps({"error": True, "message": "Internal Server Error"}),
            mimetype="application/json",
            status_code=500
        )
