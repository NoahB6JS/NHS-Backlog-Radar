import pandas as pd

#Fetch Data

file_path = "Data_sets/workforce_database.xlsx"
xls = pd.ExcelFile(file_path)
df = pd.read_excel(file_path, sheet_name="1. England", skiprows=9)
print(df.head(20))

#Store data

df.fillna(0, inplace=True) 
df.to_csv("nhs_staffing.csv", index=True)

#Clean data

 # replace empty cells with 0

#Organise data and transform it 



#Bottleneck detection - look for the problems



#Trend analysis