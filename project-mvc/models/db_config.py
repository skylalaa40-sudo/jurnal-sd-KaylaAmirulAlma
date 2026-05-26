import os

# Mengambil password dari environment variable (.env)
DB_PASSWORD = os.getenv("DB_PASSWORD")

def connect_db():
    if DB_PASSWORD:
        return "Database connected successfully"
    else:
        return "Database connection failed: missing password"