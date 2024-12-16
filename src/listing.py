import os
import datetime
import shutil


#Create Dataset
def create_dataset(rawdata_path, dataset_path):
    print(rawdata_path+"  "+dataset_path)
    if os.path.exists(dataset_path):
        print("Dataset already present, removing old one")
        shutil.rmtree(dataset_path)
        shutil.copytree(rawdata_path, dataset_path)
    else:
        print("Dataset dosen't exists, creating new one")
        shutil.copytree(rawdata_path, dataset_path)
    dataset = [dataset for dataset in os.listdir(dataset_path) if dataset.endswith(".csv")]
    return dataset

#Get file date's
def get_creation_date(rawdata_path, dataset):
    for f in dataset:
        file = os.path.join(rawdata_path, f)
        creation_timestamp = os.path.getctime(file)
        creation_date = datetime.datetime.fromtimestamp(creation_timestamp).strftime('%Y-%m-%d')
        return creation_date
