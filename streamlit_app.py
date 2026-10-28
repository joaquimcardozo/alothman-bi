
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Al Othman BI",
    page_icon="📊",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("AL OTHMAN")
st.sidebar.caption("Business Intelligence")
st.sidebar.divider()

report = st.sidebar.radio(
    "Reports",
    [
        "Dashboard",
        "Weekly Sales",
        "Season to Date",
        "Stock on Hand",
        "Sell Through by Brand"
    ]
)

st.sidebar.divider()

company = st.sidebar.selectbox(
    "Company",
    ["ALKW - Kuwait", "ALBH - Bahrain"]
)

season = st.sidebar.selectbox(
    "Season",
    ["FALL 2026", "PREFALL 2026"]
)

# Main header
st.title("Al Othman BI Reporting")
st.caption("Microsoft Dynamics AX 2012 R3 | Azure SQL")

st.divider()

# Example data only - not connected to Azure
if report == "Dashboard":

    st.subheader("Sales Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Sales Quantity", "249")

    with col2:
        st.metric("Retail Sales", "KWD 157,217")

    with col3:
        st.metric("Sales Cost", "KWD 59,668")

    st.info(
        "Development preview using sample Kuwait "
        "sales totals for 1-24 October 2026. "
        "Not connected to Azure SQL."
    )

elif report == "Weekly Sales":
    st.subheader("Weekly Sales Report")
    st.write("Barcode-level weekly sales report.")

elif report == "Season to Date":
    st.subheader("Season-to-Date Sales")
    st.write("Cumulative sales quantity, retail, cost and margin.")

elif report == "Stock on Hand":
    st.subheader("Stock on Hand")
    st.write("Inventory by barcode, color, size and warehouse.")

elif report == "Sell Through":
    st.subheader("Sell Through Report")
    st.write("Received quantity, sales, stock and sell-through percentage.")

st.divider()
st.caption("Al Othman Fashion | BI Reporting System")
