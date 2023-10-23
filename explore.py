#=====================================================================
# https://www.geeksforgeeks.org/python-introduction-matplotlib/
# https://www.geeksforgeeks.org/matplotlib-tutorial/
# https://www.geeksforgeeks.org/how-to-plot-a-pandas-dataframe-with-matplotlib/
# https://stackoverflow.com/questions/34280444/python-scatter-plot-with-multiple-y-values-for-each-x
#=====================================================================
from matplotlib import pyplot as plt
import pandas as pd


#pd.set_option('display.max_colwidth', None)
df = pd.read_csv('../../Downloads/train.csv/train.csv')
df = df.loc[df["stock_id"]==0].head(100)
print(df)
#df.to_csv("stock_id_0_first_100.csv")


#print(df.head(50000).where(df["stock_id"]==0).head(100))









