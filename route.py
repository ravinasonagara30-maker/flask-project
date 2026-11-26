from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return "hello world"
@app.route('/<name>')
def helloname(name):
    return"hello," + name
app.run(debug=True)