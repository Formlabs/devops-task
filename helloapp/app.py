import ast
import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

DEBUG = ast.literal_eval(os.getenv("APP_DEBUG", "False"))


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=DEBUG)
