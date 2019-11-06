import pandas as pd
#df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
#	'Sue': ['Pretty good.', 'Bland.']},
#	index=['Product A', 'Product B'])
#print(df)


wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")
print(wine_reviews.shape)
print(wine_reviews.head())

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print(wine_reviews.head())