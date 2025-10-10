#importación de librerías
import tkinter as tk
from tikets_frame import TiketsFrame
from inventory_frame import InventoryFrame

class HomeFrame:
    def __init__(self, frame, geometry, title):
        self.frame = frame
        self.geometry = geometry
        self.title = title
    
    def callNewFrame(self, name):
        """Llama a un frame existente por su nombre"""
        #DEUDA TÉCNICA: Encontrar una forma de automatizar esta función sin necesidad de usar if's
        genericFrame = 0
        if (name == "tikets"):
            tikets = TiketsFrame(genericFrame, "500x500", "Historial de Tikets")
            tikets.showTiketsFrame()
        if (name == "inventory"):
            inventory = InventoryFrame(genericFrame, "500x500", "Inventario")
            inventory.showInventoryFrame()

    def showHomeFrame(self):
        #inicialización del frame principal con sus elementos necesarios
        self.frame = tk.Tk()
        self.frame.geometry(self.geometry)
        self.frame.title(self.title)

        inventoryButton = tk.Button(self.frame, text = "Inventario", command = self.callNewFrame("inventory")).grid(row = 1, column = 1)
        tiketHistoriesButton = tk.Button(self.frame, text = "Historial de tikets", command = self.callNewFrame("tikets")).grid(row = 2, column = 1)
        salesButton = tk.Button(self.frame, text = "Punto de Venta").grid(row = 3, column = 1)
        self.frame.mainloop()

#inicialización y configuración de frameHome
home_frame = 0
home = HomeFrame(home_frame, "500x500", "Ventana Inicial")
home.showHomeFrame()
