import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class FolderSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Select Folder")
        
        self.label = tk.Label(root, text="No folder selected")
        self.label.pack(pady=10)
        
        self.select_button = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=5)
        
        self.quit_button = tk.Button(root, text="Exit", command=root.quit)
        self.quit_button.pack(pady=5)
    
    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.label.config(text=f"Selected Folder: {folder_selected}")
            messagebox.showinfo("Selected Folder", f"You have selected: {folder_selected}")
        else:
            messagebox.showwarning("No folder Selected", "No Folder ave been Selected")
