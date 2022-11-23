from flask import Flask,render_template
app=Flask(__name__)
#app is an object of class flask
@app.route("/index")
def firstFlask():
    name='Angel'
    return render_template('index.html', index =name)

app.run(debug=True)