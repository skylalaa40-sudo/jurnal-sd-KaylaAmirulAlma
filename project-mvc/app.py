from views.dashboard_component import render_dashboard

# Simulasi state aplikasi
app_state = {
    "items": [],
    "is_loading": True
}

def update_state(new_data):
    app_state["items"] = new_data
    app_state["is_loading"] = False


if __name__ == "__main__":
    print("Loading data...")

    mock_data = [
        {"id": 101, "name": "Produk A"},
        {"id": 102, "name": "Produk B"}
    ]

    # State loading
    render_dashboard(app_state["items"], app_state["is_loading"])

    # Update state (data masuk)
    update_state(mock_data)

    # Render ulang setelah data masuk
    render_dashboard(app_state["items"], app_state["is_loading"])