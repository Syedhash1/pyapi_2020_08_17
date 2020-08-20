#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


# Let's give it a default route
@app.route("/")
def default():
    return "You are at the default route"

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"
    #return "Hello {}".format(name)
    ## V2 STYLE STRING FORMATTER - return "Hello {}".format(name)
    ## OLD STYLE STRING FORMATTER - return "Hello %s!" % name

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

