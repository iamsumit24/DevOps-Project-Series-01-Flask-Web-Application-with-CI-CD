from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("dashboard.html")

@app.route('/health')
def health():
    return {"status": "UP"}

@app.route('/journey')
def journey():
    return jsonify({
        "name": "Sumit Tiwari",
        "start": "January 2025 - AWS DevOps Intern",
        "milestones": [
            "Completed AWS training (EC2, IAM, VPC, S3, Lambda)",
            "Built Flask & FastAPI apps with Docker",
            "Implemented CI/CD with Jenkins & Ansible",
            "Deployed on Kubernetes with monitoring tools"
        ],
        "current_focus": "Mastering CI/CD + GitOps on Kubernetes"
    })

@app.route('/tools')
def tools():
    return jsonify({
        "CI/CD": ["Jenkins", "GitHub Actions", "ArgoCD"],
        "Containers": ["Docker", "Podman"],
        "Kubernetes": ["kubeadm", "Minikube", "Helm"],
        "IaC": ["Terraform", "Ansible"],
        "Monitoring": ["Prometheus", "Grafana", "cAdvisor"],
        "Cloud": ["AWS (EC2, S3, IAM, Lambda)", "EKS"]
    })

@app.route('/mentorship')
def mentorship():
    return jsonify({
        "mentor": "Mr. Vimal Daga",
        "role": "DevOps Guru & World Record Holder",
        "learning_platform": "https://devopsprojects.hash13.com/",
        "impact": "Hands-on, industry-ready DevOps training experience"
    })

@app.route('/resources')
def resources():
    return jsonify({
        "docs": {
            "Docker": "https://docs.docker.com/",
            "Kubernetes": "https://kubernetes.io/docs/",
            "Terraform": "https://developer.hashicorp.com/terraform/docs",
            "Jenkins": "https://www.jenkins.io/doc/"
        },
        "YouTube": "https://www.youtube.com/@vimaldaga",
        "LinkedIn": "https://www.linkedin.com/in/sumit-tiwari-devops"
    })

@app.route('/contact')
def contact():
    return jsonify({
        "name": "Sumit Tiwari",
        "location": "Jabalpur, India",
        "email": "sumittiwari.prof24@gmail.com",
        "phone": "8103803420",
        "linkedin": "https://www.linkedin.com/in/sumit-tiwari-devops"
    })