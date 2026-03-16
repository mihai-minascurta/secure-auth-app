<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&pause=1000&color=A9FEF7&center=true&vCenter=true&width=600&lines=%F0%9F%93%92+Secure+Authentication+App;%F0%9F%94%92+Flask-Login+%2B+Werkzeug;%F0%9F%9B%A1%EF%B8%8F+Secure+User+Management" alt="Animated Header" />
</div>

<br>

<div align="center">
  <img src="https://img.shields.io/badge/Python-FE428E?style=for-the-badge&logo=python&logoColor=white" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Flask-A9FEF7?style=for-the-badge&logo=flask&logoColor=black" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/SQLite-C3B550?style=for-the-badge&logo=sqlite&logoColor=black" height="35">
</div>

<br>

<h3>
  🚀 Project Overview<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

A professional-grade authentication system built with Flask, focusing on industry-standard security protocols. The application provides a secure environment for user registration and login, utilizing advanced encryption to safeguard user credentials.

**Technical Logic (Verified):**
* **🔐 Cryptographic Hashing:** Implements `Werkzeug.security` to generate salted password hashes (pbkdf2:sha256), ensuring that plain-text passwords are never stored in the database.
* **🛡️ Session Management:** Uses `Flask-Login` to manage user sessions, providing persistent authentication across different pages and browser restarts.
* **🚫 Access Control:** Employs the `@login_required` decorator to protect sensitive routes (like the "Secrets" page), redirecting unauthorized users back to the login screen.
* **📁 Database Schema:** Built with `SQLAlchemy`, featuring a structured User model that handles unique emails and hashed credentials efficiently.

<br>

<h3>
  📁 Project Structure<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

```text
secure-auth-app/
├── main.py                     # Security logic, Flask routes & Auth setup
├── instance/                   # Database instance storage
│   └── users.db                # SQLite database for encrypted credentials
├── templates/                  # Secure HTML templates (login, register, secrets)
└── static/                     # CSS & Protected assets for download
```
<h3>
  🧠 Code Review & Complexity<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

<div align="center">
  <img src="https://img.shields.io/badge/OVERALL_DIFFICULTY-INTERMEDIATE-FE428E?style=for-the-badge&logoColor=white" height="35">
</div>

<br>

> **📊 SYSTEM COMPLEXITY RADAR**
>
> 🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛ **90%** | **Security & Hashing (Werkzeug)**<br>
> 🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛ **70%** | **Database Ops (SQLAlchemy)**<br>
> 🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛ **80%** | **Session Management (Flask-Login)**<br>
> 🟪🟪🟪🟪🟪🟪⬛⬛⬛⬛ **60%** | **Frontend (Jinja2 Templates)**

<br>

**🟢 High-Impact Wins:**
* **Security Standards:** Correct use of `generate_password_hash` and `check_password_hash`, avoiding common beginner security pitfalls.
* **Asset Protection:** Secure implementation of file downloads that are only accessible to verified users.

**🔧 Technical Debt:**
* **CSRF Protection:** While the authentication is solid, adding `Flask-WTF` for CSRF protection would be the next step to make it enterprise-ready.
* **Validation:** Form input could be further hardened by checking for password complexity (length, symbols) during registration.

<br>

<div align="center">
  <img src="https://img.shields.io/badge/🤖_AI_Contribution-Project_HTML_%26_CSS-50FA7B?style=flat-square" alt="AI Note">
  <br>
  <samp style="font-size: 12px; color: #6272a4;">Any custom HTML/CSS used in this project's templates was co-authored with AI.</samp>
</div>

<br>

<div align="center">
  <img src="https://placehold.co/1000x3/FE428E/FE428E.png" width="100%" height="3" alt="Pink Divider"/>
</div>
