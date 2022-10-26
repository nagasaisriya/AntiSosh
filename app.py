
from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/regdoc')
def regdoc():
    return render_template('register_doc.html')

@app.route('/reguser')
def reguser():
    return render_template('register_user.html')

if __name__=="__main__":
    app.run(debug=True)
