import pandas as pd

from matplotlib import pyplot as plt
x=[1,2,3]
y=[1,4,9]
z=[10,5,0]

plt.plot(x,y)
plt.plot(x,z)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["this is x", "this is y"])
plt.show()
sample_data=pd.read_csv("sample_data.csv")
print(type(sample_data))
print(type(sample_data.column.c))
