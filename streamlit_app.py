
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

# Customer Traffic Dashboard - Development Preview

import pandas as pd

st.divider()
st.header("ALKW Customer Traffic")
st.caption("Development preview - sample data only")

start_date = st.date_input(
    "From Date",
    value=pd.Timestamp("2026-11-01").date()
)

end_date = st.date_input(
    "To Date",
    value=pd.Timestamp("2026-11-07").date()
)

# Illustrative records, not actual customer data
data = pd.DataFrame([
    {
        "CustomerAccount": "DEMO-001",
        "CustomerCategory": "Existing",
        "NetBuyKWD": 120.000
    },
    {
        "CustomerAccount": "DEMO-002",
        "CustomerCategory": "Returning",
        "NetBuyKWD": 550.000
    },
    {
        "CustomerAccount": "DEMO-003",
        "CustomerCategory": "New",
        "NetBuyKWD": 315.000
    }
])

if start_date > end_date:
    st.error("From Date must be before To Date.")
    st.stop()

col1, col2, col3 = st.columns(3)

col1.metric("Customers", len(data))
col2.metric(
    "Net Buy (KWD)",
    f"{data['NetBuyKWD'].sum():,.3f}"
)
col3.metric(
    "Existing Customers",
    (data["CustomerCategory"] == "Existing").sum()
)

st.subheader("Customer Classification")

summary = (
    data.groupby("CustomerCategory")
    .size()
    .rename("Customers")
)

st.bar_chart(summary)

st.subheader("Customer Details")
st.dataframe(data, use_container_width=True)

st.download_button(
    "Download CSV",
    data=data.to_csv(index=False),
    file_name="customer_traffic_demo.csv",
    mime="text/csv"
)

