# 🚀 NOC AI Shift Handover Dashboard

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge\&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-2088FF?style=for-the-badge\&logo=githubactions\&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-Container%20Apps-0078D4?style=for-the-badge\&logo=microsoftazure\&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-Integration-0052CC?style=for-the-badge\&logo=jira)
![Slack](https://img.shields.io/badge/Slack-Notifications-4A154B?style=for-the-badge\&logo=slack)
![Nagios](https://img.shields.io/badge/Nagios-Monitoring-6E2B8C?style=for-the-badge)

</p>

---

## 📌 Overview

**NOC AI Shift Handover Dashboard** is an AI-assisted automation platform designed for Network Operations Center (NOC) engineers.

The dashboard automatically collects monitoring alerts, Jira tickets, and operational information to generate a centralized shift handover view. It eliminates manual reporting and provides a single place to monitor operational health.

---

# ✨ Features

* 📊 Live Dashboard
* 🚨 Nagios Alert Monitoring
* 🎫 Jira Ticket Integration
* 📈 Alert Statistics & Charts
* 🤖 AI-assisted Shift Handover
* 📄 Downloadable Reports
* 💬 Slack Notifications
* 🔄 Automatic Data Refresh
* 🐳 Docker Containerized
* ☁️ Azure Container Apps Deployment
* ⚙️ GitHub Actions CI/CD

---

# 🖥 Dashboard

The dashboard provides:

* Active Nagios Alerts
* Jira Ticket Summary
* Alert Pie Chart
* Ticket Status Chart
* AI Shift Summary
* Auto Refresh
* Responsive UI

---

# 🏗 Architecture

```text
                   GitHub Repository
                           │
                           ▼
                  GitHub Actions CI/CD
                           │
                           ▼
                    Docker Image Build
                           │
                           ▼
                      Docker Hub
                           │
                           ▼
              Azure Container Apps
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
       ▼                   ▼                   ▼
   Nagios API          Jira API         Slack Webhook
       │                   │                   │
       └───────────────────┼───────────────────┘
                           ▼
              NOC AI Shift Handover Dashboard
```

---

# 🛠 Tech Stack

| Category         | Technology           |
| ---------------- | -------------------- |
| Backend          | Python               |
| Framework        | Flask                |
| Monitoring       | Nagios               |
| Ticketing        | Jira                 |
| Notifications    | Slack                |
| Charts           | Chart.js             |
| Frontend         | HTML, CSS, Bootstrap |
| Containerization | Docker               |
| CI/CD            | GitHub Actions       |
| Cloud            | Azure Container Apps |

---

# 📂 Project Structure

```text
noc-ai-shift-handover
│
├── app.py
├── collector.py
├── nagios_client.py
├── jira_client.py
├── slack_sender.py
├── report_generator.py
├── scheduler.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── config.py
├── templates/
├── static/
└── data/
```

---

# ⚙️ CI/CD Pipeline

Every push to the **main** branch automatically:

```text
Developer
     │
git push
     │
     ▼
GitHub Actions
     │
     ▼
Build Docker Image
     │
     ▼
Push to Docker Hub
     │
     ▼
Deploy to Azure Container Apps
     │
     ▼
Live Dashboard Updated 🚀
```

---

# 📊 Dashboard Features

✅ Nagios Monitoring

✅ Jira Integration

✅ Shift Handover Summary

✅ Alert Charts

✅ Ticket Charts

✅ Slack Notification

✅ Automatic Deployment

---

# 🚀 Local Installation

Clone the repository

```bash
git clone https://github.com/teppalalalit3-spec/noc-ai-shift-handover.git
```

Move into the project

```bash
cd noc-ai-shift-handover
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

---

# 🐳 Run with Docker

Build

```bash
docker build -t noc-ai-shift-handover .
```

Run

```bash
docker run -p 8000:8000 noc-ai-shift-handover
```

---

# ☁ Azure Deployment

This project is deployed using:

* Azure Container Apps
* Docker Hub
* GitHub Actions
* Automatic CI/CD

Every GitHub push automatically deploys the latest version.

---

# 🔮 Future Enhancements

* 🤖 AI Root Cause Analysis
* 🧠 Duplicate Jira Detection
* 📥 PDF Report Download
* 📅 Shift History
* 📈 Azure Monitor Integration
* 🔄 Rollback Support
* 🔐 User Authentication
* 📊 Application Insights

---

# 👨‍💻 Author

**Lalit Kumar**

NOC Engineer | DevOps Enthusiast | Cloud & AI Automation Learner

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

🛠 Contribute improvements

---

<p align="center">

**Built with ❤️ using Python, Flask, Docker, GitHub Actions & Azure**

</p>
