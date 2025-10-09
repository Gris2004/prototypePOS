import tkinter as tk

#clase de ticketFrameClass
class TiketsFrameClass:
    """clase que representa la ventana de historial de tickets
    atributos:
        frame ? variable que almacena función tk.Tk()"""
    #función de constructor
    def __init__(self, frame):
        self.frame = frame
    
    #función para crear motrar la ventana
    def showFrame(self):
        self.frame.mainloop()
