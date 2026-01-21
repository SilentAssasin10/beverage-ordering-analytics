# ☕ Chai & Coffee Ordering and Analytics App

A multi-page **Streamlit application** for managing beverage orders and analyzing sales data.  
The project focuses on **correct data handling, aggregation logic, and time-based analytics**, rather than UI gimmicks.

---

## 📌 Project Overview

This application simulates a real-world chai & coffee business with:
- CSV-driven menu pricing
- Order placement with validation
- A structured analytics dashboard with KPIs and trends

The goal of the project is to demonstrate **applied data analytics, dashboard design, and debugging of real data issues**.

---

## 🗂️ Project Structure

├── Home.py # Landing page
├── pages/
│ ├── 1_Menu.py # Menu display (menu.csv)
│ ├── 2_Order.py # Order placement (writes to orders.csv)
│ └── 3_Dashboard.py # Overview + Analytics dashboard
├── data/
│ ├── menu.csv # Single source of truth for prices
│ └── orders.csv # Order history
├── assets/
│ └── logo.png
└── README.md


---

## 📊 Dashboard Design

The dashboard is intentionally split into two logical sections:

### 🔹 Overview
High-level business summary:
- Total Revenue
- Total Orders
- Cups Sold
- Best-Selling Item
- Monthly Revenue Trend
- Recent Buyers (latest 5 orders)

This section answers:
> **“How is the business doing at a glance?”**

---

### 🔹 Analytics
Detailed breakdowns:
- Chai vs Coffee comparison
- Top-selling items
- Revenue by city
- Orders by branch
- Time-of-day analysis using **time buckets**

This section answers:
> **“Why are these numbers the way they are?”**

---

## ⏰ Time-of-Day Bucketing

Instead of using raw timestamps, orders are grouped into meaningful time buckets:

- Midnight
- Dawn
- Morning
- Noon
- Afternoon
- Evening
- Night

This improves interpretability and reflects how real business analytics are performed.

---

## 🧠 Key Technical Concepts Used

- CSV as immutable raw data source
- Derived columns created dynamically in pandas
- Correct use of `groupby → aggregate → sort → select`
- Explicit datetime parsing and validation
- Session state for view switching
- Defensive handling of invalid timestamps
- Separation of **summary vs analysis**

---

## 🐞 Real Bug Debugged (Important)

During development, a real issue was encountered where:
- New orders were not appearing in the “Recent Buyers” list

**Root cause:**
- Sample data contained *future-dated timestamps*, so new orders placed “today” were correctly ranked as older.

**Fix:**
- Normalized test data and enforced consistent datetime parsing.

This reinforced the importance of **data correctness over UI assumptions**.

---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install streamlit (Pandas come with streamlit by default)

2. Open terminal, go to the project and then run

    streamlit run Home.py

Thanking You for visiting this project
