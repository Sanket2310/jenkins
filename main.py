from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/send',methods=['POST', 'GET'])
# ‘/send’ URL is bound with index() function.

def index():
    m = ''
    if request.method == 'POST':
            # num1 is used to store first value
        num1 = request.form.get('num1')
            # num2 is used to store second value
        num2 = request.form.get('num2')
        m=float(num1)/float(num2)
    return render_template('index.html',message=m)

if __name__=='__main__':
 app.run(host='0.0.0.0')
