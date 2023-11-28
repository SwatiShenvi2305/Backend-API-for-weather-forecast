from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
OPENWEATHERMAP_API_KEY = '26143a912d1167affb51540980be72f7'

# Endpoint to get weather forecast by city name
@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')

    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    try:
        # Make a request to OpenWeatherMap API
        response = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}'
        )

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            weather_data = response.json()
            # You can customize the data you want to return
            return jsonify({
                'city': weather_data['name'],
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
            })
        else:
            return jsonify({'error': 'Failed to retrieve weather data'}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
