from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'admin123'))
    conn.commit()
    conn.close()

init_db()

# Vulnerable Login (SQLi)
@app.route('/vulnerable-login', methods=['GET', 'POST'])
def vulnerable_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"  # UNSAFE
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()
        if user:
            return f"<h2>Welcome, {user[1]}!</h2> <p>🔥 This login is vulnerable to SQL Injection.</p>"
        else:
            return "<h2>Login Failed!</h2>"
    return render_template('login.html', title="Vulnerable Login")

# Secure Login
@app.route('/secure-login', methods=['GET', 'POST'])
def secure_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))  # SAFE
        user = cursor.fetchone()
        conn.close()
        if user:
            return f"<h2>Welcome, {user[1]}!</h2> <p>🔒 This login is secure.</p>"
        else:
            return "<h2>Login Failed!</h2>"
    return render_template('login.html', title="Secure Login")

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
