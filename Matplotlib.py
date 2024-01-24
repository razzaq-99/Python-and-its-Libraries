
                                                                 # Bar plot

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


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("expense3.xlsx")


# print(df)
df = pd.DataFrame(data)
df["Payment Mode"] = df["Payment Mode"].astype(str)
# plt.bar(df["Payment Mode"],df["Amount"])
# plt.show()



dfx = df.groupby("Payment Mode")["Amount"].sum()
# print(dfx)

plt.xlabel("Payment Methods",fontsize = 17)
plt.ylabel("Amount",fontsize = 17)
plt.title("Payment Methods vs Amount",fontsize = 20)

plt.bar(dfx.index,dfx.values)
plt.show()