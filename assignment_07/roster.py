# Data taken from: https://goheels.com/sports/mens-basketball/roster
import pandas as pd

player = {"Last Name": ["Claude", "Brown", "Cadeau", "Davis", "Tyson", "Davis", "Trimble", "Powell", "Jackson", "Washington", "Hawkins"],
          "First Name": ["Ty", "James", "Elliot", "RJ", "Cade", "Elijah", "Seth", "Drake", "Ian", "Jalen", "Russell"],
          "Height": [79, 80, 73, 72, 79, 75, 75, 78, 76, 82, 73],
          "Weight": [230, 215, 180, 180, 200, 215, 195, 195, 190, 235, 175]}

data = pd.DataFrame(player)

# BMI = weight in kg/height in meters squared
data["BMI"] = (data["Weight"]/2.205)/((data["Height"]/39.37)**2)

# Round the BMI column to 2 decimal places
data["BMI"] = data["BMI"].round(2)

print(data)

data.to_csv("BMI.csv")