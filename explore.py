#=====================================================================
# https://www.geeksforgeeks.org/python-introduction-matplotlib/
# https://www.geeksforgeeks.org/matplotlib-tutorial/
# https://www.geeksforgeeks.org/how-to-plot-a-pandas-dataframe-with-matplotlib/
# https://stackoverflow.com/questions/34280444/python-scatter-plot-with-multiple-y-values-for-each-x
#=====================================================================
from matplotlib import pyplot as plt
import pandas as pd



def f1():
  df = pd.read_csv('../../Downloads/train.csv/train.csv')
  df2 = df[df.stock_id == 0].head(100)
  df2.to_csv("stock_id_0_first_100.csv")

def f2():
  df = pd.read_csv('stock_id_0_first_100.csv')
  plt.scatter(x=range(100), y=df['reference_price'])
  plt.scatter(x=range(100), y=df['wap'])
  plt.show()





