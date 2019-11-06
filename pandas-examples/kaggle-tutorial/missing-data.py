import pandas as pd
import numpy as np

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 7)

print(reviews[reviews.country.isnull()])

print(reviews.region_2.fillna("Unknown"))
print(reviews.country.fillna("Unknown"))
