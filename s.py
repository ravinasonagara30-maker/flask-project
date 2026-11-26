from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def hello():
    return render_template('style.html')
app.run(debug=True)