import tkinter as tk
from tkinter import ttk

#inicialización y configuración de frameHome
homeFrame = tk.Tk()
homeFrame.geometry("500x500")

#configuración de la disposición de la ventana
frameLayout = tk.ttk.Frame(homeFrame, padding = 10)
frameLayout.grid()

homeFrame.mainloop()
