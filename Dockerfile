# ===================================
# Dockerfile for Streamlit App
# ===================================

# Step 1: Start with a base image (Python 3.11 on Linux)
FROM python:3.11-slim

# Step 2: Set working directory inside container
WORKDIR /app

# Step 3: Copy requirements.txt first (optimization trick!)
COPY requirements.txt .

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy all application code
COPY ./app ./app

# Step 6: Tell Docker which port the app uses
EXPOSE 8501

# Step 7: Health check (is the app alive?)
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Step 8: Command to run when container starts
CMD ["streamlit", "run", "app/app.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0", \
     "--server.headless=true"]