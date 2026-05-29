from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>CS Internship Tools - Welcome Jack!</h1>"


@app.route("/calculator")
def calculator():
    return render_template("calculator.html")


@app.route("/hello-mother")
def hello_mother():
    return render_template("hello_mother.html")


if __name__ == "__main__":
    app.run(debug=True)
