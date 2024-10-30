#here we are going to be given a padas dataframe of products that are both lowfat and recycable from an array.
import pandas as pd

data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype({'product_id':'int64', 'low_fats':'category', 'recyclable':'category'})

#We first select the rows 'low_fats' and 'recycable'
df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
#this creates a second dataframe of just low fast and recycable
#now we simply need to pull the product_id column to narrow down to the right column
df2 = df[['product_id']]

#after this we can simply run a sql query to return everything
# SELECT
#     product_id
# FROM
#     Products
# WHERE
#     low_fats = 'Y' AND recyclable = 'Y'