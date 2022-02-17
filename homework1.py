import pandas as pd

print("Type full path to text file:")
file = input()

f = open(file, "r")
characters = pd.Index(list(f.read()))

stats = characters.value_counts()

print("Order by frequency/alphabet? Type f/a:")

order = input()
if order == "a":
    stats = stats.sort_index(ascending=True)

f = open("output.txt", "w")
f.write(str(stats))
f.close()

print("Data saved to 'output.txt'")
