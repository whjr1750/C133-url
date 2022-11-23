from flask import Flask
app=Flask(__name__)
#app is an object of class flask
@app.route("/")
def firstFlask():
    return "We are learning flask"
app.run()