import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Sales Data Analysis Dashboard")

# ================= SAMPLE DATA =================

data = {
    "Product": ["Rice", "Wheat", "Sugar", "Rice", "Sugar", "Oil", "Wheat"],
    "Quantity": [10, 5, 8, 7, 6, 3, 4],
    "Price": [50, 40, 60, 50, 60, 120, 40],
    "Month": ["Jan", "Jan", "Jan", "Feb", "Feb", "Mar", "Mar"]
}

df = pd.DataFrame(data)

df["Total"] = df["Quantity"] * df["Price"]

# ================= SHOW DATA =================

st.subheader("📦 Sales Data")
st.dataframe(df)

# ================= TOTAL SALES =================

total_sales = df["Total"].sum()
st.subheader("💰 Total Sales")
st.success(total_sales)

# ================= BEST PRODUCT =================

best_product = df.groupby("Product")["Quantity"].sum()

st.subheader("🏆 Best Selling Products")
st.bar_chart(best_product)

# ================= MONTHLY SALES =================

monthly_sales = df.groupby("Month")["Total"].sum()

st.subheader("📅 Monthly Revenue")
st.bar_chart(monthly_sales)

# ================= PIE CHART =================

st.subheader("📊 Product Share")

fig, ax = plt.subplots()
best_product.plot(kind="pie", autopct="%1.1f%%", ax=ax)
st.pyplot(fig)