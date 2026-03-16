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

A robust user authentication system that demonstrates modern security practices. The application handles user registration, encrypted password storage, and protected routes, ensuring that sensitive data is only accessible to authenticated users.

**Key Features:**
* **🔐 Password Hashing:** Uses `Werkzeug` to salt and hash passwords, preventing plain-text exposure in the database.
* **session Management:** Implements `Flask-Login` to track user sessions and restrict access to specific endpoints.
* **📁 Database Integration:** Leverages `Flask-SQLAlchemy` for persistent and structured user data storage.
* **📥 File Downloads:** Includes a secure mechanism for authenticated users to download protected assets.

<br>

<h3>
  📁 Project Structure<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

```text
secure-auth-app/
├── main.py                     # App logic, Routes & Auth configuration
├── instance/                   # Database instance folder
│   └── users.db                # SQLite database for user credentials
├── templates/                  # HTML Frontend
│   ├── login.html
│   ├── register.html
│   └── secrets.html
└── static/                     # CSS & Static assets (files to download)

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
* **Security First:** Excellent implementation of password salting and hashing, which is vital for any real-world app.
* **Access Control:** Smart use of decorators (like `@login_required`) to protect sensitive routes.

**🔧 Key Recommendations:**
* **Validation:** Add stronger form validation to ensure users don't register with empty fields.
* **Flash Messages:** Use Flask's `flash()` method for better user feedback.

<br>

<div align="center">
  <img src="https://img.shields.io/badge/🤖_AI_Contribution-Project_HTML_%26_CSS-50FA7B?style=flat-square" alt="AI Note">
  <br>
  <samp style="font-size: 12px; color: #6272a4;">The HTML and CSS templates within this project were co-authored with AI.</samp>
</div>

<br>

<div align="center">
  <img src="https://placehold.co/1000x3/FE428E/FE428E.png" width="100%" height="3" alt="Pink Divider"/>
</div>
