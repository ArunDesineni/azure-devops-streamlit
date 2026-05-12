"""
DevOps Pipeline Demo - Main Streamlit Application
Demonstrates clean code structure and modular design.
"""
import streamlit as st
import pandas as pd
from datetime import datetime

from config import APP_NAME, APP_VERSION, APP_ENV, AZURE_REGION
from utils.calculations import add, subtract, multiply, divide, calculate_percentage
from utils.data_generator import generate_sales_data, get_top_products


# ===== Page Configuration =====
st.set_page_config(
    page_title=APP_NAME,
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ===== Sidebar =====
def render_sidebar():
    """Render the sidebar content."""
    st.sidebar.title("🚀 " + APP_NAME)
    st.sidebar.markdown(f"**Version:** `{APP_VERSION}`")
    
    # Environment badge
    env_color = "🟢" if APP_ENV == "production" else "🟡"
    st.sidebar.markdown(f"**Environment:** {env_color} `{APP_ENV}`")
    st.sidebar.markdown(f"**Region:** 🌍 `{AZURE_REGION}`")
    st.sidebar.markdown("---")
    
    st.sidebar.subheader("📚 Tech Stack")
    st.sidebar.success("✅ Streamlit")
    st.sidebar.success("✅ Docker")
    st.sidebar.success("✅ GitHub Actions")
    st.sidebar.success("✅ Azure")
    
    st.sidebar.markdown("---")
    st.sidebar.caption(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M')}")


# ===== Page: Home =====
def page_home():
    """Render the Home page."""
    st.title("🏠 Welcome to the DevOps Demo App")
    st.markdown("### This app demonstrates an end-to-end CI/CD pipeline")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Deployments Today", "12", "+3")
    with col2:
        st.metric("Uptime", "99.9%", "+0.1%")
    with col3:
        st.metric("Response Time", "120ms", "-20ms")
    
    st.markdown("---")
    
    st.subheader("👋 Say Hello")
    name = st.text_input("Your name:")
    if st.button("Greet Me", type="primary"):
        if name:
            st.success(f"Hello **{name}**! 🎉 You're learning DevOps like a pro!")
            st.balloons()
        else:
            st.warning("Please enter your name 👆")


# ===== Page: Calculator =====
def page_calculator():
    """Render the Calculator page."""
    st.title("🧮 Calculator")
    st.markdown("Uses functions from `utils/calculations.py`")
    
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("First number", value=10.0)
    with col2:
        b = st.number_input("Second number", value=5.0)
    
    operation = st.radio(
        "Operation:",
        ["Add", "Subtract", "Multiply", "Divide", "Percentage"],
        horizontal=True,
    )
    
    if st.button("Calculate", type="primary"):
        try:
            if operation == "Add":
                result = add(a, b)
            elif operation == "Subtract":
                result = subtract(a, b)
            elif operation == "Multiply":
                result = multiply(a, b)
            elif operation == "Divide":
                result = divide(a, b)
            else:  # Percentage
                result = calculate_percentage(a, b)
                st.info(f"{a} is this % of {b}")
            
            st.success(f"**Result:** `{result}`")
        except ValueError as e:
            st.error(f"❌ Error: {e}")


# ===== Page: Data Dashboard =====
def page_dashboard():
    """Render the Data Dashboard page."""
    st.title("📊 Sales Dashboard")
    st.markdown("Sample data generated via `utils/data_generator.py`")
    
    days = st.slider("Days of data:", 7, 60, 30)
    
    # Sales data
    sales_data = generate_sales_data(days)
    df = pd.DataFrame(sales_data)
    
    st.subheader("📈 Sales Trend")
    st.line_chart(df.set_index("date")[["sales"]])
    
    st.subheader("📋 Raw Data")
    st.dataframe(df, use_container_width=True)
    
    # Top products
    st.subheader("🏆 Top Products")
    products_df = pd.DataFrame(get_top_products())
    st.bar_chart(products_df.set_index("product")["revenue"])


# ===== Main App Logic =====
def main():
    """Main function — the entry point."""
    render_sidebar()
    
    # Navigation
    page = st.sidebar.radio(
        "📍 Navigate:",
        ["🏠 Home", "🧮 Calculator", "📊 Dashboard"],
    )
    
    if page == "🏠 Home":
        page_home()
    elif page == "🧮 Calculator":
        page_calculator()
    elif page == "📊 Dashboard":
        page_dashboard()
    
    # Footer
    st.markdown("---")
    st.caption(f"Built with ❤️ | {APP_NAME} v{APP_VERSION} | {APP_ENV.upper()}")


if __name__ == "__main__":
    main()