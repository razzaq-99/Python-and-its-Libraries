
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

# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd


# data = pd.read_excel("ESD.xlsx")

# df = pd.DataFrame(data)
# print(df.to_string)
# color = np.random.randint(low=None,high=None)

# plt.scatter(df["Age"],df["Bonus %"])
# plt.title("Age wise Employees Bonus")
# plt.xlabel("Age")
# plt.ylabel("Bonus %")
# plt.show()
# print(df.to_string)

  
  
  
# plt.scatter(df["Annual Salary"],df["Gender"])
# plt.scatter(df["Country"],df["Annual Salary"])
# plt.show()







                                                   
                                                         # PIE CHART 
# import matplotlib.pyplot as plt


# brands = ["Oneplus","Apple","Oppo","Vivo","Infinix"]
# price = [60000,120000,30000,25000]
# popularity = [25,75,35,30,50]       
# colors = ["Green","Silver","orange","red","blue"]
# ex = [0,0,0,0.09,0]


# plt.pie(popularity,labels=brands,colors=colors,explode=ex,autopct="%.2f",startangle=90)
# plt.show()




# chart from DataSet


# import matplotlib.pyplot as plt 
# import pandas as pd 

# data = pd.read_excel("expense3.xlsx")

# df = pd.DataFrame(data)

# df["Payment Mode"] = df["Payment Mode"].astype(str)
# dfx = df.groupby("Payment Mode")["Amount"].sum()
# ex = [0,0.1,0,0]


# plt.pie(df["Amount"],labels=df["Category"],autopct="%.2f")
# plt.pie(dfx.values,labels=dfx.index,autopct="%.2f",explode=ex,startangle=90)

# plt.pie()

# plt.show()
# print(df)







                              # BOX PLOT
import matplotlib.pyplot as plt        
import pandas as pd
# data = [12,44,23,66,34,88,62,99,12,45,1,10,99]
# x = [33,12,44,53,24,55,9,1,4,6,7]

# plt.boxplot(data)
# plt.boxplot(x)

# plt_values = [data,x]
# plt.boxplot(plt_values)
# plt.xlabel("plots")
# plt.ylabel("Data")
# plt.show()





# plotting from dataset

# data = pd.read_excel("ESD.xlsx")
# df = pd.DataFrame(data)
# print(df.head(10))
# plt_values = [df["Annual Salary"],df["Bonus %"]]

# plt.boxplot(df["Annual Salary"])
# plt.boxplot(plt_values)

# plt.title("Annual Salary of Emplyees")
# plt.show()











                                           # Histogram
# import matplotlib.pyplot as plt

# data1 = [23,31,55,63,8,23,33,81,4,26,34,5,2]
# data2 = [120,140,160,180]
# data3 = [92,94,99,110]

# plt.hist(data,bins=50)
# plt.hist(data1,bins=len(data1),edgecolor="black",color="orange")
# plt.hist(data2,bins=len(data2),edgecolor="black",color="orange")

# plt.hist(data,bins='auto',edgecolor="black",color="orange")

# plt.hist([data1,data2,data3],bins='auto')
# plt.xlabel('Value',fontsize=15)
# plt.ylabel('Frequency',fontsize=15)

# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)


# plt.show()

                                                         
                                                         
                                                         
                                                         
                                                        # Plotting data from DataSet
# import matplotlib.pyplot as plt 
# import pandas as pd         

# data = pd.read_excel("ESD.xlsx")
# df = pd.DataFrame(data) 

# dfx = df.groupby("Gender")["Annual Salary"].sum()

# plt.hist(df["Annual Salary"],bins='auto')    

# plt.hist(df["Bonus %"],bins='auto',edgecolor="black",align='mid',color="orange")                

# plt.show()                          










 # Violin Plot Matplotlib 
 
# import matplotlib.pyplot as plt 

# x = [71,1,80,45,85,50,15,59,90,99,98,69,99]
# y = [39,20,10,40,12,44,38,6,17,18,28,30,60,99]
# plt.violinplot(x)
# plt.violinplot(x,showmedians=True)
# plt.violinplot(x,showextrema=True)
# plt.violinplot(x,showmeans=True,points=100,positions=[13])

# plt_values = [x,y]

# plt.violinplot(plt_values)

# plt.show()




# DataSET plotting

# import matplotlib.pyplot as plt 
# import pandas as pd 

# data = pd.read_excel("ESD.xlsx")

# df = pd.DataFrame(data)

# print(df.head(10))

# plt_values = [df["Bonus %"],df["Age"]]

# plt.violinplot(plt_values)

# plt.violinplot(df["Annual Salary"],showmedians=True)
  

# plt.show()



                                              
                                              
                                                 # STEM PLOT 
import matplotlib.pyplot as plt 
import pandas as pd 

# data = [20,30,40,50,60,70,80,90,99,90,80,70,60,50,40,30,20] 


# plt.stem(data,linefmt="--",markerfmt="^",bottom=0,orientation="vertical")

# plt.xlabel("Values")
# plt.ylabel("Range")

# plt.show()
                                    




# plotting DataSet

data = pd.read_excel("ESD.xlsx")

df = pd.DataFrame(data) 

df2 = df.head(50)

# plt.stem(df2["Age"],bottom=10)  
plt.stem(df2["Annual Salary"]) 
plt.title("Annual Salary of Employees",fontsize=20)
plt.xlabel("No: of Employees",fontsize=15)
plt.ylabel("Annual Salary",fontsize=15)
plt.show()                                