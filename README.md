# DevOps-Project-Series-01: Flask Web Application with CI/CD Pipeline

👨‍💻 **Created by Sumit Tiwari**  
🚀 A beginner-friendly real-world DevOps project using Flask, Docker, Jenkins, and GitHub CI/CD automation.

---

## 🛠 Tech Stack

- **Flask** – Backend Web Framework (Python)
- **Docker** – Containerization
- **Jenkins** – CI/CD Pipeline Automation
- **Pytest** – Automated Unit Testing
- **GitHub** – Version Control
- **Linux (RHEL 9)** – Hosting Environment

---

## ⚙️ Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python run.py
# Build Docker Image
docker build -t flask-ci-cd .

# Run Container
docker run -p 5000:5000 flask-ci-cd
# Run tests
PYTHONPATH=. pytest
Jenkins CI/CD Pipeline
Jenkins pipeline automates:

Cloning repo

Installing dependencies

Running tests (Pytest)

Building Docker image

Deploying the container

Build fails if even one test fails ❌ — promoting test-first DevOps practices.

🙏 Mentorship Acknowledgement
This project is built as part of a real-world DevOps learning journey under the guidance of Mr. Vimal Daga Sir — a global DevOps mentor.

📬 Contact
📧 Email: sumittiwari.prof24@gmail.com
🌐 LinkedIn: linkedin.com/in/sumit-tiwari-devops

