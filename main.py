import tkinter as tk
from ui import FinanceTrackerGUI
from storage import Storage
from config import DATA_FILE

def main():
    root = tk.Tk()
    storage = Storage(DATA_FILE)
    app = FinanceTrackerGUI(root, storage)
    root.mainloop()

if __name__ == "__main__":
    main()
