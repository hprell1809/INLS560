# Data taken from: https://goheels.com/sports/mens-basketball/roster
import pandas as pd

roster = ["Claude", "Brown", "Cadeau", "Davis", "Tyson", "Davis", "Trimble", "Powell", "Jackson", "Washington", "Hawkins"]
player = {"Last Name": roster}
data = pd.DataFrame(roster)
print(data)