import sqlite3


DB_PATH = "database/tracker.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS periods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def add_period(start_date, end_date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO periods (
            start_date,
            end_date
        )
        VALUES (?, ?)
    """, (start_date, end_date))

    conn.commit()
    conn.close()

def get_periods():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM periods
        ORDER BY start_date DESC
    """)

    periods = cursor.fetchall()

    conn.close()

    return periods