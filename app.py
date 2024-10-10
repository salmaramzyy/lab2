from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    fname = request.form.get('fname')
    lname = request.form.get('lname')  
    return render_template('result.html', fname=fname, lname=lname)

if __name__ == '__main__':  
    app.run(debug=True)
