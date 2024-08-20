import os
import datetime
import shutil
import main 

#Rawdata path input from user - then dataset path is radatapath + /dataset/
#rawdata_path = input("Enter the path of the rawdata: ")
rawdata_path = main.choice
dataset_path = rawdata_path+"/dataset/"

#Copy the rawdata in dataset dir
if os.path.exists(dataset_path):
    shutil.rmtree(dataset_path)
shutil.copytree(rawdata_path, dataset_path)

dataset = [dataset for dataset in os.listdir(dataset_path) if dataset.endswith(".csv")]


def get_creation_date(file):
    for f in dataset:
        file = os.path.join(rawdata_path, f)
        creation_timestamp = os.path.getctime(file)
        creation_date = datetime.datetime.fromtimestamp(creation_timestamp).strftime('\n%Y-%m-%d')
        return creation_date
