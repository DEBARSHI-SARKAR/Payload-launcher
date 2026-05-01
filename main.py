import tkinter as tk
from tkinter import ttk
from cell import pcell
import json
import os

SAVE_FILE = "data.json"


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Payload Launcher")
        self.root.geometry("450x800")

        # Top bar
        tk.Button(root, text="+ Add Cell", command=self.add_cell).pack(fill="x")

        # Scroll system
        self.canvas = tk.Canvas(root)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.container = tk.Frame(self.canvas)

        self.container.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.container, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.cells = []

        self.load()

    def add_cell(self, data=None):
        cell = pcell(self.container, data=data,
                     on_delete=self.remove_cell,
                     on_update=self.save)
        self.cells.append(cell)
        self.save()

    def remove_cell(self, cell):
        self.cells.remove(cell)
        self.save()

    def save(self):
        data = []
        for c in self.cells:
            data.append({
                "name": c.name.get(),
                "ip_last": c.ip_last.get(),
                "port": c.port_entry.get(),
                "file": c.file_path
            })

        with open(SAVE_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        if not os.path.exists(SAVE_FILE):
            return

        with open(SAVE_FILE, "r") as f:
            data = json.load(f)

        for cell_data in data:
            self.add_cell(cell_data)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
