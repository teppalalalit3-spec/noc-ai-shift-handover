from jira import JIRA
from dotenv import load_dotenv
import os

load_dotenv()


def get_jira():
    """
    Create Jira connection only when needed.
    """
    return JIRA(
        server=os.getenv("JIRA_URL"),
        basic_auth=(
            os.getenv("JIRA_EMAIL"),
            os.getenv("JIRA_API_TOKEN")
        )
    )


def get_open_tickets():
    """
    Fetch all Jira tickets that are not Done.
    """

    try:

        jira = get_jira()

        issues = jira.search_issues(
            "status != Done ORDER BY priority DESC",
            maxResults=100
        )

        tickets = []

        for issue in issues:

            tickets.append({
                "id": issue.key,
                "title": issue.fields.summary,
                "status": issue.fields.status.name if issue.fields.status else "Unknown",
                "priority": issue.fields.priority.name if issue.fields.priority else "Not Set",
                "assignee": issue.fields.assignee.displayName if issue.fields.assignee else "Unassigned"
            })

        return tickets

    except Exception as e:

        print(f"Jira Error: {e}")

        return []
