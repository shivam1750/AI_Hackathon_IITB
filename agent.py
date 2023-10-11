# Import necessary modules
from uagents import Agent, Context, Model
import requests
from flask import Flask, request, jsonify

# Define a message model
class TemperatureMessage(Model):
    location: str
    temperature: float

# Create the agent
agent = Agent(name="temperature_alert_agent")
uagent_app = Flask(__name__)
# Weatherbit API key (replace with your own key)
api_key = 'Your-weatherbit api key'

# Function to fetch temperature
def fetch_temperature(location):
    endpoint = 'https://api.weatherbit.io/v2.0/current'
    params = {
        'key': api_key,
        'city': location,
        'units': 'M'  # Metric units (Celsius)
    }
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

        data = response.json()
        print(data)
        temperature = data['data'][0]['temp']
        return temperature
    except requests.RequestException as e:
        # Handle any request-related errors, e.g., connection issues, invalid URLs
        print(f"Request Error: {e}")
        return None
    except (KeyError, IndexError, ValueError) as e:
        # Handle JSON parsing errors or missing data in the API response
        print(f"JSON Parsing Error: {e}")
        return None