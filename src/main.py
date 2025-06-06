from folderSelector import FolderSelectorApp
import tkinter as tk
import listing
import extraction
import pandas as pd

#trend per nome file - EB aumenta TS diminuisce come anche YM

def main():
    #Select rawdata folder
    root = tk.Tk()
    selector = FolderSelectorApp(root)
    root.mainloop()
    rawdata_path = getattr(selector, "selected_folder", None)
    dataset_path = rawdata_path + "/dataset/"

    #Create dataset
    dataset = listing.create_dataset(rawdata_path, dataset_path)
    try:
        extraction.remove_dirty_strings(dataset_path, dataset)
        enriched_dataset = extraction.enrich_dataset(dataset_path, rawdata_path, dataset)
    except Exception as e:
        print(f"An error occurred while enriching the dataset: {e}")
    #Filter dataset

if __name__ == "__main__":
    
    main()