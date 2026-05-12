"""
Configuration settings for the Streamlit app.
Reads from environment variables with sensible defaults.
"""
import os

# App metadata
APP_NAME = os.getenv("APP_NAME", "DevOps Pipeline Demo")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENV = os.getenv("APP_ENV", "development")  # development / production

# Feature flags
ENABLE_ANALYTICS = os.getenv("ENABLE_ANALYTICS", "false").lower() == "true"

# Azure info (will use later)
AZURE_REGION = os.getenv("AZURE_REGION", "Central India")