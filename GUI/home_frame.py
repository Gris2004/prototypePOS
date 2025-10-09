#importación de librerías
import tkinter as tk

class HomeFrame:
    def __init__(self, frame, geometry):
        self.frame = frame
        self.geometry = geometry

    def showHomeFrame(self):
        self.frame.geometry(self.geometry)
        
        inventoryButton = tk.Button(self.frame, text = "Inventario").grid(row = 1, column = 1)
        tiketHistoriesButton = tk.Button(self.frame, text = "Historial de tikets").grid(row = 2, column = 1)
        salesButton = tk.Button(self.frame, text = "Punto de Venta").grid(row = 3, column = 1)
        self.frame.mainloop()

#inicialización y configuración de frameHome
frame = tk.Tk()
home = HomeFrame(frame, "500x500")
home.showHomeFrame()
