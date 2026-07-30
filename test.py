from collector import (
    load_alerts,
    load_tickets,
    get_alert_summary,
    get_ticket_summary
)

alerts = load_alerts()
tickets = load_tickets()

print("Alerts Summary")
print(get_alert_summary(alerts))

print("\nTickets Summary")
print(get_ticket_summary(tickets))
