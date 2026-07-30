from slack_sender import send_to_slack

send_to_slack(
    {"CRITICAL": 8, "WARNING": 2},
    {"To Do": 6},
    "reports/handover_test.txt"
)
