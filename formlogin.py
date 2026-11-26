from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def hello():
    return render_template('form.html')
@app.route('/formlogin',methods=['GET'])
def login():
    uname=request.args.get('uname')
    password=request.args.get('pass')
    if uname=="ravu" and password=="123":
        return "welcome %s" % uname
    else:
        return "try again"
app.run(debug=True)


