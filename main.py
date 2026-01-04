import pandas as pd

#Fetch Data

file_path = "Data_sets/workforce_database.xlsx"
xls = pd.ExcelFile(file_path)

df = pd.read_excel(file_path, sheet_name="1. England", skiprows=9)

print(df.head(20))

#Store data

df.to_csv("nhs_staffing_raw.csv", index=True)

#Clean data



#Organise data and transform it 



#Bottleneck detection - look for the problems



#Trend analysis