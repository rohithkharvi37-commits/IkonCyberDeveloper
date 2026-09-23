# IkonCyberDeveloper
<h1 align="center">🔐 Login After Dark</h1><p align="center">
  A secure login system with <strong>Email OTP verification</strong>,
  <strong>Google Gemini AI integration</strong>, and
  <strong>failed-login protection</strong>.
</p><hr><h2>📌 About the Project</h2><p>
<strong>Login After Dark</strong> is a web-based authentication system that includes both
<strong>frontend</strong> and <strong>backend</strong> components. The application provides
username and password authentication followed by <strong>Email OTP verification</strong>
for an additional layer of security.
</p><h2>🚀 Features</h2><ul>
  <li>User-friendly login page developed using frontend technologies.</li>
  <li>Backend handles user authentication and login requests.</li>
  <li>Email OTP verification for secure authentication.</li>
  <li>Username and password validation before allowing access.</li>
  <li>Protection against repeated incorrect login attempts.</li>
  <li><strong>Login protection:</strong> After 3 consecutive incorrect username or password attempts, the login system is frozen for <strong>15 seconds</strong>.</li>
  <li><strong>OTP protection:</strong> After 3 consecutive incorrect OTP attempts, OTP verification is frozen for <strong>15 seconds</strong>.</li>
  <li>Google Gemini AI is integrated into the project for AI-powered functionality.</li>
</ul><h2>🧪 Demo Login</h2><p>For testing purposes, use the following credentials:</p><table>
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
If incorrect credentials are entered, the login attempt is rejected.
</p><h2>🛡️ Security & Failed Attempt Protection</h2><p>
The system includes protection against repeated unauthorized authentication attempts.
Both <strong>login credentials</strong> and <strong>OTP verification</strong> have
a 3-attempt limit.
</p><ul>
  <li>After <strong>3 consecutive incorrect username or password attempts</strong>, login is frozen for <strong>15 seconds</strong>.</li>
  <li>After <strong>3 consecutive incorrect OTP attempts</strong>, OTP verification is frozen for <strong>15 seconds</strong>.</li>
  <li>During the freeze period, the user cannot continue the respective authentication step.</li>
  <li>After the 15-second cooldown, the user can try again.</li>
  <li>Successful authentication resets the relevant failed-attempt counter.</li>
</ul><h2>🔑 Authentication Flow</h2><ol>
  <li>The user opens the login page.</li>
  <li>The user enters their username and password.</li>
  <li>The backend verifies the login credentials.</li>
  <li>If the credentials are incorrect, the failed-login counter increases.</li>
  <li>After 3 consecutive failed login attempts, the login system is frozen for 15 seconds.</li>
  <li>If the credentials are correct, an OTP is sent to the user's registered email address.</li>
  <li>The user enters the received OTP.</li>
  <li>If the OTP is incorrect, the failed-OTP counter increases.</li>
  <li>After 3 consecutive incorrect OTP attempts, OTP verification is frozen for 15 seconds.</li>
  <li>If the OTP is correct, the user is successfully logged in.</li>
</ol><h2>🤖 AI Used</h2><p>
The project uses <strong>Google Gemini AI</strong> to provide AI-powered functionality
and demonstrate the integration of modern AI technology into a web application.
</p><h2>🛠️ Technologies Used</h2><table>
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
    <td>User authentication</td>
<h1 align="center">🔐 Login After Dark</h1><p align="center">
  A secure login system with <strong>Email OTP verification</strong>,
  <strong>Google Gemini AI integration</strong>, and
  <strong>failed-login protection</strong>.
</p><hr><h2>📌 About the Project</h2><p>
<strong>Login After Dark</strong> is a web-based authentication system that includes both
<strong>frontend</strong> and <strong>backend</strong> components. The application provides
username and password authentication followed by <strong>Email OTP verification</strong>
for an additional layer of security.
</p><h2>🚀 Features</h2><ul>
  <li>User-friendly login page developed using frontend technologies.</li>
  <li>Backend handles user authentication and login requests.</li>
  <li>Email OTP verification for secure authentication.</li>
  <li>Username and password validation before allowing access.</li>
  <li>Protection against repeated incorrect login attempts.</li>
  <li><strong>Login protection:</strong> After 3 consecutive incorrect username or password attempts, the login system is frozen for <strong>15 seconds</strong>.</li>
  <li><strong>OTP protection:</strong> After 3 consecutive incorrect OTP attempts, OTP verification is frozen for <strong>15 seconds</strong>.</li>
  <li>Google Gemini AI is integrated into the project for AI-powered functionality.</li>
</ul><h2>🧪 Demo Login</h2><p>For testing purposes, use the following credentials:</p><table>
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
If incorrect credentials are entered, the login attempt is rejected.
</p><h2>🛡️ Security & Failed Attempt Protection</h2><p>
The system includes protection against repeated unauthorized authentication attempts.
Both <strong>login credentials</strong> and <strong>OTP verification</strong> have
a 3-attempt limit.
</p><ul>
  <li>After <strong>3 consecutive incorrect username or password attempts</strong>, login is frozen for <strong>15 seconds</strong>.</li>
  <li>After <strong>3 consecutive incorrect OTP attempts</strong>, OTP verification is frozen for <strong>15 seconds</strong>.</li>
  <li>During the freeze period, the user cannot continue the respective authentication step.</li>
  <li>After the 15-second cooldown, the user can try again.</li>
  <li>Successful authentication resets the relevant failed-attempt counter.</li>
</ul><h2>🔑 Authentication Flow</h2><ol>
  <li>The user opens the login page.</li>
  <li>The user enters their username and password.</li>
  <li>The backend verifies the login credentials.</li>
  <li>If the credentials are incorrect, the failed-login counter increases.</li>
  <li>After 3 consecutive failed login attempts, the login system is frozen for 15 seconds.</li>
  <li>If the credentials are correct, an OTP is sent to the user's registered email address.</li>
  <li>The user enters the received OTP.</li>
  <li>If the OTP is incorrect, the failed-OTP counter increases.</li>
  <li>After 3 consecutive incorrect OTP attempts, OTP verification is frozen for 15 seconds.</li>
  <li>If the OTP is correct, the user is successfully logged in.</li>
</ol><h2>🤖 AI Used</h2><p>
The project uses <strong>Google Gemini AI</strong> to provide AI-powered functionality
and demonstrate the integration of modern AI technology into a web application.
</p><h2>🛠️ Technologies Used</h2><table>
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
    <td>User authentication</td>