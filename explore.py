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

  df0 = df[df.stock_id == 0].head(100)
  df0.to_csv("sample/stock_id_0_first_100.csv")

  df1 = df[df.stock_id == 1].head(100)
  df1.to_csv("sample/stock_id_1_first_100.csv")
  
  df2 = df[df.stock_id == 2].head(100)
  df2.to_csv("sample/stock_id_2_first_100.csv")


def f2():
  df0 = pd.read_csv('sample/stock_id_0_first_100.csv').head(9)
  df1 = pd.read_csv('sample/stock_id_1_first_100.csv').head(9)
  df2 = pd.read_csv('sample/stock_id_2_first_100.csv').head(9)

  plt.scatter(x=range(9), y=df0['reference_price'])
  plt.scatter(x=range(9), y=df1['reference_price'])
  plt.scatter(x=range(9), y=df2['reference_price'])
  #plt.scatter(x=range(100), y=df['wap'])

  plt.show()

#f1()
f2()
