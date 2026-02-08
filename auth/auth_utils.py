import sqlite3
import hashlib
import os
from datetime import datetime

# ---------------- CONSTANTS ----------------
DB_PATH = "database/users.db"
os.makedirs("database", exist_ok=True)

# ---------------- DB CONNECTION ----------------
def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

# ---------------- INIT DB ----------------
def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        mobile TEXT,
        degree TEXT CHECK(degree IN ('B.Tech','M.Tech','MCA')),
        branch TEXT,
        college TEXT,
        university TEXT,
        passing_year INTEGER,
        cgpa TEXT,
        skills TEXT,
        profile_pic TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()

# Initialize DB at import
init_db()

# ---------------- PASSWORD HASHING ----------------
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

# ---------------- REGISTER USER ----------------
def register_user(
    full_name,
    email,
    password,
    mobile,
    degree,
    branch,
    college,
    university,
    passing_year,
    cgpa,
    skills,
    profile_pic_path
):
    try:
        email = email.lower().strip()   # normalize email

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO users (
            full_name, email, password, mobile,
            degree, branch, college, university,
            passing_year, cgpa, skills,
            profile_pic, created_at
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            full_name.strip(),
            email,
            hash_password(password),
            mobile,
            degree,
            branch,
            college,
            university,
            passing_year,
            cgpa,
            ",".join(skills),
            profile_pic_path,
            datetime.now().isoformat()
        ))

        conn.commit()
        conn.close()
        return True

    except sqlite3.IntegrityError:
        return False
    except Exception as e:
        print("Register error:", e)
        return False

# ---------------- LOGIN USER ----------------
def login_user(email, password):
    email = email.lower().strip()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT id, full_name, email, degree
    FROM users
    WHERE email=? AND password=?
    """, (email, hash_password(password)))

    user = cur.fetchone()
    conn.close()

    return user

# ---------------- GET USER DETAILS ----------------
def get_user_details(email):
    email = email.lower().strip()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE email=?", (email,))
    data = cur.fetchone()

    conn.close()
    return data
