from flask import Flask
app=Flask(__name__)

@app.route("/<var>")
def va(var):
    return var

@app.route("/asdf")
def va1(var):
    return var

@app.route("/")
def index(var):
    return "index"

if __name__=='__main__':
    app.debug=True
    app.run()