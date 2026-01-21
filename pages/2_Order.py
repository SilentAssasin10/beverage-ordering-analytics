import streamlit as st
import pandas as pd
from datetime import datetime
import os

menu_df = pd.read_csv("data/menu.csv")

st.sidebar.image("assets/logo.png")
st.sidebar.markdown("""
    <h4 style='text-align:center; font-family: sans-seriff'>Always Online!</h4>
""", unsafe_allow_html=True)
st.header("Welcome to the ***Ordering Page***")

#User name
name = st.text_input("Enter your name here:")
gender = st.selectbox("Enter your gender:", ["Male", "Female", "Prefer not to say"], index=None, placeholder="Select One")
city = None
branch = None
if name:
    cities = [
        "Kolkata",
        "Delhi",
        "Mumbai",
        "Bengaluru",
        "Hyderabad",
        "Chennai",
        "Pune",
        "Jaipur",
        "None"
    ]
    city = st.selectbox("Enter your location:",cities, index=None, placeholder="Pick your city")
    if city == "Kolkata":
        branch = st.selectbox("Choose Your branch:", [
        "College Street",
        "Park Street",
        "Salt Lake",
        "New Town",
        "Howrah Station"
    ],index=None, placeholder="Select your branch")
    elif city == "Delhi":
        branch = st.selectbox("Choose Your branch:", [
        "Connaught Place",
        "Chandni Chowk",
        "Karol Bagh",
        "Saket",
        "Dwarka Sector 21"
    ],index=None, placeholder="Select your branch")
    elif city == "Mumbai":
        branch = st.selectbox("Choose Your branch:", [
        "Andheri West",
        "Bandra Linking Road",
        "Dadar Station",
        "Powai",
        "Colaba Causeway"
    ],index=None, placeholder="Select your branch")
    elif city == "Bengaluru":
        branch = st.selectbox("Choose Your branch:", [
        "Whitefield",
        "Indiranagar",
        "Koramangala",
        "Electronic City",
        "Yelahanka"
    ],index=None, placeholder="Select your branch")
    elif city == "Hyderabad":
        branch = st.selectbox("Choose Your branch:", [
        "Hitech City",
        "Gachibowli",
        "Banjara Hills",
        "Secunderabad",
        "Charminar"
    ],index=None, placeholder="Select your branch")
    elif city == "Chennai":
        branch = st.selectbox("Choose Your branch:", [
        "T Nagar",
        "Anna Nagar",
        "Velachery",
        "Adyar",
        "Tambaram"
    ],index=None, placeholder="Select your branch")
    elif city == "Pune":
        branch = st.selectbox("Choose Your branch:", [
        "Hinjewadi",
        "Baner",
        "Wakad",
        "Kothrud",
        "FC Road"
    ],index=None, placeholder="Select your branch")
    elif city == "Jaipur":
        branch = st.selectbox("Choose Your branch:", [
        "MI Road",
        "Vaishali Nagar",
        "Malviya Nagar",
        "Bapu Bazaar",
        "Amer Road"
    ], index=None, placeholder="Select your branch")
    if city == "None":
        pass
        st.error("Sorry we only serve in this cities!")


if branch:
    st.write(f"Hello {name}, Thanks for visiting our {branch} branch. Let's take your order")

if branch:
    st.subheader("Choose what you want to make:")
    choice = st.selectbox("Chai or Coffee?", ["Chai", "Coffee", "None"], index=None, placeholder="Select a drink")

#choice start

    if choice is None:
        st.info("Please select a drink")

    if choice == "None":
        st.error("Sorry for our inconvenience....we only serve Chai or Coffee!")
    chai = None
    coffee = None
    sugar_level = None
    cups = None
    if choice == "Chai":
        chai_type = ["Classic & Popular", "Premium & Special", "Herbal & Healthy", "Fusion & Fun"]
        variant = st.selectbox("Choose your type of chai:", chai_type, index=None, placeholder="Choose from the options")
        
#variants of chai
        classic_popular_chai = ["Masala Chai", "Adrak Chai", "Elaichi Chai", "Cutting Chai", "Ginger Masala Chai"]
        premium_special_chai = ["Kesar Chai","Kashmiri Kahwa","Irani Chai","Saffron Almond Chai","Rose Chai"]
        herbal_healthy_chai = ["Tulsi Chai","Lemongrass Chai","Green Tea","Chamomile Tea","Mint Chai"]
        fusion_fun_chai = ["Chocolate Chai","Vanilla Chai","Caramel Chai"]


        if variant == "Classic & Popular":
            drink = st.selectbox("Choose your chai:", classic_popular_chai, index=None, placeholder="Choose from the options")
            chai = drink
            if chai:
                st.write(f"Awesome! You've chosen {chai}")
                sugar_level = st.slider("Sugar level(Tea Spoons):",0,5,1)
                cups = st.number_input("How many cups?",min_value=1,max_value=10,step=1)

        elif variant == "Premium & Special":
            drink = st.selectbox("Choose your chai:", premium_special_chai, index=None, placeholder="Choose from the options")
            chai = drink
            if chai:
                st.write(f"Awesome! You've chosen {chai}")
                sugar_level = st.slider("Sugar level(Tea Spoons):",0,5,1)
                cups = st.number_input("How many cups?",min_value=1,max_value=10,step=1)


        elif variant == "Herbal & Healthy":
            drink = st.selectbox("Choose your chai:", herbal_healthy_chai, index=None, placeholder="Choose from the options")
            chai = drink
            if chai:
                st.write(f"Awesome! You've chosen {chai}")
                sugar_level = st.slider("Sugar level(Tea Spoons):",0,5,1)
                cups = st.number_input("How many cups?",min_value=1,max_value=10,step=1)
            
        elif variant == "Fusion & Fun":
            drink = st.selectbox("Choose your chai:", fusion_fun_chai, index=None, placeholder="Choose from the options")
            chai = drink
            if chai:
                st.write(f"Awesome! You've chosen {chai}")
                sugar_level = st.slider("Sugar level(Tea Spoons):",0,5,1)
                cups = st.number_input("How many cups?",min_value=1,max_value=10,step=1)

        

#End of Chai, coffee will be the next part

    if choice == "Coffee":
        coffee_type = ["Classic Coffee", "Milk based", "Dessert & Specialty Coffee", "Healthy / Low Caffeine Options", "Strong / Premium Brews"]
        variant = st.selectbox("Choose your type of coffee:", coffee_type, index=None, placeholder="Choose from the options")

#Coffee types
        coffee = None
        if variant == "Classic Coffee":
            classic_coffee = ["Espresso","Americano","Filter Coffee","Black Coffee"]
            drink = st.selectbox("Choose your coffee:",classic_coffee, index=None, placeholder="Select one")
            coffee = drink
            if coffee:
                st.write(f"Awesome! You've chosen {coffee}")
                sugar_level = st.slider("Sugar level(Tea Spoons):",0,5,1)
                cups = st.number_input("How many cups?",min_value=1,max_value=10,step=1)

        if variant == "Milk based":
            milk_based_coffee = ["Cappuccino","Latte","Flat White","Mocha"]
            drink = st.selectbox("Choose your coffee:",milk_based_coffee, index=None, placeholder="Select one")
            coffee = drink
            if coffee:
                st.write(f"Awesome! You've chosen {coffee}")
                sugar_level = st.slider("Sugar level(Tea Spoons):",0,5,1)
                cups = st.number_input("How many cups?",min_value=1,max_value=10,step=1)

        if variant == "Dessert & Specialty Coffee":
            dessert_specialty_coffee = ["Affogato","Irish Coffee","Caramel Macchiato","Vanilla Latte","Hazelnut Coffee"]
            drink = st.selectbox("Choose your coffee:",dessert_specialty_coffee, index=None, placeholder="Select one")
            coffee = drink
            if coffee:
                st.write(f"Awesome! You've chosen {coffee}")
                sugar_level = st.slider("Sugar level(Tea Spoons):",0,5,1)
                cups = st.number_input("How many cups?",min_value=1,max_value=10,step=1)

        if variant == "Healthy / Low Caffeine Options":
            healthy_coffee = ["Decaf Coffee","Chicory Coffee","Bulletproof Coffee"]
            drink = st.selectbox("Choose your coffee:", healthy_coffee, index=None, placeholder="Select one")
            coffee = drink
            if coffee:
                st.write(f"Awesome! You've chosen {coffee}")
                sugar_level = st.slider("Sugar level(Tea Spoons):",0,5,1)
                cups = st.number_input("How many cups?",min_value=1,max_value=10,step=1)

        if variant == "Strong / Premium Brews":
            premium_strong_coffee = ["Double Espresso","Ristretto","Turkish Coffee", "Cold Brew"]
            drink = st.selectbox("Choose your coffee:", premium_strong_coffee, index=None, placeholder="Select one")
            coffee = drink
            if coffee:
                st.write(f"Awesome! You've chosen {coffee}")
                sugar_level = st.slider("Sugar level(Tea Spoons):",0,5,1)
                cups = st.number_input("How many cups?",min_value=1,max_value=10,step=1)

#coffee done
    bt = st.button("Submit")

    if bt:
        if (chai or coffee) and cups is not None:
            selected_item = chai or coffee

            price_row = menu_df[menu_df["Item"] == selected_item]

            if price_row.empty:
                st.error("Price not found for selected item.")
            else:
                unit_price = price_row["Price_INR"].values[0]
                total_price = unit_price * cups

                order_data = {
                    "Customer Name": name,
                    "Gender": gender,
                    "City Name": city,
                    "Branch Name": branch,
                    "Drink Type": choice,
                    "Choice": selected_item,
                    "Cups Number": cups,
                    "Unit Price": unit_price,
                    "Total Revenue": total_price,
                    "Order Placed": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                df = pd.DataFrame([order_data])

                file_path = "data/orders.csv"

                if os.path.exists(file_path):
                    df.to_csv(file_path, mode="a", header=False, index=False)
                else:
                    df.to_csv(file_path, index=False)

                st.success(
                    f"Your {selected_item} is being brewed "
                    f"({cups} cups, ₹{total_price}) ☕"
                )
                st.write("***Thank you for visiting us***")
        else:
            st.error("Please complete your order before submitting.")

        

