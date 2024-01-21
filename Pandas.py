import pandas as pd

# data = { "Name":['Razzaq','Ali','Ahmed'],
#          "Age":[20,21,22],
#          "Salary":[500000,200000,100000]
#          }

# df = pd.DataFrame(data)
# print(df)






data = pd.read_csv("Hotel Reservations.csv")

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

print(data.duplicated().head(5))


