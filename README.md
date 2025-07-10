# SQL Injection Demonstration Tool

![Demo Preview](https://i.imgur.com/JQ8KZOl.png)  
*A professional Flask-based web application demonstrating SQL Injection vulnerabilities and secure coding practices.*

---

## 🚀 **Features**
- **Vulnerable Login Page** (Demonstrates classic SQL Injection)
- **Secure Login Page** (Uses parameterized queries)
- **Clean, Professional UI** with side-by-side comparison
- **Educational Explanations** of attacks and defenses
- **Self-contained Setup** (SQLite database, no external dependencies)

---

## ⚙️ **Installation (Kali Linux)**

### Prerequisites
- Python 3.x
- Kali Linux (or any Linux distro)

### Step-by-Step Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/sql-injection-demo.git
cd sql-injection-demo
```
# Create and activate virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
# Install dependencies
```
pip install flask
```
# Initialize database and run application
```
python init_db.py  # Creates sample database
```
# Running the Application
```bash
# Start the Flask server (default: http://127.0.0.1:5000)
python app.py
```
# For network access (LAN):
```
python app.py --host 0.0.0.0
python app.py
```
