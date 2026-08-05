from jira_client import get_open_tickets

tickets = get_open_tickets()

for ticket in tickets:
    print(ticket)

