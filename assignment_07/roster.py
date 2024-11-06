# Data taken from: https://goheels.com/sports/mens-basketball/roster
import pandas as pd

roster = ["Claude", "Brown", "Cadeau", "Davis", "Tyson", "Davis", "Trimble", "Powell", "Jackson", "Washington", "Hawkins"]
player = {"Last Name": roster,
          "First Name": ["Ty", "James", "Elliot", "RJ", "Cade", "Elijah", "Seth", "Drake", "Ian", "Jalen", "Russell"],
          "height": [79, 80, 73, 72, 79, 75, 75, 78, 76, 82, 73],
          "weight": [230, 215, 180, 180, 200, 215, 195, 195, 190, 235, 175]}
data = pd.DataFrame(player)
print(data)