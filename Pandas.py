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
print(data.isnull().sum())
