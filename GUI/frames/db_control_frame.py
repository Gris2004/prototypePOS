import tkinter as tk

class DBControlFrame:
    """DBControlFrame representa a la ventana de control de base de datos o inventario
    atributos:
        frame: es la variable que almacena el objeto tk.Tk()
        geometry: es la variable que almacena un string que define la geometría del frame
        title: es la variable que almacena un string que define el título del frame

    métodos:
        __init__: es el constructor de la clase DBControlFrame
        showDBControlFrame: es la función que muestra el frame con su configuración y disposición inicial"""
    
    def __init__(self, frame, geometry, title):
        """__init__ es el constructor de la clase DBControlFrame"""
        self.frame = frame
        self.geometry = geometry
        self.title = title

    def showDBControlFrame(self):
        """showDBControlFrame es la función que muestra el frame con su configuración y disposición inicial"""
        self.frame = tk.Tk()
        self.frame.geometry(self.geometry)
        self.frame.title(self.title)

        self.frame.mainloop
