import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Customer": [
        "Jeet",
        "Amit",
        "Rahul",
        "Jeet",
        "Amit",
        "Riya"
    ],
    "Product": [
        "Biscuit",
        "Cold Drink",
        "Chips",
        "Biscuit",
        "Chocolate",
        "Chips"
    ],

    "Quantity": [5, 3, 7, 2, 6, 4],
    "Price": [10, 40, 20, 10, 50, 20],

    "Month": [
        "January",
        "January",
        "February",
        "March",
        "March",
        "April"
    ]
}

df = pd.DataFrame(data)

df["Total"] = df["Quantity"] * df["Price"]

df.index = range(1, len(df) + 1)


print("\n========== BILLING ANALYSIS ==========\n")

print(df)

best_product = df.groupby("Product")["Quantity"].sum()

print("\nBest Selling Products:\n")
print(best_product)

customer_spending = df.groupby("Customer")["Total"].sum()

print("\nCustomer Spending:\n")
print(customer_spending)

monthly_income = df.groupby("Month")["Total"].sum()

print("\nMonthly Income:\n")
print(monthly_income)

avg_sales = df["Total"].mean()

prediction = avg_sales * 30

print("\nPredicted Next Month Sales =", prediction)


plt.figure(figsize=(8,5))

monthly_income.plot(kind="bar")

plt.title("Monthly Income Analysis")
plt.xlabel("Month")
plt.ylabel("Income")

plt.show()