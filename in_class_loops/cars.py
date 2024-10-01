# This is a list, a string is different and trickier
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.capitalize())

fridge = ['apples', 'blueberries', 'strawberries', 'cantalope']
for fruit in fridge:
    if fruit == "strawberries":
        print(fruit.title()) 
    else:
        print(fruit.upper()) 