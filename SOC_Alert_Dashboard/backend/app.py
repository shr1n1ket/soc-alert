from flask import Flask, render_template
import json

app = Flask(__name__, template_folder="../frontend/templates",
            static_folder="../frontend/static")

@app.route("/dashboard")
def dashboard():
    with open("alerts/alerts.json") as file:
        alerts = json.load(file)
    return render_template("dashboard.html", alerts=alerts)

if __name__ == "__main__":
    app.run(debug=True)