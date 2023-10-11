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

# Function to send notifications
async def send_notification(ctx, location, temperature, min_temp, max_temp):
    if min_temp <= temperature <= max_temp:
        message = f"Temperature in {location} is {temperature}°C (Normal)"
    else:
        message = f"Temperature in {location} is {temperature}°C (Alert)"
    
    await ctx.send(agent.address, TemperatureMessage(location=location, temperature=temperature))
    ctx.logger.info(message)

# Route to update user settings
@uagent_app.route('/update_settings', methods=['POST'])
def update_settings():
    global user_location, user_min_temp, user_max_temp

    data = request.json
    user_location = data['location']
    user_min_temp = data['min_temp']
    user_max_temp = data['max_temp']

    return jsonify({'message': 'Settings updated successfully'})

# Function to periodically fetch temperature and send notifications
@agent.on_interval(period=1.0)  # Fetch temperature every 1 minute
async def check_temperature(ctx: Context):
    location = user_location  # Use the global user_location
    min_temp = user_min_temp  # Use the global user_min_temp
    max_temp = user_max_temp  # Use the global user_max_temp
    
    temperature = fetch_temperature(location)
    await send_notification(ctx, location, temperature, min_temp, max_temp)

if __name__ == "__main__":
    uagent_app.run(host='127.0.0.1', port=5000)    