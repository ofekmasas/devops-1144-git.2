from flask import Flask,send_file
import requests

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return "This is the homepage of ofek's website"

@app.route("/")
def home():
    # Fetch data from an API
    api_url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(api_url)
    data = response.json()

    # Extract weather info
    weather = data.get("weather", "No data available")
    temperature = data.get("temperature", "Unknown")

    # Return the response (simple example)
    return f"The weather in London is {weather}, with a temperature of {temperature}°C."

# Greeting Route
@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route("/about")
def about():
    return 'This is a sample website created by ofek'

if __name__ == "__main__":
    app.run(debug=True)
