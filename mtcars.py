import pandas as p
import matplotlib.pyplot as m
import seaborn as s

# Read data
data = p.read_csv("mtcars.csv")

# Define variables
wt = data['wt']
mpg = data['mpg']  
iv = range(len(data))

# SCATTER
m.scatter(iv, mpg, color='k', label='mpg')
m.scatter(iv, wt, color='g', label='wt')
m.title("Relationship b/w Weight and MPG")
m.legend()
m.show()

# BAR PLOT
c = data['am'].value_counts()
co = ['k', 'g']
m.bar(c.index, c.values, color=co, width=0.3)
m.xticks([0, 1], ['0-Automatic', '1-Manual'])
m.xlabel("Transmission Type")
m.ylabel("Number of Cars")
m.title("Frequency distribution of transmission type of cars")
m.show()

# BOX PLOT
s.boxplot(x=mpg, color='c')  # Specify x=mpg
m.xlabel("MPG")
m.ylabel("Values")
m.title("Box Plot of MPG Values")
m.show()
