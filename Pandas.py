import pandas as pd

data = { "Name":['Razzaq','Ali','Ahmed'],
         "Age":[20,21,22],
         "Salary":[500000,200000,100000]
         }

df = pd.DataFrame(data)
print(df)