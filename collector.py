from collections import Counter
from nagios_client import get_live_alerts
from jira_client import get_open_tickets


def load_alerts():
    """
    Fetch live pending alerts from Nagios.
    """
    return get_live_alerts()


def load_tickets():
    """
    Fetch all open Jira tickets.
    """
    return get_open_tickets()


def get_alert_summary(alerts):
    """
    Count Nagios alerts by status.
    """
    summary = Counter()

    for alert in alerts:
        status = alert.get("status", "UNKNOWN").upper()
        summary[status] += 1

    # Ensure common statuses always exist
    return {
        "CRITICAL": summary.get("CRITICAL", 0),
        "WARNING": summary.get("WARNING", 0),
        "UNKNOWN": summary.get("UNKNOWN", 0),
        "OK": summary.get("OK", 0)
    }


def get_ticket_summary(tickets):
    """
    Count Jira tickets by workflow status.
    Works with any Jira workflow.
    """

    summary = Counter()

    for ticket in tickets:
        status = ticket.get("status", "Unknown")
        summary[status] += 1

    return dict(summary)
