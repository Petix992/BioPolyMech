from folderSelector import FolderSelectorApp
import tkinter as tk
import listing
import extraction


def main():
    #Select rawdata folder
    root = tk.Tk()
    selector = FolderSelectorApp(root)
    root.mainloop()
    rawdata_path = getattr(selector, "selected_folder", None)
    dataset_path = rawdata_path + "/dataset/"

    #Create dataset
    dataset = listing.create_dataset(rawdata_path, dataset_path)
    extraction.remove_dirty_strings(dataset_path, dataset)
    extraction.enrich_dataset(dataset_path, rawdata_path, dataset)

if __name__ == "__main__":
    
    main()