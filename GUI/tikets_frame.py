import tkinter as tk

#clase de ticketFrameClass
class TiketsFrameClass:
    #función de constructor
    def __init__(self, frame):
        self.frame = frame
    
    #función para crear motrar la ventana
    def showFrame(self):
        self.frame.mainloop()

tiketFrame = tk.Tk()
frameObject = TiketsFrameClass(tiketFrame)
frameObject.showFrame()
