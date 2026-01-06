import tkinter as tk
import sys
sys.path.append('../utils/')
from windows_controller import WindowsController

#clase de TiketsFrame
class TiketsFrame:
    """clase que representa la ventana de historial de tickets
    atributos:
        frame: atributo que almacena el objeto tk.Tk(
        geometry: atributo que almacena el string que representa el tamaño del frame
        title: atributo que almacena el string que representa el título del frame

    métodos:
        __init__ es el constructor de la clase TiketsFrame
        showTiketsFrame es la función que muestra el frame con la configuración y disposición iniciales"""
    
    def __init__(self, frame, geometry, title):
        """__init__ es el constructor de la clase TiketsFrame"""
        self.frame = frame
        self.geometry = geometry
        self.title = title
    
    #función para crear motrar la ventana
    def setupTiketsFrame(self):
        """showTiketsFrame es la función que muestra el frame con la configuración y disposición iniciales"""
        self.frame.geometry(self.geometry)
        self.frame.title(self.title)

        #protocol in case that the user closes the window
        wController = WindowsController()
        self.frame.protocol("WM_DELETE_WINDOW", lambda: wController.destructionDetect(self.frame))

if __name__ == "__main__":
    genericFrame = tk.Tk()
    tikets = TiketsFrame(genericFrame, "500x500", "Historial de Tikets")
    tikets.setupTiketsFrame()
    tikets.frame.mainloop()
