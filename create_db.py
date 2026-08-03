import sqlite3

# Connect to the database
conn = sqlite3.connect("database/faculty.db")

# Create a cursor
cursor = conn.cursor()

# Create admin table
cursor.execute("""
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Insert default admin (only if it doesn't already exist)
cursor.execute("""
INSERT OR IGNORE INTO admin (id, username, password)
VALUES (1, 'admin', 'admin123')
""")

# Create notes table
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    unit TEXT NOT NULL,
    filename TEXT NOT NULL
)
""")

# Save changes
conn.commit()

# Close the connection
conn.close()

print("Database created successfully!")