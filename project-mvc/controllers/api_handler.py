import random

# Simulasikan data dari database
users = [
    {"id": 1, "name": "Admin"},
    {"id": 2, "name": "User"}
]

def get_users():
    if random.randint(1, 3) == 1:
        return {
            "status": "error",
            "message": "Server sedang sibuk"
        }

    return {
        "status": "success",
        "data": users
    }

