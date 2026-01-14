import pandas as pd

#Load CSV
data = pd.read_csv("data/raw_data.csv")
original_rows = len(data)

#Remove rows with missing values
cleaned_data = data.dropna() # removes rows with ANY NaN
cleaned_rows = len(cleaned_data)

#Save cleaned CSV
cleaned_data.to_csv("data/cleaned_data.csv", index = False)

#Print summary
print(f"Original rows: {original_rows}")
print(f"Cleaned rows: {cleaned_rows}")
print("Data saved to cleaned_data.csv")