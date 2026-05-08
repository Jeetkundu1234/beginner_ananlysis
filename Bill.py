import pandas as pd
cart = []

while True:

    name = input("Enter product name (Type done to finish): ")

    if name.lower() == "done":
        break

    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))

    total = price * qty

    cart.append([name, price, qty, total])

df = pd.DataFrame(
    cart,
    columns=["Product", "Price", "Qty", "Total"]
)
df.index = range(1, len(df) + 1)

print("\n------ BILL ------")
print(df)

grand_total = df["Total"].sum()
print("\nGrand Total =", grand_total)