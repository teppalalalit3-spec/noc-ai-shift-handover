import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK = os.getenv("SLACK_WEBHOOK_URL")


def send_to_slack(report_file):

    with open(report_file, "r") as f:
        report = f.read()

    payload = {
        "blocks": [

            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "📋 NOC SHIFT HANDOVER REPORT"
                }
            },

            {
                "type": "divider"
            },

            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"```{report}```"
                }
            }

        ]
    }

    response = requests.post(
        WEBHOOK,
        json=payload
    )

    if response.status_code == 200:
        print("✅ Slack handover sent successfully.")
    else:
        print(response.text)
