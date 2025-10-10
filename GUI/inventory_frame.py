import tkinter as tk

class InventoryFrame:
    def __init__(self, frame, geometry, title):
        self.frame = frame
        self.geometry = geometry
        self.title = title

    def showInventoryFrame(self):
        self.frame = tk.Tk()
        self.frame.geometry(self.geometry)
        self.frame.title(self.title)

        self.frame.mainloop()
