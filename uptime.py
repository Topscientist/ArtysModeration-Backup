from flask import Flask
from threading import Thread

bot_started = "false"

app = Flask('Artys Moderation Uptime')

@app.route('/')
def home():
    return "<h1>Hello There!</h1>"
    return "The uptime monitroring system is working!"

def run():
  app.run(host='0.0.0.0',port=8080)

def uptime_check():
    t = Thread(target=run)
    t.start()