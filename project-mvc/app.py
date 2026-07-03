from flask import Flask, render_template
import os

from controllers.api_handler import get_users
from views.dashboard_component import (
    render_dashboard,
    fetch_data_from_api
)

app = Flask(__name__)

# ==============================
# Variabel Lingkungan
# ==============================
user_name = os.getenv("APP_USER", "Guest")
app_env = os.getenv("APP_ENV", "development")

# ==============================
# Simulasi State Aplikasi
# ==============================
app_state = {
    "items": [],
    "is_loading": True
}


def update_state(new_data):
    app_state["items"] = new_data
    app_state["is_loading"] = False


# ==============================
# Route Flask
# ==============================
@app.route("/")
def home():

    products = [
        {"id": 101, "name": "Produk A"},
        {"id": 102, "name": "Produk B"}
    ]

    users = [
        {"id": 1, "name": "Admin"},
        {"id": 2, "name": "User"}
    ]

    return render_template(
        "index.html",
        user=user_name,
        env=app_env,
        products=products,
        users=users
    )


# ==============================
# Main Program
# ==============================
if __name__ == "__main__":

    print("===== VERSI 2.0 - STABIL =====")
    print(f"Halo {user_name}!")
    print(f"Status Lingkungan: {app_env}")

    print("Loading data...")

    mock_data = [
        {"id": 101, "name": "Produk A"},
        {"id": 102, "name": "Produk B"}
    ]

    # Render loading
    render_dashboard(app_state["items"], app_state["is_loading"])

    # Update data
    update_state(mock_data)

    # Render setelah loading
    render_dashboard(app_state["items"], app_state["is_loading"])

    # Simulasi API
    data = fetch_data_from_api(get_users)

    if data:
        render_dashboard(data)

    # Jalankan Flask
    app.run(host="0.0.0.0", port=5000)