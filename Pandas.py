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

import pandas as pd 
data = pd.read_excel("ESD.xlsx")
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







