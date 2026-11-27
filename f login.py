from flask import *
app = Flask(__name__)
app.secret_key ="abc"
@app.route('/')
def sss():
    return render_template('f.html')
@app.route('/flogin',methods=['GET'])
def login():
    error =None
    uname=request.args.get('uname')
    password=request.args.get('pass')
    if uname=="ravu" and password=="123":
        flash("you are successfully logged in")
        return render_template('mss.html',name=uname)
    else:
        error="invalid username and password"
        return render_template('f.html',error=error)
app.run(debug=True)