import streamlit as st
import pandas as pd

st.set_page_config(page_title="Menu", layout="wide",page_icon="🧋")

st.sidebar.image("assets/logo.png")
st.sidebar.markdown("""
    <h4 style='text-align:center; font-family: sans-seriff'>Always Online!</h4>
""", unsafe_allow_html=True)

#----------------------------
# Title & KPI for bestseller
#----------------------------

st.title("🧾Menu")

orders_df = pd.read_csv("data/orders.csv")
menu_df = pd.read_csv("data/menu.csv")

best_sold = orders_df.groupby("Choice")["Cups Number"].sum().idxmax()
price = menu_df.loc[menu_df["Item"] == best_sold, "Price_INR"]

col1,col2 = st.columns(2)

with col1:
    col1.metric("Best Seller",best_sold)
with col2:
    col2.metric("Price (Rs)", price)

st.divider()

#----------------------------
# Menu starts here
#----------------------------
st.subheader("👀Check for the items")

if "view_format" not in st.session_state:
    st.session_state.view_format = "Chai"

col1, col2 = st.columns(2)
with col1:
    if st.button("Chai"):
        st.session_state.view_format = "Chai"
with col2:
    if st.button("Coffee"):
        st.session_state.view_format = "Coffee"

#----------------------------
# Chai Items in the menu
#----------------------------

if st.session_state.view_format == "Chai":
    filtered_df = menu_df[menu_df["Drink_Type"] == "Chai"]

else:
    filtered_df = menu_df[menu_df["Drink_Type"] == "Coffee"]

Image_map = {
    "Chai" : "assets/chai.jpg",
    "Coffee" : "assets/coffee.jpg"
}

def image_box(drink_type,item,price):
    with st.container(border=True):
        st.image(
            Image_map.get(drink_type),
            use_container_width=True
        )
        st.markdown(f"{item}")
        st.markdown(f"{price}")

cols = st.columns(3)
for i, row in filtered_df.iterrows():
    with cols[i % 3]:
        image_box(
        drink_type= row["Drink_Type"],
        item = row["Item"],
        price= row["Price_INR"]
    )
    

 
