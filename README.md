<h1 align="center">🛡️ Login After Dark</h1><p align="center">
  <strong>Next-Gen Secure 2FA & Threat-Mitigation System</strong>
</p><p align="center">
  A secure web-based authentication and threat-monitoring system designed to protect
  modern applications against repeated unauthorized login attempts and suspicious activity.
</p><hr><h2>📌 About the Project</h2><p>
<strong>Login After Dark</strong> is a secure web-based authentication system built with
<strong>Python, Flask, HTML, CSS, and JavaScript</strong>. It combines username and password
authentication with <strong>Email OTP verification</strong> to provide two-factor protection.
</p><p>
The system also includes failed-attempt protection, temporary lockouts, automated security
alert emails, unusual login-time detection, and <strong>Google Gemini AI integration</strong>.
</p><h2>🚀 Key Features</h2><p>The project currently includes <strong>8 major security and functionality features:</strong></p><ol>
  <li>
    <strong>🔐 Two-Factor Authentication (2FA)</strong><br>
    The system verifies the user's username and password first and then requires an
    OTP sent to the registered email address.
<img width="678" height="287" alt="Image" src="https://github.com/user-attachments/assets/ae7c807e-43bc-4c2d-9552-83c9a9629939"  />
  </li>  <li>
    <strong>⏱️ Credential Brute-Force Protection</strong><br>
    After 3 consecutive incorrect username or password attempts, the login system is
    temporarily frozen for<strong>15 seconds</strong>.

  <img width="684" height="184" alt="Image" src="https://github.com/user-attachments/assets/ece4bb5b-916b-4e51-8b9c-d4adc0a6764c" />
  <img width="684" height="184" alt="Image" src="https://github.com/user-attachments/assets/ece4bb5b-916b-4e51-8b9c-d4adc0a6764c" />
  </li>  <li>
    <strong>🔢 OTP Attempt Protection</strong><br>
    After 3 consecutive incorrect OTP attempts, OTP verification is temporarily
    frozen for <strong>15 seconds</strong>.
    <img width="502" height="176" alt="Image" src="https://github.com/user-attachments/assets/671dc8ca-4e84-4239-8380-5dcd7a452f65" />
    <img width="533" height="185" alt="Image" src="https://github.com/user-attachments/assets/c3fd6dc3-2cba-4112-8dc6-101dae5055bd" />
  </li>  <li>
    <strong>🚨 Automated Security Alert Email</strong><br>
    When 3 consecutive incorrect username or password attempts are detected,
    the system automatically sends a security alert email to notify about the
    failed login attempts.
  </li>  <li>
    <strong>🕒 Unusual Login Time Detection</strong><br>
    The system monitors login timing and can identify authentication attempts
    occurring during configured unusual or off-hours.
  </li>  <li>
    <strong>⚠️ Unusual Activity Security Warning</strong><br>
    When an unusual login time is detected, the system can generate a security
    warning and notify the relevant user or administrator.
  </li>  <li>
    <strong>🤖 Google Gemini AI Integration</strong><br>
    Google Gemini AI is integrated to provide AI-powered functionality within
    the application.
  </li>  <li>
    <strong>🔒 Environment & Secret Protection</strong><br>
    Sensitive configuration values are kept outside the source code using
    environment variables and <code>.env</code> configuration. A
    <code>.env.example</code> template can be used to show required variables
    without exposing actual credentials.
  </li>
</ol><h2>🛡️ Security Architecture</h2><h3>1. ⏱️ Adaptive Brute-Force Defense</h3><p>
The system applies a 3-attempt threshold and a 15-second temporary lockout
to both major authentication stages.
</p><ul>
  <li>
    <strong>Phase 1 – Credentials:</strong> Protects the username and password
    login stage from repeated incorrect attempts.
  </li>
  <li>
    <strong>Phase 2 – OTP:</strong> Protects the OTP verification stage from
    repeated incorrect OTP submissions.
  </li>
</ul><h3>2. 🚨 Automated Security Alert</h3><p>
When the failed-login threshold is reached, the backend automatically sends
a security alert email containing information about the failed authentication
event. This helps the user or administrator become aware of possible
unauthorized access attempts.
</p><h3>3. 🕒 Behavioral Anomaly Detection</h3><p>
The system can monitor the timing of successful authentication attempts.
If a login occurs during a configured unusual or off-hours period, the
system can generate an <strong>Unusual Activity Security Warning</strong>.
</p><h3>4. 🔐 Environment Isolation</h3><p>
The project separates application code and sensitive configuration. Secrets
such as email credentials and API keys are stored using environment variables
instead of being directly written into the source code.
</p><h2>🧪 Demo Login</h2><p>For testing purposes, use the following credentials:</p>
<img width="673" height="291" alt="Image" src="https://github.com/user-attachments/assets/21cf1b5f-a13f-4419-9815-8cd2ece8c8be" />
<table>
  <tr>
    <th>Field</th>
    <th>Demo Value</th>
  </tr>
  <tr>
    <td><strong>Username</strong></td>
    <td><code>admin</code></td>
  </tr>
  <tr>
    <td><strong>Password</strong></td>
    <td><code>12345</code></td>
  </tr>
</table><p>
After successful credential verification, an OTP is sent to the registered
email address. The user must enter the correct OTP to complete authentication.
  <img width="691" height="269" alt="Image" src="https://github.com/user-attachments/assets/1d45dc37-e5c2-4fdb-b2ca-7d1d9174d893" />
</p><h2>🔑 Authentication Flow</h2><ol>
  <li>The user opens the login page.</li>
  <li>The user enters their username and password.</li>
  <li>The backend verifies the credentials.</li>
  <li>If the credentials are incorrect, the failed-attempt counter increases.</li>
  <li>After 3 consecutive failed attempts, login is frozen for 15 seconds.</li>
  <li>A security alert email is sent when the failed-login threshold is reached.</li>
  <li>If the credentials are correct, an OTP is sent to the registered email address.</li>
  <li>The user enters the received OTP.</li>
  <li>If the OTP is incorrect, the failed-OTP counter increases.</li>
  <li>After 3 consecutive incorrect OTP attempts, OTP verification is frozen for 15 seconds.</li>
  <li>If the OTP is correct, the user is successfully authenticated.</li>
  <li>The system can also check whether the login occurred during a configured unusual time period.</li>
</ol><h2>🛡️ Two-Factor Protection</h2><p>
At present, <strong>Login After Dark</strong> provides two-factor protection:
</p><ul>
  <li><strong>First Factor:</strong> Username and password authentication.</li>
  <li><strong>Second Factor:</strong> Email OTP verification.</li>
</ul><p>
Both authentication stages include protection against repeated incorrect attempts,
providing an additional layer of protection against unauthorized access.
</p><h2>🚨 Threat Mitigation</h2><p>
The system is designed to identify and respond to repeated authentication failures.
It uses temporary lockouts and security notifications to reduce the impact of
repeated unauthorized login attempts.
</p><ul>
  <li>3 failed credential attempts → 15-second login lockout.</li>
  <li>3 failed OTP attempts → 15-second OTP lockout.</li>
  <li>Repeated credential failures → Security alert email.</li>
  <li>Unusual login time → Unusual activity warning.</li>
</ul><p>
The backend and frontend are kept separately to maintain a clear project
structure and make the application easier to manage and develop.
</p><h2>🛠️ Tech Stack</h2><table>
  <tr>
    <th>Technology</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td><strong>Python</strong></td>
    <td>Backend development</td>
  </tr>
  <tr>
    <td><strong>Flask</strong></td>
    <td>Web backend and API handling</td>
  </tr>
  <tr>
    <td><strong>Flask-Mail</strong></td>
    <td>Email and OTP delivery</td>
  </tr>
  <tr>
    <td><strong>HTML5</strong></td>
    <td>Frontend structure</td>
  </tr>
  <tr>
    <td><strong>CSS3</strong></td>
    <td>Frontend styling</td>
  </tr>
  <tr>
    <td><strong>JavaScript</strong></td>
    <td>Frontend functionality</td>
  </tr>
  <tr>
    <td><strong>Google Gemini AI</strong></td>
    <td>AI-powered functionality</td>
  </tr>
  <tr>
    <td><strong>python-dotenv</strong></td>
    <td>Environment variable management</td>
  </tr>
  <tr>
    <td><strong>SMTP</strong></td>
    <td>Email communication</td>
  </tr>
  <tr>
    <td><strong>Git & GitHub</strong></td>
    <td>Version control and project hosting</td>
  </tr>
</table><h2>🔒 Security Practices</h2><ul>
  <li>Sensitive credentials should be stored in environment variables.</li>
  <li>Actual <code>.env</code> files should not be committed to GitHub.</li>
  <li>Use <code>.env.example</code> to document required configuration variables.</li>
  <li>Authentication attempts are monitored for repeated failures.</li>
  <li>Temporary lockouts help limit repeated authentication attempts.</li>
  <li>Email alerts provide notification of repeated failed login attempts.</li>
</ul><h2>📂 Project Purpose</h2><p>
This project was developed to demonstrate a modern authentication and
threat-mitigation system combining <strong>2FA</strong>, Email OTP,
failed-attempt protection, security alerts, unusual login-time detection,
environment-based secret management, and <strong>Google Gemini AI</strong>.
</p><hr><p align="center">
  <strong>🛡️ Login After Dark</strong>
</p><p align="center">
  Built with Python, Flask, HTML, CSS, JavaScript & Google Gemini AI.
</p>
