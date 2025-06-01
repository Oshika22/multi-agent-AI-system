import sqlite3
import json
from datetime import datetime

# Connect to SQLite DB
conn = sqlite3.connect("memory.db")
cursor = conn.cursor()

# Create the memory_log table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS memory_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT,
    type TEXT,
    intent TEXT,
    extracted TEXT,
    timestamp TEXT
)
''')
conn.commit()


def log_to_memory(source, type, intent, extracted):
    """
    Store a memory log in the SQLite DB.
    Converts extracted dict to JSON string.
    """
    extracted_json = json.dumps(extracted)  # Convert dict to JSON
    timestamp = datetime.now().isoformat()
    cursor.execute("""
        INSERT INTO memory_log (source, type, intent, extracted, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (source, type, intent, extracted_json, timestamp))
    conn.commit()


def get_memory_logs():
    """
    Fetch all memory logs from the DB (most recent first).
    Handles JSON decode errors gracefully.
    """
    cursor.execute("SELECT * FROM memory_log ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    logs = []

    for row in rows:
        try:
            extracted = json.loads(row[4])  # Safely convert back to dict
        except json.JSONDecodeError:
            extracted = {"error": "Invalid JSON in DB", "raw": row[4]}  # fallback

        logs.append({
            "id": row[0],
            "source": row[1],
            "type": row[2],
            "intent": row[3],
            "extracted": extracted,
            "timestamp": row[5]
        })

    return logs
