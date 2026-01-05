import pandas as pd

#-----Fetch Data----------------

#database1
file_path = "Data_sets/workforce_database.xlsx"
xls = pd.ExcelFile(file_path)
db1 = pd.read_excel(file_path, sheet_name="1. England", skiprows=9)

#Database2
db2 = "clean_db/RTT_NHS.csv"

#-----Store data----------------

input_file = "Data_sets/RTT_NHS.csv"
output_file = "clean_db/RTT_NHS_cleaned.csv"

# Load full dataset
df = pd.read_csv(input_file)

# Keep essential identifier columns
id_cols = [
    "Period",
    "Provider Org Name",
    "RTT Part Type",
    "RTT Part Description",
    "Treatment Function Name"
]

# Identify all waiting time columns
week_cols = [c for c in df.columns if c.startswith("Gt")]

# Helper to extract start week number
def get_week_start(col):
    if "Weeks SUM" in col:
        return int(col.split()[1])
    if "104 Weeks" in col:
        return 104
    return None

# Create week mapping
week_map = {c: get_week_start(c) for c in week_cols}

# Define buckets
bucket_0_18 = [c for c, w in week_map.items() if w is not None and w <= 18]
bucket_19_26 = [c for c, w in week_map.items() if 19 <= w <= 26]
bucket_27_52 = [c for c, w in week_map.items() if 27 <= w <= 52]
bucket_52_plus = [c for c, w in week_map.items() if w > 52]

# Create new bucketed columns
df["Wait_0_18_weeks"] = df[bucket_0_18].sum(axis=1)
df["Wait_19_26_weeks"] = df[bucket_19_26].sum(axis=1)
df["Wait_27_52_weeks"] = df[bucket_27_52].sum(axis=1)
df["Wait_52_plus_weeks"] = df[bucket_52_plus].sum(axis=1)

# Final clean dataset
final_df = df[id_cols + [
    "Wait_0_18_weeks",
    "Wait_19_26_weeks",
    "Wait_27_52_weeks",
    "Wait_52_plus_weeks"
]]

# Save
final_df.to_csv(output_file, index=False)



print("Bucketed waiting list data saved.")

#-----Organise data and transform it -----------------



#-----Bottleneck detection - look for the problems--------



#Trend analysis