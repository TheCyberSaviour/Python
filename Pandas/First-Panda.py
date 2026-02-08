import pandas as pd

data = [(1, "Hello", 21, "M", "Space"),
        (2, "World", 20, "F", "Earth"),
        (3, "Cat", 19, "F", "Mars"),
        (4, "Dog", 18, "F", "Venus"),
        (5, "Mouse", 17, "F", "Gravity"), 
        (6, "Horse", 19, "F", "Newton"),
        (7, "Cow", 20, "F", "Milkyway"),
        (8, "Eagle", 21, "M", "Hollow")]

data = pd.DataFrame(data, columns=["ID", "Name", "Age", "Gender", "City"])

print(f"\n {data} \n")

