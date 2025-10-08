"""
Archivo que representa la ventana principal que lleva a las ventanas de
inventario, historial de tickets, punto de venta
"""

#importación de librerías
import tkinter as tk

#inicialización y configuración de frameHome
homeFrame = tk.Tk()
homeFrame.geometry("500x500")

inventoryButton = tk.Button(homeFrame, text = "Inventario").grid(row = 1, column = 1)
tiketHistoriesButton = tk.Button(homeFrame, text = "Historial de tikets").grid(row = 2, column = 1)
salesButton = tk.Button(homeFrame, text = "Punto de Venta").grid(row = 3, column = 1)
homeFrame.mainloop()
