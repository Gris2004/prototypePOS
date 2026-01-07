import tkinter as tk
import sys
sys.path.append('../utils/')
from windows_controller import WindowsController

class HomeFrame:
    """HomeFrame es la clase que representa a la ventana principal
    atributos:
        frame: es el atributo guarda el valor del objeto tk.Tk()
        geometry: es el atributo que guarda el string que representa el tamaño del frame
        : es el atributo que guarda el string que representa el título del frame

    métodos:
        __init__: es el constructor de la clase HomeFrame
        callNewFrame: llama a un frame existente por su nombre
        showHomeFrame: muestra el frame principal con la configuración y disposición iniciales"""
    
    def __init__(self, frame, geometry, title):
        """__init__ es el constructor de la clase HomeFrame"""
        self.frame = frame
        self.geometry = geometry
        self.title = title

    def setup(self):
        """show_home_frame es la función que muestra el frame con su disposición y configuración inicial"""
        self.frame.geometry(self.geometry)
        self.frame.title(self.title)

        inventoryButton = tk.Button(self.frame, text="Inventario")
        inventoryButton.grid(row=1, column=1)

        tiketHistoriesButton = tk.Button(self.frame, text="Historial de tikets")
        tiketHistoriesButton.grid(row=2, column=1)

        salesButton = tk.Button(self.frame, text="Punto de Venta")
        salesButton.grid(row=3, column=1) 

        #protocol in case that the user closes the window
        wController = WindowsController()
        self.frame.protocol('WM_DELETE_WINDOW', lambda: wController.destructionDetect(self.frame))

if __name__ == "__main__":
    genericFrame = tk.Tk()
    home = HomeFrame(genericFrame, "500x500", "ventana principal")
    home.setup()
    home.frame.mainloop()
