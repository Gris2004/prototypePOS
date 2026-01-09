import tkinter as tk
from utils.windows_controller import WindowsController

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

    def setup(self):
        """muestra el frame de SalesPointFrame con su configuración y disposición inicial""" 
        self.frame.geometry(self.geometry)
        self.frame.title(self.title)

        #protocol in case that the user closes the window
        wController = WindowsController()
        self.frame.protocol("WM_DELETE_WINDOW", lambda: wController.destructionDetect(self.frame))

if __name__ == "__main__":
    genericFrame = tk.Tk()
    spFrame = SalesPointFrame(genericFrame, "500x500", "Punto de Venta")
    spFrame.setup()
    spFrame.frame.mainloop()
