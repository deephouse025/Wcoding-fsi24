from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>llo, World!</p>"

@app.route("/bubbles")
def whatever():
  return "<div style='width: 100px; height: 100px; border-radius: 50%; background-color: yellow;'></div>"
