import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="DevOps Pipeline Demo",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 End-to-End DevOps Pipeline Demo")
st.markdown("### Deployed via GitHub Actions CI/CD on Azure")

# Sidebar
st.sidebar.header("📚 Project Info")
st.sidebar.success("✅ Source: GitHub")
st.sidebar.success("✅ CI/CD: GitHub Actions")
st.sidebar.success("✅ Container: Docker")
st.sidebar.success("✅ Host: Azure App Service")
st.sidebar.info(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# Main content
col1, col2 = st.columns(2)

with col1:
    st.subheader("👋 Welcome!")
    name = st.text_input("Enter your name:")
    if st.button("Greet Me"):
        if name:
            st.success(f"Hello **{name}**! Welcome to DevOps! 🎉")
        else:
            st.warning("Please enter your name")

with col2:
    st.subheader("🧮 Quick Calculator")
    a = st.number_input("Number 1", value=10)
    b = st.number_input("Number 2", value=5)
    st.metric("Sum", a + b)

# Footer
st.markdown("---")
st.caption("Built with ❤️ | Streamlit + Docker + GitHub Actions + Azure")