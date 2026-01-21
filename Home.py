import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Home", page_icon="🧋")

st.sidebar.image("assets/logo.png")
st.sidebar.markdown("""
    <h4 style='text-align:center; font-family: sans-seriff'>Always Online!</h4>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.block-container {
    padding-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

# Navbar
st.markdown("""
<style>
.navbar {
    display: flex;
    justify-content: center;
    gap: 40px;
    padding: 15px;
    background-color: #f5f0eb;
    border-radius: 12px;
    font-weight: bold;
}
.navbar a {
    text-decoration: none;
    color: #333;
}
</style>

<div class="navbar">
    <a href="#">Home</a>
    <a href="#">Menu</a>
    <a href="#">Order</a>
    <a href="#">Dashboard</a>
</div>
""", unsafe_allow_html=True)

#why use us
st.markdown("""
<style>
.use-card {
    background-color: #84DBA7;   /* latte color */
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.08);
}
.use-title {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 8px;
}
.use-text {
    font-size: 0.95rem;
    color: #444;
}
</style>
""", unsafe_allow_html=True)

#Hero section
st.markdown("""
<style>
.hero {
    background-image: url("https://imgs.search.brave.com/ai3JvR55bCvUALSX7uuc7d3lqxY9ziEWVnte-u8T92k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTE0/NTYxMjk1MS9waG90/by9ob3ctdG8tbWFr/ZS1jb2ZmZWUtbGF0/dGUtYXJ0LmpwZz9z/PTYxMng2MTImdz0w/Jms9MjAmYz1lV3lT/QTA2NnpEREtlQzNX/TjlXR2VrQnNna1Bn/OXRsVnF1VnRzd2xp/WF9jPQ");
    background-size: cover;
    background-position: center;
    padding: 80px 40px;
    border-radius: 15px;
    color: white;
    text-align: center;
    transparency: 50
}
.hero h1 {
    font-size: 3rem;
}
.hero p {
    font-size: 1.2rem;
}
</style>

<div class="hero">
    <h1>☕ Chai & Coffee Corner</h1>
    <p>Customize • Order • Analyze</p>
</div>
""", unsafe_allow_html=True)
st.text("\n")

#Why use our app
st.markdown("""
    <h2 style='text-align:center; font-weight: bold; font-size:3rem'>Why Use Our App</h2>
""",unsafe_allow_html=True)
st.text("\n")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="use-card">
        <div class="use-title" style='color: black'><b><i>☕ Deep Customization</i></b></div>
        <div class="use-text">
            Fine-grained control over drink type, variants, sugar, and add-ons.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="use-card">
        <div class="use-title" style='color: black'><b><i>🎯 End-to-End Experience</i></b></div>
        <div class="use-text">
            Customize drinks, place orders, and view analytics — all in one app.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="use-card">
        <div class="use-title" style='color: black'><b><i>📊 Built-in Analytics</i></b></div>
        <div class="use-text">
            Every order is saved and visualized through an interactive dashboard.
        </div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="use-card">
        <div class="use-title" style='color: black'><b><i>🏪 Multi-City & Branch Ready</i></b></div>
        <div class="use-text">City and branch-level tracking built into orders.</div>
    </div>
    """, unsafe_allow_html=True)

st.text("\n\n")

#Next section

st.write("\n\n")

st.markdown("""
    <h3 style='text-align:center; font-family: sans-serif; font-weight: bold; color: white'>How to Use</h3>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("**👋 Step 1: Get Started**")
    st.write("Enter your basic details like name, city, and branch to begin your ordering experience.")
with col2:
    st.subheader("**📖 Step 2: Explore Menu**")
    st.write("Discover different chai and coffee options with pricing, descriptions, health benefits.")
with col3:
    st.subheader("**☕ Step 3: Place Order**")
    st.write("Customize your drink by selecting variants and sugar levels, then submit your order with one click.")
with col4:
    st.subheader("**📈 Step 4: View Insights**")
    st.write("Check the analytics dashboard to see order history, trends, and performance across drinks and locations.")


components.html("""
<hr style="margin-top:60px; border:0.5px solid #444;">

<div style="text-align:center; color:#aaa; font-size:0.9rem;">

  <p>
    Brewed with care, powered by data ☕📊
  </p>

  <p >
    Built by <strong>Arkapravo Roy</strong>
  </p>

  <p>
    Python • Streamlit • Pandas
  </p>

  <p style="font-size:1rem; color:#777;">
    © 2026 | Chai & Coffee Ordering and Analytics App
  </p>
</div>
""", height=200)
