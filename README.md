# 🚀 Azure DevOps Streamlit Pipeline

End-to-end DevOps pipeline for deploying a Streamlit web app.

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Registry:** GitHub Container Registry
- **Cloud:** Microsoft Azure App Service
- **Language:** Python 3.11

## 📁 Project Structure

azure-devops-streamlit/
├── app/                 # Application code
├── tests/               # Unit tests
├── .github/workflows/   # CI/CD pipelines
├── Dockerfile           # Container definition
└── requirements.txt     # Python dependencies



## 🐳 Docker Usage

### Build Locally
\```bash
docker build -t streamlit-app:v1 .
\```

### Run Locally
\```bash
docker run -d -p 8501:8501 --name my-app streamlit-app:v1
\```

### Pull from GHCR (Pre-built)
\```bash
docker pull ghcr.io/YOUR-USERNAME/streamlit-app:latest
\```

## 📦 Container Registry

Docker images are published to **GitHub Container Registry**:
- Registry: `ghcr.io`
- Image: `ghcr.io/ArunDesineni/streamlit-app`
- Tags: `latest`, `v1`