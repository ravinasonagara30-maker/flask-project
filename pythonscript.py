from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def registration():
    return render_template('register.html')
@app.route('/success',methods=['POST'])
def printdata():
    result = request.form
    return render_template('result.html',result=result)
app.run(debug=True)