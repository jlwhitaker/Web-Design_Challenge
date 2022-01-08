import pandas as pd

df = pd.read_csv("cities.csv")

df.to_html(open("cities.html", "w"))


