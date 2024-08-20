import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import folderSelector

if __name__ == "__main__":
    root = tk.Tk()
    choice = folderSelector.FolderSelectorApp(root)
    root.mainloop()
