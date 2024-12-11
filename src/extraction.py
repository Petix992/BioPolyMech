import pandas as pd
import fileinput
import listing

#Removing dirty string
def remove_dirty_strings( dataset_path, dataset):
    for f in dataset: 
        with fileinput.FileInput(dataset_path+f, inplace=True) as file:
            for line in file:
                print(line.replace("Results Table 1", ""), end='')

#Create Dataframe with all informations
def enrich_dataset(dataset_path, rawdata_path ,dataset):
    enriched_dataset = pd.DataFrame()
    for f in dataset:
        df = pd.read_csv(dataset_path+f)
        df = df.iloc[1:-2, 1:]
        df['Experiment Date'] = listing.get_creation_date(rawdata_path, dataset)
        df['Filename'] = f
        enriched_dataset = enriched_dataset._append(df, ignore_index=True)
    #Removing "," from Modulus (Young's Tensile stress - Cursor) values
    enriched_dataset["Modulus (Young's Tensile stress - Cursor)"] = enriched_dataset["Modulus (Young's Tensile stress - Cursor)"].str.replace(',', '')
    print(enriched_dataset)
    return enriched_dataset

#Converting in float 
#df_dataset = enrich_dataset.iloc[:, :-2].astype(float)

#enrich_dataset.iloc[:, :4] = enrich_dataset.iloc[:, :4].astype(float)


#print(df_dataset)

#Filtering for range
#df_dataset = df_dataset[df_dataset["Modulus (Young's Tensile stress - Cursor)"].between(700, 900)]

#print(df_all)



