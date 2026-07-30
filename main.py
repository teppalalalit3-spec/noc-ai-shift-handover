from collector import (
    load_alerts,
    load_tickets,
    get_alert_summary,
    get_ticket_summary
)

from report_generator import generate_report
from slack_sender import send_to_slack


def main():

    # Fetch live Nagios alerts
    alerts = load_alerts()

    # Fetch open Jira tickets
    tickets = load_tickets()

    # Generate summaries
    alert_summary = get_alert_summary(alerts)
    ticket_summary = get_ticket_summary(tickets)

    # Generate handover report
    report = generate_report(
        alerts,
        tickets,
        alert_summary,
        ticket_summary
    )

    # Send complete report to Slack
    send_to_slack(report)

    print("\n✅ Report Generated Successfully!")
    print(f"📄 Report saved at: {report}")
    print("📨 Slack handover sent successfully.")


if __name__ == "__main__":
    main()
