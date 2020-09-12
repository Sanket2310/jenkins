"""This module returns a welcome page of my blog site"""
from flask import Flask, render_template, request
app = Flask(__name__)

"""The route() function of the Flask class is a decorator,
which tells the application which URL should call the associated function. """
@app.route('/',methods=['post', 'get'])
# ‘/’ URL is bound with index() function.
def index():
    """renders html file which accepts two numbers,operation as input and returns result."""
    message = ''
    if request.method == 'POST':
        number_1 = request.form.get('n1')
        number_2 = request.form.get('n2')
        operation = request.form.get('op')
        if operation=="+":
            message=int(number_1)+int(number_2)
        elif operation=="-":
            message=int(number_1)-int(number_2)
        elif operation=="*":
            message=int(number_1)*int(number_2)
        elif operation=="/" and int(number_2)!=0:
            message=int(number_1)/int(number_2)
        else:
            message="Invalid Operation"
    return render_template('index.html',message=message)
@app.route('/aboutme')
def aboutme():
    """renders aboutme page as output"""
    return "<h1>Yash Jaiswal<br/>Platform Engineer<br>Qid:21031<br>Quantiphi</h1>"

if __name__=='__main__':
    app.run(host='0.0.0.0')
