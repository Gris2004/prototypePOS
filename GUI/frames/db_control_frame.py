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

    def setupDBControlFrame(self):
        """showDBControlFrame es la función que muestra el frame con su configuración y disposición inicial""" 
        self.frame.geometry(self.geometry)
        self.frame.title(self.title)

if __name__ == "__main__":
    genericFrame = tk.Tk()
    dbcFrame = DBControlFrame(genericFrame, "500x500", "Control de Base de Datos")
    dbcFrame.setupDBControlFrame()
    dbcFrame.frame.mainloop()
