import tkinter as tk
from tkinter import messagebox

class InventoryFrame:
    """InventoryFrame es una clase que representa la ventana de inventario
    atributos:
        frame: es el atributo que almacena el objeto tk.Tk()
        geometry: es el atributo que almacena un string que representa el tamaño del frame
        title: es el atributo que almacena un string que representa el título del frame

    métodos:
        __init__ es el constructor de la clase InventoryFrame
        showInventoryFrame es la función que se encarga de mostrar el frame con su configuración y disposición iniciales"""

    def __init__(self, frame, geometry, title):
        """es el constructor de la clase InventoryFrame"""
        self.frame = frame
        self.geometry = geometry
        self.title = title

    def setupInventoryFrame(self):
        """es la función que muestra el frame con su disposición y configuración iniciales"""
        self.frame.geometry(self.geometry)
        self.frame.title(self.title)
        self.frame.protocol("WM_DELETE_WINDOW", self.destructionDetect)

    def destructionDetect(self):
        "it detects when the user closes the window and open the welcome window"
        close = messagebox.askyesno(
                message = "¿estás seguro de que quieres cerrar la aplicación?", 
                title = "Confirmación de Cierre",
                icon = "info"
                )
        if close:
            #checking the window closure
            self.frame.destroy()

if __name__ == "__main__":
    genericFrame = tk.Tk()
    inventory = InventoryFrame(genericFrame, "500x500", "Ventana de Inventario")
    inventory.setupInventoryFrame()
    inventory.frame.mainloop()
  
