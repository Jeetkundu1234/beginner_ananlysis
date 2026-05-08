
import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Country": ["India", "USA", "Brazil", "Russia", "Japan"],
    "Cases": [45000000, 103000000, 37000000, 22000000, 33000000],
    "Deaths": [530000, 1120000, 700000, 390000, 74000]
}


df = pd.DataFrame(data)


df.index = range(1, len(df) + 1)


print("\n========== COVID-19 DATA ANALYSIS ==========\n")

print(df)


total_cases = df["Cases"].sum()
total_deaths = df["Deaths"].sum()

print("\nTotal Cases =", total_cases)
print("Total Deaths =", total_deaths)


highest = df.loc[df["Cases"].idxmax()]

print("\nCountry With Highest Cases:")
print(highest["Country"])


plt.figure(figsize=(8,5))

plt.bar(df["Country"], df["Cases"])

plt.title("COVID-19 Cases By Country")
plt.xlabel("Country")
plt.ylabel("Cases")

plt.show()