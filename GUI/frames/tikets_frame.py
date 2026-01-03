import tkinter as tk

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
    def showTiketsFrame(self):
        """showTiketsFrame es la función que muestra el frame con la configuración y disposición iniciales"""
        self.frame = tk.Tk()
        self.frame.geometry(self.geometry)
        self.frame.title(self.title)
        self.frame.mainloop()
