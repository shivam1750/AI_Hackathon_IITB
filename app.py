
# Import necessary libraries
from flask import Flask, render_template, request, flash, jsonify
import requests
import time
import json
app = Flask(__name__)
app.secret_key = 'k2open'  # Change this to a secret key for production

# Weatherbit API key (replace with your own key)

api_key = '2297b08ba295456ba1088f3eb8d4c1f4'

# Initialize user settings
user_location = ''
user_min_temp = None
user_max_temp = None

# Function to fetch temperature
def fetch_temperature(location):
    endpoint = 'https://api.weatherbit.io/v2.0/current'
    params = {
        'key': api_key,
        'city': location,
        'units': 'M'  # Metric units (Celsius)
    }

    response = requests.get(endpoint, params=params)
    data = response.json()
    temperature = data['data'][0]['temp']
    return temperature

# def write_temperature_to_json(location, temperature):
#     data = {
#         'location': location,
#         'temperature': temperature,
#     }

#     with open('temperature_data.json', 'w') as json_file:
#         json.dump(data, json_file)

def append_temperature_to_json(location, temperature):
    try:
        with open('temperature_data.json', 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = []

    # Make sure existing_data is a list
    if not isinstance(existing_data, list):
        existing_data = []

    data = {
        'location': location,
        'temperature': temperature,
    }
    existing_data.append(data)

    with open('temperature_data.json', 'w') as json_file:
        json.dump(existing_data, json_file)


# Route to get temperature data
@app.route('/get_temperature', methods=['GET'])
def get_temperature():
    location = request.args.get('location')
    temperature = fetch_temperature(location)  # Call the fetch_temperature function with the 'location' parameter
    # print(jsonify())
    append_temperature_to_json(location, temperature)
    return jsonify({'temperature': temperature})

# Function to update settings in agent.py
def update_agent_settings(location, min_temp, max_temp):
    agent_url = 'http://127.0.0.1:5000/update_settings'  # URL of the agent.py endpoint
    data = {
        'location': location,
        'min_temp': min_temp,
        'max_temp': max_temp
    }
    
    try:
        response = requests.post(agent_url, json=data)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

        # Check if the response contains JSON data
        if response.headers.get('content-type') == 'application/json':
            return response.json()
        else:
            return {'message': 'Invalid response from the agent'}
    except requests.RequestException as e:
        # Handle any request-related errors, e.g., connection issues, invalid URLs
        print(f"Request Error: {e}")
        return {'message': 'Request error'}
    except Exception as e:
        # Handle other exceptions
        print(f"Error: {e}")
        return {'message': 'An error occurred'}

# ...


@app.route('/', methods=['GET', 'POST'])
def index():
    global user_location, user_min_temp, user_max_temp

    if request.method == 'POST':
        user_location = request.form['location']
        user_min_temp = float(request.form['min_temp'])
        user_max_temp = float(request.form['max_temp'])
        flash('Settings updated!', 'success')

        # Send user inputs to the uAgent
        update_agent_settings(user_location, user_min_temp, user_max_temp)

    return render_template('index.html', location=user_location, min_temp=user_min_temp, max_temp=user_max_temp)

if __name__ == '__main__':
    app.run(debug=True)