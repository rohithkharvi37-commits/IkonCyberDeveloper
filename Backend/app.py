import os
from flask import Flask, render_template, request, redirect, url_for

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FRONTEND_DIR = os.path.abspath(os.path.join(BASE_DIR, '../Frontend'))
STATIC_DIR = os.path.join(FRONTEND_DIR, 'static')

app = Flask(__name__, template_folder=FRONTEND_DIR, static_folder=STATIC_DIR)

@app.route('/')
def home():
    return redirect(url_for('login_page'))

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        
        if username == "admin" and password == "12345":
            return redirect(url_for('success_page'))
        else:
            return "<h2 style='color:red; background:black; padding:20px;'>Invalid Login! <a href='/login'>Try Again</a></h2>"
    
    return render_template('login.html')

@app.route('/success')
def success_page():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)