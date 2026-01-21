import streamlit as st
import pandas as pd
import datetime as dt


st.set_page_config(page_title="Dashboard", layout="wide",page_icon="🧋")

st.sidebar.image("assets/logo.png")
st.sidebar.markdown("""
    <h4 style='text-align:center; font-family: sans-seriff'>Always Online!</h4>
""", unsafe_allow_html=True)

st.title("🔔Chai & Coffee Analytics Dashboard")
st.write("Analytics based on customer orders")

orders_df = pd.read_csv("data/orders.csv")

#----------------------------
#Choice Select Box
#----------------------------

refined_df = orders_df.copy()
refined_df["Order Placed"] = pd.to_datetime(
    refined_df["Order Placed"].astype(str).str.strip(),
    errors="coerce",
    infer_datetime_format=True
)

st.divider()



#----------------------------
# KPI CALCULATION
#----------------------------

total_revenue = refined_df["Total Revenue"].sum()
total_cups_sold = refined_df["Cups Number"].sum()
total_orders = len(refined_df)
best_sold = refined_df.groupby("Choice")["Cups Number"].sum().idxmax()

#----------------------------
# DISPLAY
#----------------------------
import time

def animated_metric(label, target_value, suffix="", duration=0.4):
    placeholder = st.empty()
    steps = 30
    delay = duration / steps

    for i in range(steps + 1):
        current = int((target_value / steps) * i)
        placeholder.metric(label, f"{current}{suffix}")
        time.sleep(delay)

st.subheader("In a glance👀")
col1, col2, col3, col4 = st.columns(4)

with col1:
    animated_metric("💰 Total Revenue (₹)", total_revenue)

with col2:
    animated_metric("🧾 Total Orders", total_orders)

with col3:
    animated_metric("☕ Cups Sold", total_cups_sold)

with col4:
    col4.metric("🏆 Best Seller", best_sold)  # don’t animate text


st.divider()


#----------------------------
# SESSION STATE DECLARE
#----------------------------
view_format = None

if "view_format" not in st.session_state:
    st.session_state.view_format = "overview"
col1, col2 = st.columns(2)

with col1:
    if st.button("Overview", key="overview_btn"):
        st.session_state.view_format = "overview"

with col2:
    if st.button("Analytics", key="anaytics_btn"):
        st.session_state.view_format = "analytics"

#----------------------------
# OVERVIEW BOARD
#----------------------------

recent_df = (
    refined_df
    .dropna(subset=["Order Placed"])
    .sort_values("Order Placed", ascending=False)
    .head(5)
    [["Customer Name", "Gender", "Total Revenue"]]
)



if st.session_state.view_format == "overview":
    col1, col2 = st.columns(2)
    with col2:
        st.subheader("🧾 Recent Buyers")
        st.dataframe(
            recent_df,
            use_container_width=True,
            hide_index=True
        )
    with col1:
        refined_df["Month"] = refined_df["Order Placed"].dt.month        
        refined_df["Month Name"] = refined_df["Order Placed"].dt.month_name()     

        monthly_revenue = refined_df.groupby(["Month","Month Name"])["Total Revenue"].sum().reset_index()
        monthly_revenue = monthly_revenue.sort_values("Month")
        st.bar_chart(monthly_revenue, x="Month Name", y="Total Revenue")    
        
    refined_df["Hour"] = refined_df["Order Placed"].dt.hour
    def get_time_bucket(hour):
        if 0 <= hour < 4:
            return "Midnight"
        if 4 <= hour < 6:
            return "Dawn"
        if 6 <= hour < 12:
            return "Morning"
        if 12 <= hour < 15:
            return "Noon"
        if 15 <= hour < 17:
            return "Afternoon"
        if 17 <= hour < 18:
            return "Evening"
        if 18 <= hour < 24:
            return "Night"
    
    refined_df["Time Bucket"] = refined_df["Hour"].apply(get_time_bucket)

    time_orders = refined_df.groupby("Time Bucket")["Cups Number"].sum().reset_index()
    bucket_order = [
        "Midnight", "Dawn", "Morning", "Noon", "Afternoon", "Evening", "Night"
    ]

    time_orders["Time Bucket"] = pd.Categorical(
        time_orders["Time Bucket"],
        categories=bucket_order,
        ordered=True
    )

    st.subheader("🕒 Orders by Time of Day")
    view_option = None
    if "view_option" not in st.session_state:
        st.session_state.view_option = "Bar Chart"
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Bar Chart"):
            st.session_state.view_option = "Bar Chart"
    with col2:
        if st.button("Line Chart"):
            st.session_state.view_option = "Line Chart"

    if st.session_state.view_option == "Bar Chart":
        st.bar_chart(time_orders, x="Time Bucket", y="Cups Number")
    if st.session_state.view_option == "Line Chart":
        st.line_chart(time_orders, x="Time Bucket", y="Cups Number")
#----------------------------
# ANALYTICS BOARD
#----------------------------
if st.session_state.view_format == "analytics":

    col1, col2 = st.columns(2)
    with col1:
    # Chai vs Coffee
        st.subheader("☕ Chai vs Coffee Sales")
        drinks = refined_df.groupby("Drink Type")["Cups Number"].sum().reset_index()
        st.bar_chart(drinks, x= "Drink Type", y="Cups Number")

    with col2:
    #Top 5 items sold
        st.subheader("🔥 Top 5 Selling Items")
        items = refined_df.groupby("Choice")["Cups Number"].sum().sort_values(ascending=False).head(5)
        st.bar_chart(items)

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
    #City vs Revenue
        st.subheader("💵 Revenue vs City")
        money = refined_df.groupby("City Name")["Total Revenue"].sum().sort_values(ascending=False).head(5)
        st.bar_chart(money)
    with col2:
    #Branch vs Orders
        st.subheader("🏪 Orders by Branch")
        orders = refined_df.groupby("Branch Name")["Cups Number"].sum().sort_values(ascending=False).head(5)
        st.bar_chart(orders)



