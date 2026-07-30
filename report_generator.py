from datetime import datetime
import os


def generate_report(alerts, tickets, alert_summary, ticket_summary):
    """Generate a NOC Shift Handover Report"""

    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reports/handover_{timestamp}.txt"

    with open(filename, "w") as report:

        report.write("=" * 70 + "\n")
        report.write("                 NOC SHIFT HANDOVER REPORT\n")
        report.write("=" * 70 + "\n\n")

        report.write(
            f"Generated On : {datetime.now().strftime('%d-%b-%Y %H:%M:%S')}\n\n"
        )

        # ----------------------------------------------------
        # NAGIOS ALERT SUMMARY
        # ----------------------------------------------------

        report.write("NAGIOS ALERT SUMMARY\n")
        report.write("-" * 70 + "\n")

        for status, count in sorted(alert_summary.items()):
            report.write(f"{status:<12}: {count}\n")

        report.write("\n")

        # ----------------------------------------------------
        # JIRA SUMMARY
        # ----------------------------------------------------

        report.write("JIRA TICKET SUMMARY\n")
        report.write("-" * 70 + "\n")

        if ticket_summary:
            for status, count in sorted(ticket_summary.items()):
                report.write(f"{status:<15}: {count}\n")
        else:
            report.write("No open Jira tickets.\n")

        report.write("\n")

        # ----------------------------------------------------
        # ACTIVE NAGIOS ALERTS
        # ----------------------------------------------------

        report.write("ACTIVE NAGIOS ALERTS\n")
        report.write("-" * 70 + "\n")

        if alerts:
            for alert in alerts:
                report.write(
                    f"[{alert['status']}] "
                    f"{alert['host']} | "
                    f"{alert['service']} | "
                    f"{alert['message']}\n"
                )
        else:
            report.write("No active alerts.\n")

        report.write("\n")

        # ----------------------------------------------------
        # OPEN JIRA TICKETS
        # ----------------------------------------------------

        report.write("OPEN JIRA TICKETS\n")
        report.write("-" * 70 + "\n")

        if tickets:
            for ticket in tickets:
                report.write(
                    f"{ticket['id']} | "
                    f"{ticket['status']} | "
                    f"{ticket['priority']} | "
                    f"{ticket['title']}\n"
                )
        else:
            report.write("No open Jira tickets.\n")

        report.write("\n")

        # ----------------------------------------------------
        # SHIFT SUMMARY
        # ----------------------------------------------------

        report.write("SHIFT SUMMARY\n")
        report.write("-" * 70 + "\n")
        report.write(f"Total Active Alerts : {len(alerts)}\n")
        report.write(f"Total Open Tickets  : {len(tickets)}\n")

        report.write("\n")
        report.write("=" * 70 + "\n")
        report.write("End of Report\n")
        report.write("=" * 70 + "\n")

    return filename
