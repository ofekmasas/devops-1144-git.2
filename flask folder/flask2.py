import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    # Fetch a random dog image from Dog CEO API
    api_url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(api_url)
    data = response.json()

    # Get the URL of the random dog image
    dog_image_url = data["message"]

    # Print the whole data dictionary
    print("Full data received from the API:", data)

    # Print just the message (dog image URL)
    print("Dog image URL:", data["message"])

    # Return an HTML page that displays the dog image
    return f"""
    <h1>Random Dog Image</h1>
    <p>Here is a random dog image for you:</p>
    <p>i added another line</p>
    <img src="{dog_image_url}" alt="Random Dog" width="500">
    """

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=8080)