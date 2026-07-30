from flask import Flask, render_template
from collector import (
    load_alerts,
    load_tickets,
    get_alert_summary,
    get_ticket_summary
)

import os
import glob
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def dashboard():

    alerts = load_alerts()
    tickets = load_tickets()

    alert_summary = get_alert_summary(alerts)
    ticket_summary = get_ticket_summary(tickets)

    reports = sorted(
        glob.glob("reports/*.txt"),
        reverse=True
    )

    latest_report = os.path.basename(reports[0]) if reports else "No Reports"

    return render_template(
        "index.html",
        alerts=alerts,
        tickets=tickets,
        alert_summary=alert_summary,
        ticket_summary=ticket_summary,
        current_time=datetime.now().strftime("%d-%b-%Y %H:%M:%S"),
        latest_report=latest_report
    )


if __name__ == "__main__":
    app.run(debug=True)
