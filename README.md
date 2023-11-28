# Backend-API-for-weather-forecast
-This is a simple  backend API that retrieves weather forecast information based on user input location.
-This is a simple Flask-based API for retrieving weather forecast data based on a specific location using the OpenWeatherMap 
 API.
-Install prerequisites:
  pip install Flask requests 
  
PROCEDURE:

Obtain an API key from OpenWeatherMap and replace 'YOUR_API_KEY' with your actual API key.
Run the Flask application.
The API will be accessible at http://127.0.0.1:5000/.

USAGE:

Get weather information by typing the required city name.
Endpoint: /weather
Query Parameter:
city : the name of the city for which you want to retrieve the weather
forecast.

Example Request:
http://127.0.0.1:5000/weather?city=London

Example Response:
{
"city": "London",
"temperature": 280.32,
"description": "light intensity drizzle"
}

ERROR HANDLING:

1. If the city parameter is not provided, the API will return a 400 Bad Request
with an error message.
2. If there is an issue with the weather data retrieval, the API will return an
error message along with the appropriate status code.

DEPENDENCIES:

1.Flask
2.Requests

NOTES:

Make sure to keep your OpenWeatherMap API key secure and do not expose it publicly.
Customize the data returned in the response according to your requirements.

LICENCE:

Feel free to customize the README further based on additional information
you want to provide or specific details about your API.



