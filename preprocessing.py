# mittul rungta 
# final year project 

# this python script reads the raw data and then preprocesses it
# and then save the preprocessed data to a parquet file 


import pandas as pd
import os
import glob

# Get a list of all CSV files in a directory
csv_files = glob.glob('/Users/mittulrungta/Desktop/Year3/FinalYP/fwlmb11wni392kodtyljkw4n2/files_csv/*.csv')


# Create an empty dataframe to store the combined data
dfs = []

# Loop through each CSV file and append its contents to the combined dataframe
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    dfs.append(df)

# Pconcatenate the dataframes 
final_df = pd.concat(dfs, ignore_index=False)

#convert the time column to pandas datetime
final_df["Time"] = pd.to_datetime(final_df["Time"], unit="s")

#since the time were not in order sort the coulmn by time 
df_timesort = final_df.sort_values(by="Time")

#only selected device D out of the 8 devices 
df_devicesort = final_df[final_df["DeviceId"] == "D"]

# Rename columns for consistency
df_devicesort.columns = ["timestamp", "DeviceId", "Sensor", "Value"]

# Convert timestamp to datetime
df_devicesort["timestamp"] = pd.to_datetime(df_devicesort["timestamp"])

# Use pivot_table to reshape data while handling duplicate timestamps
df_pivot = df_devicesort.pivot_table(index="timestamp", columns="Sensor", values="Value", aggfunc="mean")

# Reset index to save properly
df_pivot.reset_index(inplace=True)

df_pivot.to_parquet("final_data.parquet")