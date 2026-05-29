from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>CS Internship Tools - Welcome Jack!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
