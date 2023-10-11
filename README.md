# AI_Hackathon_IITB

# 🌡Temperature Alert Agent

Project designed to monitor temperature data and provide alerts or notifications when specific temperature thresholds are exceeded. This type of project is used in various industries, including healthcare, agriculture, manufacturing, and environmental monitoring

# **📁** File Directory Structure :
```markdown
my_project/
|-- static/
|   |-- styles.css
|
|-- templates/
|   |-- index.html
|
|-- agent.py
|
|-- app.py
|
|-- private_keys.json
|-- requirements.txt
|-- requirements.txt
|-- README.md
```
# **💾 Installation :**
Get started with uAgents by installing it for Python 3.8, 3.9, 3.10, or 3.11:
```markdown
pip install -r requirements.txt
```
1. **uagents** :
    - ```https://docs.fetch.ai/uAgents/```
    - ```from uagents import Agent, Context, Model```
    - **`uagents`** Library: This line of code imports the **`Agent`**, **`Context`**, and **`Model`** classes from the **`uagents`** library.
2. **Flask**:
    - Flask is a lightweight web framework for building web applications in Python.
    - Flask to create a web interface for your project, allowing users to interact with your temperature alert system through a browser.
3. **Requests**:
    - **`requests`** library is used for making HTTP requests in Python.
    - use it to communicate with external APIs, such as Weatherbit API for fetching weather data or other data sources relevant to your temperature monitoring.
4. **Time**:
    - **`time`** module is part of the Python standard library and allows you to work with time-related functions.
    - tasks like scheduling temperature checks, setting alert intervals, or timing data collection.

# ⛅🌨🌩Weatherbit API :

1. **Visit the Weatherbit Website**:
Go to the Weatherbit website at **https://www.weatherbit.io/**.
2. **Sign Up**:
Click on the "Sign Up" or "Get Started" button on the Weatherbit website to create an account.
3. **Generate API Key**:
After logging in, you can generate an API key. Look for an option like "API Key" or "Generate API Key" in your account dashboard.
4. **Get Your API Key**:
Once you've selected a plan and completed any necessary steps, you will be provided with an API key. This key is essential for making API requests to Weatherbit services.

    ```json
    {
    		"message": "Login successful!",
    		"api_key": "YOUR_API_KEY"
    }
    ```
    


# 🚩References :
https://github.com/fetchai/uAgents


https://www.weatherbit.io/


https://www.youtube.com/watch?v=_0QX0HD-VD0&list=PL09jEkqdEp94fSWTjyK7PgvHRtp795KuH


https://docs.fetch.ai/uAgents/
