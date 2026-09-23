import os
import random
import time
import base64
import cv2
import numpy as np
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
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

# Credentials & Security Passwords
USERNAME = "admin"
PASSWORD = "12345"
DURESS_PASSWORD = "0000"  # Set to 0000 as you tested! Triggers decoy page & silent alarm

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if "failed_attempts" not in session:
        session["failed_attempts"] = 0
    if "lockout_time" not in session:
        session["lockout_time"] = 0

    # 15-second lockout check for Login
    current_time = time.time()
    lockout_duration = 15
    if current_time - session["lockout_time"] < lockout_duration:
        remaining = int(lockout_duration - (current_time - session["lockout_time"]))
        return f"<h2 style='color:#ffcc00; background:black; padding:20px; font-family:Arial;'>⚠️ Too many failed login attempts! Locked out. Please try again in {remaining} seconds. <a href='/login' style='color:#fff;'>Refresh</a></h2>"

    if request.method == "POST":
        username = request.form.get("username")
        entered_password = request.form.get("password")
        
        # ---------------------------------------------------------
        # DURESS / PANIC MODE TRIGGER (0000)
        # ---------------------------------------------------------
        if username == USERNAME and entered_password == DURESS_PASSWORD:
            session.clear()
            session["user"] = username
            session["duress_active"] = True
            
            # Send Silent Emergency Panic Alert Email
            try:
                recipient_email = os.getenv("MAIL_USERNAME")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                alert_msg = Message("🚨 EMERGENCY ALERT: Duress Code Activated!", sender=os.getenv("MAIL_USERNAME"), recipients=[recipient_email])
                alert_msg.body = f"CRITICAL SECURITY WARNING:\n\nThe panic/duress password (0000) was entered at {timestamp} from IP: {request.remote_addr}.\nSilent alarm triggered. The user has been safely routed to a decoy dashboard to avoid raising suspicion."
                mail.send(alert_msg)
            except Exception as mail_error:
                print(f"Duress alert email failed: {mail_error}")

            return redirect(url_for("decoy_dashboard"))

        # ---------------------------------------------------------
        # NORMAL SECURE LOGIN FLOW
        # ---------------------------------------------------------
        if username == USERNAME and entered_password == PASSWORD:
            session["failed_attempts"] = 0
            session["lockout_time"] = 0
            
            # Reset OTP tracking variables
            session["otp_failed_attempts"] = 0
            session["otp_lockout_time"] = 0
            
            # GENERATE OTP & RECORD EXPIRATION TIMESTAMP (1 min 30 sec = 90 seconds)
            otp = str(random.randint(100000, 999999))
            session["otp"] = otp
            session["otp_timestamp"] = time.time()
            
            current_hour = datetime.now().hour
            is_unusual_time = (current_hour >= 10 and current_hour <= 18)
            
            if is_unusual_time:
                timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                email_subject = "🚨 Security Alert & OTP: Unusual Login Time"
                email_body = f"SECURITY WARNING:\nYour login was initiated at an unusual hour ({timestamp_str}).\n\nYour OTP code is: {otp}\n(Note: Valid for 1 minute 30 seconds)"
            else:
                email_subject = "Team Ikon - Your OTP Code"
                email_body = f"Your OTP code is: {otp}\n(Note: Valid for 1 minute 30 seconds)"
            
            # Send the single OTP email immediately
            try:
                recipient_email = os.getenv("MAIL_USERNAME") 
                msg = Message(email_subject, sender=os.getenv("MAIL_USERNAME"), recipients=[recipient_email])
                msg.body = email_body
                mail.send(msg)
            except Exception as mail_error:
                print(f"OTP email failed: {mail_error}")

            # Abnormal Authentication & Session Binding: Bind IP Address & Device Fingerprint
            session["user_ip"] = request.remote_addr
            session["user_agent"] = request.headers.get('User-Agent')
            session["user"] = username
            
            # Redirect to Biometric Face Authentication step
            return redirect(url_for("face_page"))
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

@app.route("/face")
def face_page():
    if "user" not in session or session.get("duress_active"):
        return redirect(url_for("login"))
    return render_template("face.html")

@app.route("/verify-face", methods=["POST"])
def verify_face():
    if "user" not in session:
        return jsonify({"success": False, "message": "Unauthorized session"})

    try:
        data = request.get_json(silent=True)
        if not data or "image" not in data:
            return jsonify({"success": False, "message": "Invalid or missing JSON payload!"})

        img_string = data["image"]
        img_data = img_string.split(",")[1] if "," in img_string else img_string
        
        # Decode live webcam image from base64
        np_arr = np.frombuffer(base64.b64decode(img_data), np.uint8)
        live_img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        
        if live_img is None:
            return jsonify({"success": False, "message": "Failed to decode webcam image frame."})

        # Load the Master Owner Image (owner.jpg)
        owner_path = os.path.join(BASE_DIR, "owner.jpg")
        if not os.path.exists(owner_path):
            return jsonify({"success": False, "message": "Master face photo (owner.jpg) not found in Backend folder!"})

        owner_img = cv2.imread(owner_path)
        if owner_img is None:
            return jsonify({"success": False, "message": "Could not read owner.jpg image file."})

        # Resize both images to standard dimensions (200x200) for direct comparison
        live_resized = cv2.resize(live_img, (200, 200))
        owner_resized = cv2.resize(owner_img, (200, 200))

        # Convert to grayscale
        live_gray = cv2.cvtColor(live_resized, cv2.COLOR_BGR2GRAY)
        owner_gray = cv2.cvtColor(owner_resized, cv2.COLOR_BGR2GRAY)

        # Mathematically compare histograms
        hist_live = cv2.calcHist([live_gray], [0], None, [256], [0, 256])
        cv2.normalize(hist_live, hist_live, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

        hist_owner = cv2.calcHist([owner_gray], [0], None, [256], [0, 256])
        cv2.normalize(hist_owner, hist_owner, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

        similarity = cv2.compareHist(hist_owner, hist_live, cv2.HISTCMP_CORREL)

        # Threshold for matching
        if similarity > 0.35:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": f"Access Denied: Face does not match owner profile! (Score: {similarity:.2f})"})
            
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

@app.route("/otp", methods=["GET", "POST"])
@app.route("/otp.html", methods=["GET", "POST"])
def otp_page():
    if "user" not in session or session.get("duress_active"):
        return redirect(url_for("login"))

    # Abnormal Authentication Checks (IP & Browser/Device Fingerprint Mismatch)
    if request.remote_addr != session.get("user_ip") or request.headers.get('User-Agent') != session.get("user_agent"):
        session.clear()
        return "<h2 style='color:red; background:black; padding:20px; font-family:Arial;'>🚨 Security Alert: Abnormal Session / Device Mismatch Detected! Possible Session Hijacking. Access Denied. <a href='/login' style='color:#ffcc00;'>Login Again</a></h2>"

    # CHECK OTP EXPIRATION (1 minute 30 seconds = 90 seconds)
    otp_expiry_limit = 90
    if "otp_timestamp" in session:
        elapsed_time = time.time() - session["otp_timestamp"]
        if elapsed_time > otp_expiry_limit:
            session.pop("otp", None)
            session.pop("otp_timestamp", None)
            return "<h2 style='color:#ffcc00; background:black; padding:20px; font-family:Arial;'>⚠️ OTP has expired! It is only valid for 1 minute and 30 seconds. <a href='/login' style='color:#fff;'>Please Login Again</a></h2>"

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
    if "user" not in session or session.get("duress_active"):
        return redirect(url_for("login"))

    # Abnormal Authentication Checks (IP & Browser/Device Fingerprint Mismatch)
    if request.remote_addr != session.get("user_ip") or request.headers.get('User-Agent') != session.get("user_agent"):
        session.clear()
        return "<h2 style='color:red; background:black; padding:20px; font-family:Arial;'>🚨 Security Alert: Abnormal Session / Device Mismatch Detected! Possible Session Hijacking. Access Denied. <a href='/login' style='color:#ffcc00;'>Login Again</a></h2>"

    return render_template("success.html")

@app.route("/decoy-dashboard")
def decoy_dashboard():
    if "user" not in session or not session.get("duress_active"):
        return redirect(url_for("login"))
    # Decoy page looks completely normal / empty so an attacker thinks they gained access safely
    return """
    <!DOCTYPE html>
    <html>
    <head><title>Dashboard</title></head>
    <body style="background:#0f172a; color:#f8fafc; font-family:Arial; text-align:center; padding:100px;">
        <div style="max-width:400px; margin:0 auto; background:#1e293b; padding:40px; border-radius:12px; border:1px solid #334155;">
            <h2 style="color:#fff; margin-top:0;">Welcome, User</h2>
            <p style="color:#94a3b8;">No recent records or sensitive data available.</p>
            <a href="/login" style="color:#3b82f6; text-decoration:none; font-size:14px;">Logout</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=False)