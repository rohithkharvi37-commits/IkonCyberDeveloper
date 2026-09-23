<h1 align="center">🔐 Login After Dark</h1><p align="center">
  A secure web-based authentication system with <strong>Email OTP verification</strong>,
  <strong>AI integration</strong>, and <strong>failed-attempt protection</strong>.
</p><hr><h2>📌 About the Project</h2><p>
<strong>Login After Dark</strong> is a web-based authentication system that includes both
<strong>frontend</strong> and <strong>backend</strong> components. It provides secure
username and password authentication followed by Email OTP verification.
The project also integrates <strong>Google Gemini AI</strong> and includes security
features to help prevent repeated unauthorized login attempts.
</p><h2>🚀 Key Features</h2><p>The project currently includes <strong>6 main security and functionality features:</strong></p><ol>
  <li><strong>Username & Password Authentication</strong> – Validates the user's login credentials before allowing access.</li>  <li><strong>Email OTP Verification</strong> – Sends an OTP to the registered email address as a second authentication step.</li>  <li><strong>Login Attempt Protection</strong> – After 3 consecutive incorrect username or password attempts, the login system is frozen for <strong>15 seconds</strong>.</li>  <li><strong>OTP Attempt Protection</strong> – After 3 consecutive incorrect OTP attempts, OTP verification is frozen for <strong>15 seconds</strong>.</li>  <li><strong>Security Alert Email</strong> – After 3 consecutive incorrect username or password attempts, the system sends a security alert email to notify the user about the failed login attempts.</li>  <li><strong>Google Gemini AI Integration</strong> – Uses Google Gemini AI to provide AI-powered functionality within the application.</li>
</ol><h2>🧪 Demo Login</h2><p>For testing purposes, use the following credentials:</p><table>
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
If the correct username and password are entered, the system proceeds to OTP verification.
If incorrect credentials are entered 3 consecutive times, the login system is temporarily
frozen for 15 seconds and a security alert email is sent.
</p><h2>🔑 Authentication Flow</h2><ol>
  <li>The user opens the login page.</li>
  <li>The user enters their username and password.</li>
  <li>The backend verifies the credentials.</li>
  <li>If the credentials are incorrect, the failed-attempt counter increases.</li>
  <li>After 3 consecutive failed attempts, login is frozen for 15 seconds and a security alert email is sent.</li>
  <li>If the credentials are correct, an OTP is sent to the user's registered email address.</li>
  <li>The user enters the received OTP.</li>
  <li>If the OTP is incorrect, the failed-OTP counter increases.</li>
  <li>After 3 consecutive incorrect OTP attempts, OTP verification is frozen for 15 seconds.</li>
  <li>If the OTP is correct, the user is successfully logged in.</li>
</ol><h2>🛡️ Two-Factor Protection</h2><p>
At present, <strong>Login After Dark</strong> uses two-factor protection:
</p><ul>
  <li><strong>First Factor:</strong> Username and password authentication.</li>
  <li><strong>Second Factor:</strong> Email OTP verification.</li>
</ul><p>
Both authentication steps have protection against repeated incorrect attempts.
This provides an additional layer of security against unauthorized access.
<table>
  <tr>
    <th>Technology</th>
    <th>Usage</th>
  </tr>
  <tr>
    <td><strong>HTML</strong></td>
    <td>Frontend structure</td>
  </tr>
  <tr>
    <td><strong>CSS</strong></td>
    <td>Frontend styling</td>
  </tr>
  <tr>
    <td><strong>JavaScript</strong></td>
    <td>Frontend functionality</td>
  </tr>
  <tr>
    <td><strong>Python</strong></td>
    <td>Backend development</td>
  </tr>
  <tr>
    <td><strong>Email OTP</strong></td>
    <td>Two-factor authentication</td>
  </tr>
  <tr>
    <td><strong>Google Gemini AI</strong></td>
    <td>AI-powered functionality</td>
  </tr>
  <tr>
    <td><strong>Git & GitHub</strong></td>
    <td>Version control and project hosting</td>
  </tr>
</table><h2>🔒 Security Overview</h2><p>
The application combines <strong>username/password authentication</strong>,
<strong>Email OTP verification</strong>, <strong>failed-attempt protection</strong>,
and <strong>security alert emails</strong> to provide a multi-layered authentication
process.
</p><p>
After 3 consecutive incorrect login attempts, the system temporarily freezes login
for <strong>15 seconds</strong> and sends a security alert email. Similarly,
3 consecutive incorrect OTP attempts temporarily freeze OTP verification for
<strong>15 seconds</strong>.
</p><h2>📂 Project Purpose</h2><p>
This project was developed to demonstrate a secure web-based authentication system
with frontend and backend integration, two-factor authentication, failed-attempt
protection, security alerts, and Google Gemini AI integration.
</p><hr><p align="center">
  <strong>🔐 Login After Dark</strong>
</p><p align="center">
  Built with HTML, CSS, JavaScript, Python & Google Gemini AI.
</p>