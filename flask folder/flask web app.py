from flask import Flask

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return "This is the homepage of ofek's website"

# Greeting Route
@app.route("/greet/<name>")
def greet(name):
    if name!='about':
        return f"Hello, {name}!"
    return 'This is a sample website created by ofek'

if __name__ == "__main__":
    app.run(debug=True)
