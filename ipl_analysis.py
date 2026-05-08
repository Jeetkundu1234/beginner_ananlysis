import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Player": [
        "Virat Kohli",
        "Rohit Sharma",
        "MS Dhoni",
        "KL Rahul",
        "Shubman Gill"
    ],

    "Team": [
        "RCB",
        "MI",
        "CSK",
        "LSG",
        "GT"
    ],

    "Runs": [
        741,
        620,
        450,
        680,
        710
    ],

    "Matches": [
        15,
        14,
        14,
        15,
        15
    ],

    "Wins": [
        9,
        10,
        11,
        8,
        12
    ]
}

df = pd.DataFrame(data)

df.index = range(1, len(df) + 1)


print("\n========== IPL DATA ANALYSIS ==========\n")

print(df)


highest = df.loc[df["Runs"].idxmax()]

print("\nHighest Scorer:")
print(highest["Player"], "-", highest["Runs"], "Runs")

best_team = df.loc[df["Wins"].idxmax()]

print("\nBest Team:")
print(best_team["Team"])


df["Win %"] = (df["Wins"] / df["Matches"]) * 100

print("\nWin Percentage:\n")

print(df[["Team", "Win %"]])


print("\nPlayer Comparison:\n")

comparison = df[["Player", "Runs"]]

print(comparison)


plt.figure(figsize=(8,5))

plt.bar(df["Player"], df["Runs"])

plt.title("IPL Player Runs Comparison")
plt.xlabel("Players")
plt.ylabel("Runs")

plt.show()