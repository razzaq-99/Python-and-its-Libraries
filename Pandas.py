import pandas as pd

# data = { "Name":['Razzaq','Ali','Ahmed'],
#          "Age":[20,21,22],
#          "Salary":[500000,200000,100000]
#          }

# df = pd.DataFrame(data)
# print(df)






# data = pd.read_csv("Hotel Reservations.csv")


# print(data.to_string())
# print(data.head(10))
# print(data.tail(10))
# print(data.info())
# print(data.describe())
# print(data.isnull().sum())



                                              # Handling Duplicate values

# print(data["no_of_adults"].duplicated().head(10))    


# print(data.duplicated())

# print(data.duplicated().sum())

# print(data["Booking_ID"].drop_duplicates())

# print(data["Booking_ID"].duplicated().head(5))

# print(data.duplicated().tail(10))

# x = data.drop_duplicates("Booking_ID")
# print(x.duplicated().head(5))
# print(x.duplicated().sum())

# print(data.duplicated().head(5))






                                     # Working with Null Values



# x = {
#     "name":["Ali","Ahmed","Shera","Kazim","Meer","Ahad"],
#     "Age":[12,33,44,55,22,],
#     "Salary":"",
#     "City":""
# }


# df = pd.DataFrame(x)
# print(df)

# print(df.isnull())



# import pandas as pd
# data = pd.read_csv("hotel_bookings.csv")
# print(data.to_string())
# print(data.head(10))
# data = data["company"].dropna()
# print(data.isnull().sum())



# print(data["children"].isnull().sum())

# print(data["children"].tail(10))


# x = (data.fillna("30000000000"))
# print(x)
# print(x.isnull().sum())

# print(data["company"].fillna("HR").head(5))       # replace first 5 null vales with HR








                                             # Column Transformations/ making new column from existing columns

# import pandas as pd 
# data = pd.read_excel("ESD.xlsx")
# print(data)


# data.loc[(data["Bonus %"] == 0), "GetBonus"] = "no bonus"
# data.loc[(data["Bonus %"] > 0), "GetBonus"] = "bonus"

# print(data.head(10))



# data.loc[(data["Country"] == "China"), "Budget"] = "50 %"
# data.loc[(data["Country"] == "United States"), "Budget"] = "HIGH"

# print(data.head(10))
# print(data.tail(10))


       # making one column from two existing columns
# data["Location"] = data["City"] +", "+ data["Country"]

# print(data)


# data["New Bonus"] = (data["Annual Salary"]/100)*20

# print(data.head(10))


# x = {"Months":["November","October","August","December"]}

# df = pd.DataFrame(x)
# # print(df)

 
# def extract(value):
#     return value[0:3] 


# df["    months_shortcut"] = df["Months"].map(extract)

# print(df)






# x = {"Date":["12-12-2001","23-10-2010","04-03-2004","16-06-2003","21-08-2015"]}

# df = pd.DataFrame(x)

# print(df)

# def extract(value):
#     return value[0:2]

# df["  Day"] = df["Date"].map(extract)


# def extract(value):
#     return value[3:5]

# df["  Month"] = df["Date"].map(extract)


# def extract(value):
#     return value[6:]

# df["  Year"] = df["Date"].map(extract)



# print(df)








# x = {"Full Date":["12-12-2001","23-10-2010","04-03-2004","16-06-2003","21-08-2015"]}

# df = pd.DataFrame(x)

# print(df)

# def extract(value,start,end):
#     return value[start,end]

# df["  Day"] = df["Full Date"].map(lambda x: extract[0,2])
# df["  Month"] = df["Full Date"].map(lambda x: extract[3,5])
# df["  Year"] = df["Full Date"].map(lambda x: extract[6,10])

# def extract(value):
#     return value[3:5]

# df["  Month"] = df["Full Date"].map(extract)


# def extract(value):
#     return value[6:]

# df["  Year"] = df["Full Date"].map(extract)



# print(df)










                                                    # Group By in Pandas

# import pandas as pd
# data = pd.read_excel("ESD.xlsx")

# print(data.head(10))


# gp = data.groupby("Department").agg({"Gender":"count"})
# print(gp)


# gp = data.groupby("Job Title").agg({"Gender":"count"})
# print(gp)


# gp = data.groupby("Country").agg({"City":"count"})
# print(gp)


# gp = data.groupby(["Department","Gender"]).agg({"EEID":"count"})
# print(gp)


# gp = data.groupby("Country").agg({"Age":"mean"})
# print(gp)


# gp = data.groupby("Country").agg({"Age":"sum"})
# print(gp)

# gp = data.groupby("Country").agg({"Annual Salary":"sum"})
# print(gp)

# gp = data.groupby("Country").agg({"Annual Salary":"count"})
# print(gp)


# gp = data.groupby("Country").agg({"Annual Salary":"max"})
# print(gp)


# gp = data.groupby("Country").agg({"Annual Salary":"min"})
# print(gp)


# gp = data.groupby("Country").agg({"Bonus %":"max"})
# print(gp)


# gp = data.groupby("Department").agg({"Annual Salary":"count"})
# print(gp)



# gp = data.groupby(["Country","City","Gender"]).agg({"Annual Salary":"max","Age":"max"})
# print(gp)


 
 
 
 
 
 
 
 
 
                                     # Merge , Join and Concatenate in Pandas
                                     
# import pandas as pd 

# data1 = {"EmpID":["E1","E2","E3","E4","E5"],
#        "Names":["Ali","Ahmed","Razzaq","Umair","Iqra"],
#        "Age":[23,21,19,43,77]
#        }

# data2 = {"EmpID":["E1","E2","E6","E8","E5"],
#        "salary":[23000,45000,33400,12000,10000]}

# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)


# print(df1)
# print(df2)

# print(pd.merge(df1,df2, on = "EmpID"))        # merging two dataset based on one Common Column (EmpID).



# print(pd.merge(df1,df2,how="right"))
# print(pd.merge(df1,df2,how="cross"))
# print(pd.merge(df1,df2,how="inner"))
# print(pd.merge(df1,df2,how="left"))
# print(pd.merge(df1,df2,how="outer"))


# print(pd.concat([df1,df2]))





                            
                            
                                      # Compare DataFrames
                                      
# import pandas as pd
# data = {"Fruits":["mango","Apple","Banana","Lemon"],
#         "Price":[120,140,100,200],
#         "Quantity":[10,8,15,50]}

# df1 = pd.DataFrame(data)
# print(df1)



# df2 = df1.copy()
# df2.loc[0,"Price"] = 500
# df2.loc[1,"Price"] = 200
# df2.loc[2,"Price"] = 150
# df2.loc[3,"Price"] = 250

# print()

# df2.loc[0,"Quantity"] = 15
# df2.loc[1,"Quantity"] = 13
# df2.loc[2,"Quantity"] = 20
# df2.loc[3,"Quantity"] = 80

# print(df2)

# print(df1.compare(df2))                                            # It compare exact changes occurance
# print(df1.compare(df2,keep_shape=True))







                                                      # Pivoting , Melting in Pandas 
     
# dict = {"keys":["key1","key2","key1","key2"],
#         "Names":["Jone","Micheal","David","Josh"],
#         "Houses":["Black","Red","Blue","Black"],
#         "Grades":["A+","A","B+","C"]}


# df = pd.DataFrame(dict)

# print(df)

# print()

# print(df.pivot(index="keys",columns="Names",values="Houses"))
# print(df.pivot(index="keys",columns="Names",values=["Houses","Grades"]))







# dict = {"Names":["Jone","Micheal","David","Josh"],
#         "Houses":["Black","Red","Blue","Black"],
#         "Grades":["A+","A","B+","C"]}

# df = pd.DataFrame(dict)

# print(df)

# print()

# print(pd.melt(df,id_vars=["Names"],value_vars=["Grades"]))

# print()

# print(pd.melt(df,id_vars=["Names"],value_vars=["Houses"]))




# import pandas as pd
# print(pd.options.display.max_rows)                              # display number of rows to be shown


# pd.options.display.max_rows = 9999                              # Increase the maximum number of rows to display the entire DataFrame:
# print(pd.options.display.max_rows)           


                                                       # IF the data is very large and you want to remove wrong added value

import pandas as pd
x = {"Name":["Ali","Ahmed","Raza"],"Age":[18,38,128]}
df = pd.DataFrame(x)
print(df)
for y in df.index:
  if df.loc[y, "Age"] > 120:
    df.drop(y, inplace = True)
    
print(df)    