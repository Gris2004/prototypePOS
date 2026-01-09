import tkinter as tk
import sys
from GUI.utils.windows_controller import WindowsController

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

    def setup(self):
        """es la función que muestra el frame con su disposición y configuración iniciales"""
        self.frame.geometry(self.geometry)
        self.frame.title(self.title)

        #protocol in case that the user closes the window
        wController = WindowsController()
        self.frame.protocol("WM_DELETE_WINDOW", lambda: wController.destructionDetect(self.frame))

if __name__ == "__main__":
    genericFrame = tk.Tk()
    inventory = InventoryFrame(genericFrame, "500x500", "Ventana de Inventario")
    inventory.setup()
    inventory.frame.mainloop()
  
