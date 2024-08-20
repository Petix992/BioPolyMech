import pandas as pd
import numpy as np
import fileinput
import os
import datetime
import listing

df_all = pd.DataFrame()


#Removing dirty string
for f in listing.dataset: 
    with fileinput.FileInput(listing.dataset_path+f, inplace=True) as file:
        for line in file:
            print(line.replace("Results Table 1", ""), end='')

#Create Dataframe with all informations
for f in listing.dataset:
    df = pd.read_csv(listing.dataset_path+f)
    df = df.iloc[1:-2, 1:]
    df['Experiment Date'] = listing.get_creation_date(f)
    df['Filename'] = f
    df_all = df_all._append(df, ignore_index=True)

#Removing "," from Modulus (Young's Tensile stress - Cursor)
df_all["Modulus (Young's Tensile stress - Cursor)"] = df_all["Modulus (Young's Tensile stress - Cursor)"].str.replace(',', '')

# Print the DataFrame
print(df_all)

#Converting in float 
df_dataset = df_all.iloc[:, :-2].astype(float)

df_all.iloc[:, :4] = df_all.iloc[:, :4].astype(float)


print(df_dataset)

#Filtering for range
#df_dataset = df_dataset[df_dataset["Modulus (Young's Tensile stress - Cursor)"].between(700, 900)]

#print(df_all)



