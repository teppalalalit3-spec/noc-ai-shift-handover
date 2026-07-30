import os
from dotenv import load_dotenv

load_dotenv()

# Nagios
NAGIOS_URL = os.getenv("NAGIOS_URL")
NAGIOS_USERNAME = os.getenv("NAGIOS_USERNAME")
NAGIOS_PASSWORD = os.getenv("NAGIOS_PASSWORD")

# Jira
JIRA_URL = os.getenv("JIRA_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

# Scheduler
REPORT_TIMES = [
    "06:00",
    "14:00",
    "22:00"
]
