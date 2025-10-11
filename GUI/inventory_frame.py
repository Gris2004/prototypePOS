import tkinter as tk

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

    def showInventoryFrame(self):
        """es la función que muestra el frame con su disposición y configuración iniciales"""
        self.frame = tk.Tk()
        self.frame.geometry(self.geometry)
        self.frame.title(self.title)

        self.frame.mainloop()
