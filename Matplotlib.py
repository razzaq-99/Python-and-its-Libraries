
                                                                 # BAR PLOT

# import pandas as pd
# import matplotlib.pyplot as plt

# y = [99,70,97,66,23,44]
# x = ["Part1","Part2","Part3","Part4","Part5","Part6"]
# colors = ["red","green","orange","blue","yellow","red"]



# plt.bar(x,y,color = "orange")
# plt.bar(x,y,color = colors,)
# plt.bar(x,y,color = colors,edgecolor="black")
# plt.xlabel("Parts of Harry Potter ",fontsize = 18)
# plt.ylabel("Popularity",fontsize = 18)
# plt.title("Popularity of Harry Potter",fontsize = 18)
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# data = pd.read_excel("expense3.xlsx")



# df = pd.DataFrame(data)
# print(df)

# df["Payment Mode"] = df["Payment Mode"].astype(str)
# plt.bar(df["Payment Mode"],df["Amount"])
# plt.show()



# dfx = df.groupby("Payment Mode")["Amount"].sum()
# print(df)

# plt.xlabel("Payment Methods",fontsize = 17)
# plt.ylabel("Amount",fontsize = 17)
# plt.title("Payment Methods vs Amount",fontsize = 20)
# colors = ["red","green","orange","blue"]
# plt.bar(dfx.index,dfx.values,color = colors)
# plt.show()


# df["Category"] = df["Category"].astype(str)

# dfx = df.groupby("Category")["Amount"].sum()
# print(dfx)


# plt.xlabel("Category")
# plt.ylabel("Amount")
# plt.title("Category vs Amount")
# plt.bar(df["Category"],df["Amount"])
# plt.bar(dfx.index,dfx.values)
# plt.show()




                                                               # LINE PLOT
                                                               
# import matplotlib.pyplot as plt
# x = ["day1","day2","day3","day4","day5","day6"]
# y = [100,400,120,330,20,200]
# z = [200,500,40,250,0,400]
# z1 = [400,600,350,100,50,30]


# # plt.plot(x,y)
# # plt.plot(x,y,marker="*")
# plt.plot(x,y,marker = "^",ls ="--",color="red",label="week1")
# plt.plot(x,z,marker = "^",ls ="--",color="blue",label="week2")
# plt.plot(x,z1,marker = "^",ls ="-",color="green",label="week3")
# plt.legend()
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt

# data = pd.read_excel("expense3.xlsx")
# df = pd.DataFrame(data)
# print(df)


# df["Payment Mode"] = df["Payment Mode"].astype(str)
# df["Amount"] = df["Amount"].astype(str)
# df["Category"] = df["Category"].astype(str)
# df["Payment Mode"] = df["Payment Mode"].astype(str)
# df["Date"] = df["Date"].astype(str)


# dfx1 = df.groupby("Category")["Amount"].sum()
# dfx2 = df.groupby("Payment Mode")["Amount"].sum()
# dfx3 = df.groupby("Date")["Amount"].sum()


# print(dfx1)
# print(dfx2)
# print(dfx3)


# plt.plot(df["Category"],df["Amount"])
# plt.plot(dfx1.index,dfx1.values,marker="^",label ="Annual bills")
# plt.plot(dfx2.index,dfx2.values,marker = "^",label="Payment Methods",color = "red")
# plt.plot(dfx3.index,dfx3.values,marker="^",label="Every date amount",color="green")

# plt.legend()
# plt.show()





                                           # SCATTER PLOT
# import matplotlib.pyplot as plt
# import numpy as np
# import Pandas as pd


# x = np.random.randint(1,100,70)
# y = np.random.randint(10,100,70)
# colors = np.random.randint(10,100,70)

# plt.scatter(x,y,marker="*",cmap="rainbow",c = colors,)
# plt.scatter(x,y,marker="*",cmap="twilight",c = colors,)
# plt.colorbar()
# plt.show()





# Plotting from DataSet

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_excel("ESD.xlsx")

df = pd.DataFrame(data)
# print(df.to_string)
# color = np.random.randint(low=None,high=None)

# plt.scatter(df["Age"],df["Bonus %"])
# plt.title("Age wise Employees Bonus")
# plt.xlabel("Age")
# plt.ylabel("Bonus %")
# plt.show()
# print(df.to_string)

  
  
  
# plt.scatter(df["Annual Salary"],df["Gender"])
plt.scatter(df["Country"],df["Annual Salary"])
plt.show()