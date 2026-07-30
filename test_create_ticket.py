from jira_client import create_incident

ticket = create_incident(
    host="localhost",
    service="HTTP",
    message="HTTP service is CRITICAL"
)

print("Created:", ticket)

