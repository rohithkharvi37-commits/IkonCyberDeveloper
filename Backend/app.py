import os
import random
import time
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FRONTEND_DIR = os.path.abspath(os.path.join(BASE_DIR, '../Frontend'))

app = Flask(__name__, template_folder=FRONTEND_DIR)
app.secret_key = os.getenv("SECRET_KEY", "fallback_key")

# Configure Gmail SMTP
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")

mail = Mail(app)

# Credentials
USERNAME = "admin"
PASSWORD = "12345"

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if "failed_attempts" not in session:
        session["failed_attempts"] = 0
    if "lockout_time" not in session:
        session["lockout_time"] = 0

 
    current_time = time.time()
    lockout_duration = 15
    if current_time - session["lockout_time"] < lockout_duration:
        remaining = int(lockout_duration - (current_time - session["lockout_time"]))
        return f"<h2 style='color:#ffcc00; background:black; padding:20px; font-family:Arial;'>⚠️ Too many failed login attempts! Locked out. Please try again in {remaining} seconds. <a href='/login' style='color:#fff;'>Refresh</a></h2>"

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == USERNAME and password == PASSWORD:
            session["failed_attempts"] = 0
            session["lockout_time"] = 0
            
            # Reset OTP tracking when a fresh login succeeds
            session["otp_failed_attempts"] = 0
            session["otp_lockout_time"] = 0
            
            # --- UNUSUAL LOGIN TIME CHECK ---
            current_hour = datetime.now().hour
            # Define unusual hours as late night (Between 10 PM / 22:00 and 6 AM / 06:00)
            is_unusual_time = (current_hour >= 22 or current_hour < 6)
            
            if is_unusual_time:
                try:
                    recipient_email = os.getenv("MAIL_USERNAME")
                    timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    unusual_msg = Message("🚨 Security Alert: Unusual Login Time Detected", sender=os.getenv("MAIL_USERNAME"), recipients=[recipient_email])
                    unusual_msg.body = f"SECURITY WARNING:\n\nA successful password entry was recorded at an unusual hour: {timestamp_str}.\nIf this was not you, please secure your account immediately."
                    mail.send(unusual_msg)
                except Exception as mail_error:
                    print(f"Unusual time alert email failed: {mail_error}")

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
            session["failed_attempts"] += 1
            attempts_left = 3 - session["failed_attempts"]
            
            if session["failed_attempts"] >= 3:
                session["lockout_time"] = time.time()
                
                # Send Security Alert Email for Login Breach
                try:
                    recipient_email = os.getenv("MAIL_USERNAME")
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    alert_msg = Message("🚨 Security Alert: Multiple Failed Login Attempts", sender=os.getenv("MAIL_USERNAME"), recipients=[recipient_email])
                    alert_msg.body = f"SECURITY WARNING:\n\nYour login system detected 3 consecutive failed password attempts at {timestamp}.\nThe system has been locked out for 15 seconds."
                    mail.send(alert_msg)
                except Exception as mail_error:
                    print(f"Alert email failed: {mail_error}")

                return "<h2 style='color:red; background:black; padding:20px; font-family:Arial;'>❌ 3 failed login attempts! Security alert email sent. You are locked out for 15 seconds. <a href='/login' style='color:#ffcc00;'>Try Again</a></h2>"
            
            return f"<h2 style='color:red; background:black; padding:20px; font-family:Arial;'>❌ Invalid Credentials! Attempts left: {attempts_left}. <a href='/login' style='color:#ffcc00;'>Try Again</a></h2>"
            
    return render_template("login.html")

@app.route("/otp", methods=["GET", "POST"])
@app.route("/otp.html", methods=["GET", "POST"])
def otp_page():
    if "user" not in session:
        return redirect(url_for("login"))

    if "otp_failed_attempts" not in session:
        session["otp_failed_attempts"] = 0
    if "otp_lockout_time" not in session:
        session["otp_lockout_time"] = 0

    # 15-second lockout check for OTP
    current_time = time.time()
    lockout_duration = 15
    if current_time - session["otp_lockout_time"] < lockout_duration:
        remaining = int(lockout_duration - (current_time - session["otp_lockout_time"]))
        return f"<h2 style='color:#ffcc00; background:black; padding:20px; font-family:Arial;'>⚠️ Too many failed OTP attempts! Locked out. Please try again in {remaining} seconds. <a href='/otp' style='color:#fff;'>Refresh</a></h2>"

    if request.method == "POST":
        entered_otp = request.form.get("otp")
        if entered_otp == session.get("otp"):
            session["otp_failed_attempts"] = 0
            session["otp_lockout_time"] = 0
            return redirect(url_for("success_page"))
        else:
            session["otp_failed_attempts"] += 1
            attempts_left = 3 - session["otp_failed_attempts"]

            if session["otp_failed_attempts"] >= 3:
                session["otp_lockout_time"] = time.time()
                
                # Send Security Alert Email for OTP Breach
                try:
                    recipient_email = os.getenv("MAIL_USERNAME")
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    alert_msg = Message("🚨 Security Alert: Multiple Failed OTP Attempts", sender=os.getenv("MAIL_USERNAME"), recipients=[recipient_email])
                    alert_msg.body = f"SECURITY WARNING:\n\nYour system detected 3 consecutive failed OTP verification attempts at {timestamp}.\nThe session has been locked out for 15 seconds."
                    mail.send(alert_msg)
                except Exception as mail_error:
                    print(f"OTP alert email failed: {mail_error}")

                return "<h2 style='color:red; background:black; padding:20px; font-family:Arial;'>❌ 3 failed OTP attempts! Security alert email sent. You are locked out for 15 seconds. <a href='/otp' style='color:#ffcc00;'>Try Again</a></h2>"

            return f"<h2 style='color:red; background:black; padding:20px; font-family:Arial;'>❌ Invalid OTP! Attempts left: {attempts_left}. <a href='/otp' style='color:#ffcc00;'>Try Again</a></h2>"
            
    return render_template("otp.html")

@app.route("/success")
@app.route("/success.html")
def success_page():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)