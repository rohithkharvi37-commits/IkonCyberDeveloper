import os
import random
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail, Message
from dotenv import load_dotenv

# Load secret variables from the .env file in the root directory
load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FRONTEND_DIR = os.path.abspath(os.path.join(BASE_DIR, '../Frontend'))

app = Flask(__name__, template_folder=FRONTEND_DIR)
app.secret_key = os.getenv("SECRET_KEY", "fallback_key")

# Configure Gmail SMTP using secure environment variables
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")

mail = Mail(app)

# Credentials check
USERNAME = "rohith"
PASSWORD = "12345"

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == USERNAME and password == PASSWORD:
            # Generate 6-digit OTP
            otp = str(random.randint(100000, 999999))
            session["otp"] = otp
            session["user"] = username
            
            try:
                recipient_email = os.getenv("MAIL_USERNAME") 
                msg = Message("Team Ikon - Your OTP Code", sender=os.getenv("MAIL_USERNAME"), recipients=[recipient_email])
                msg.body = f"Your login verification OTP code is: {otp}"
                mail.send(msg)
                return redirect(url_for("otp_page"))
            except Exception as e:
                return f"<h2 style='color:red; background:black; padding:20px;'>Email Error: {e} <a href='/login'>Try Again</a></h2>"
        else:
            return "<h2 style='color:red; background:black; padding:20px; font-family:Arial;'>Invalid Credentials! <a href='/login' style='color:#ffcc00;'>Try Again</a></h2>"
            
    return render_template("login.html")

@app.route("/otp", methods=["GET", "POST"])
@app.route("/otp.html", methods=["GET", "POST"])
def otp_page():
    if request.method == "POST":
        entered_otp = request.form.get("otp")
        if entered_otp == session.get("otp"):
            return redirect(url_for("success_page"))
        else:
            return "<h2 style='color:red; background:black; padding:20px; font-family:Arial;'>Invalid OTP! <a href='/otp'>Try Again</a></h2>"
    return render_template("otp.html")

@app.route("/success")
@app.route("/success.html")
def success_page():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)