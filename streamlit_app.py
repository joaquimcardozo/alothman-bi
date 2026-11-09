
import streamlit as st
import pandas as pd
from datetime import date

# ======================================================
# PAGE CONFIGURATION
# ======================================================

st.set_page_config(
    page_title="Al Othman BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# GOOGLE LOGIN
# ======================================================

if not st.user.is_logged_in:

    st.title("🔐 Al Othman BI")
    st.subheader("Employee Sign In")

    st.write(
        "Welcome to the Al Othman Business "
        "Intelligence Reporting System."
    )

    st.write(
        "Please sign in using your approved Google account."
    )

    if st.button(
        "Sign in with Google",
        type="primary"
    ):
        st.login("google")

    st.stop()


# ======================================================
# EMPLOYEE AUTHORIZATION
# ======================================================

email = str(
    st.user.get("email", "")
).strip().lower()

email_verified = st.user.get(
    "email_verified", False
) is True

allowed_emails = {
    str(address).strip().lower()
    for address in st.secrets["access"]["allowed_emails"]
}

if not email_verified or email not in allowed_emails:

    st.error(
        "Access denied. Your Google account is "
        "not authorized to use Al Othman BI."
    )

    if st.button("Log out"):
        st.logout()

    st.stop()


# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.title("AL OTHMAN")
st.sidebar.caption("Business Intelligence")

st.sidebar.success("Authenticated")

st.sidebar.write(
    f"Signed in as: {email}"
)

if st.sidebar.button("Log out"):
    st.logout()

st.sidebar.divider()

report = st.sidebar.radio(
    "Reports",
    [
        "Dashboard",
        "Customer Traffic",
        "Weekly Sales",
        "Season to Date",
        "Stock on Hand",
        "Sell Through by Brand"
    ]
)

st.sidebar.divider()

company = st.sidebar.selectbox(
    "Company",
    [
        "ALKW - Kuwait",
        "ALBH - Bahrain"
    ]
)

season = st.sidebar.selectbox(
    "Season",
    [
        "FALL 2026",
        "PREFALL 2026"
    ]
)


# ======================================================
# MAIN HEADER
# ======================================================

st.title("Al Othman BI Reporting")
st.caption(
    "Microsoft Dynamics AX 2012 R3 | Azure SQL"
)

st.divider()


# ======================================================
# DASHBOARD
# ======================================================

if report == "Dashboard":

    st.subheader("Business Intelligence Dashboard")

    st.info(
        "Development preview. "
        "Live Azure SQL data is not connected."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Reports Available", "5")
    col2.metric("Companies", "2")
    col3.metric("Authentication", "Google")

    st.write(
        "Select a report from the left sidebar."
    )


# ======================================================
# CUSTOMER TRAFFIC
# ======================================================

elif report == "Customer Traffic":

    st.subheader("Customer Traffic Report")

    if company != "ALKW - Kuwait":

        st.warning(
            "Customer Traffic is currently being "
            "developed for ALKW - Kuwait."
        )

        st.stop()

    st.caption(
        "ALKW | Development preview | Sample data"
    )

    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input(
            "From Date",
            value=date(2026, 11, 1)
        )

    with col2:
        end_date = st.date_input(
            "To Date",
            value=date(2026, 11, 7)
        )

    if start_date > end_date:
        st.error(
            "From Date cannot be after To Date."
        )
        st.stop()

    # Demo data only.
    # Actual customer data will come from AOF_BI.

    data = pd.DataFrame([
        {
            "CustomerAccount": "DEMO-001",
            "CustomerName": "Sample Existing Customer",
            "CustomerCategory": "Existing",
            "NetBuyKWD": 120.000,
            "TicketCount": 1
        },
        {
            "CustomerAccount": "DEMO-002",
            "CustomerName": "Sample Returning Customer",
            "CustomerCategory": "Returning",
            "NetBuyKWD": 550.000,
            "TicketCount": 1
        },
        {
            "CustomerAccount": "DEMO-003",
            "CustomerName": "Sample New Customer",
            "CustomerCategory": "New",
            "NetBuyKWD": 315.000,
            "TicketCount": 1
        }
    ])

    st.warning(
        "These are sample records. "
        "Date filters are not yet connected "
        "to Azure SQL."
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Customers",
        len(data)
    )

    col2.metric(
        "New Customers",
        int(
            (data["CustomerCategory"] == "New").sum()
        )
    )

    col3.metric(
        "Existing Customers",
        int(
            (data["CustomerCategory"] == "Existing").sum()
        )
    )

    col4.metric(
        "Net Buy (KWD)",
        f"{data['NetBuyKWD'].sum():,.3f}"
    )

    st.divider()

    st.subheader("Customer Classification")

    summary = (
        data.groupby("CustomerCategory")
        .size()
        .rename("Customers")
    )

    st.bar_chart(summary)

    st.subheader("Customer Details")

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        label="Download CSV",
        data=data.to_csv(index=False),
        file_name="customer_traffic_demo.csv",
        mime="text/csv"
    )


# ======================================================
# OTHER REPORTS
# ======================================================

elif report == "Weekly Sales":

    st.subheader("Weekly Sales")
    st.info("Report under development.")


elif report == "Season to Date":

    st.subheader("Season-to-Date Sales")
    st.info("Report under development.")


elif report == "Stock on Hand":

    st.subheader("Stock on Hand")
    st.info("Report under development.")


elif report == "Sell Through by Brand":

    st.subheader("Sell Through by Brand")
    st.info("Report under development.")


# ======================================================
# FOOTER
# ======================================================

st.divider()

st.caption(
    "Al Othman Fashion | Business Intelligence"
)
