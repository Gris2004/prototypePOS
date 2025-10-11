import tkinter as tk

class SalesPointFrame:
    """SalesPointFrame representa a la ventana de punto de venta
    atributos:
        frame: es el atributo que almacena al objeto tk.Tk()
        geometry: atributo que almacena un string que define el tamaño del frame
        title: atributo que almacena un string que define el título del frame

    métodos:
        __init__: es el constructor de la clase SalesPointFrame
        showSalesPoint: es la función que muestra el frame con su disposición y configuración inicial"""
    
    def __init__(self, frame, geometry, title):
        """constructor de la clase SalesPointFrame"""
        self.frame = frame
        self.geometry = geometry
        self.title = title

    def showSalesPointFrame(self):
        """muestra el frame de SalesPointFrame con su configuración y disposición inicial"""
        self.frame = tk.Tk()
        self.frame.geometry(self.geometry)
        self.frame.title(self.title)

        self.frame.mainloop()

