import pandas as pd

# data = { "Name":['Razzaq','Ali','Ahmed'],
#          "Age":[20,21,22],
#          "Salary":[500000,200000,100000]
#          }

# df = pd.DataFrame(data)
# print(df)






# data = pd.read_csv("Hotel Reservations.csv")


# print(data)
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




# data = pd.read_csv("hotel_bookings.csv")

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

import pandas as pd
data = pd.read_excel("ESD.xlsx")

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


