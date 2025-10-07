import tkinter as tk
from tkinter import ttk
#a
#inicialización y configuración de frameHome
homeFrame = tk.Tk()
homeFrame.geometry("500x500")

#configuración de la disposición de la ventana
frameLayout = tk.ttk.Frame(homeFrame, padding = 10)
frameLayout.grid()

inventoryButton = tk.Button(homeFrame, text = "Inventario").grid(row = 1, column = 1)
tiketHistoriesButton = tk.Button(homeFrame, text = "Historial de tikets").grid(row = 2, column = 1)
salesButton = tk.Button(homeFrame, text = "Punto de Venta").grid(row = 3, column = 1)
homeFrame.mainloop()
