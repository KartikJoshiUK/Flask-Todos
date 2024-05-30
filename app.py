# Imports
from flask import Flask
from dotenv import load_dotenv

#  Initialization
load_dotenv()
app = Flask(__name__)


# Routes
@app.route("/")
def index():
    return "Hello World!!"

# Server
if __name__ == "__main__":
    app.run(debug=True)