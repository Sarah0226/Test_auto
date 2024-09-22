# -*- coding: utf-8 -*-
import requests
import json
import Logger
from datetime import datetime, timedelta
from hamcrest import assert_that, equal_to

'''
The information from Task 1 (9-day forecast) is from Hong Kong Observatory API, please:
1. Capture the related API endpoint
2. Send a request using this API endpoint with your preferred language
3. Test the request response status is whether successful or not
4. Extract the relative humidity (e,g, 60 - 85%) for the day after tomorrow from the API
response (e.g. if today is Monday, then extract the relative humidity for Wednesday)

'''

def task_2():

    # Get current datetime
    current_datetime = datetime.now()

    # Send api request
    api_url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en"
    response = requests.get(api_url)

    # Check response status code is 200
    assert_that(
        response.status_code, equal_to(200), "Api response fail!"
    )

    # Transfer response to json
    json_data = json.loads(response.text)

    # Get date of day after tomorrow
    day_after_tomorrow = current_datetime + timedelta(days=2)
    day_after_tomorrow_string = day_after_tomorrow.strftime("%Y%m%d")

    # Get the relative humidity
    for weather_data in json_data["weatherForecast"]:
        if weather_data["forecastDate"] == day_after_tomorrow_string:
            Logger.logging.info(weather_data["forecastMaxrh"])
            Logger.logging.info(weather_data["forecastMinrh"])
            assert weather_data["forecastMaxrh"] != None
            assert weather_data["forecastMinrh"] != None


if __name__ == "__main__":
    task_2()
