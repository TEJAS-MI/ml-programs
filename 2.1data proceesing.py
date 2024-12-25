import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\91914\Desktop\python\example.xlsx")

df_filled_mean = df.copy()

print(df.head())

for column in df.columns:
    col_data = df[column]

    if pd.api.types.is_numeric_dtype(col_data):
        mean_value = col_data.mean()
        df_filled_mean[column] = df[column].fillna(mean_value)
    else:
        mode_value = col_data.mode()[0]
        df_filled_mean[column] = df[column].fillna(mode_value)

print("\nData with missing values filled:")
print(df_filled_mean)