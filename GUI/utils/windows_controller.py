import tkinter as tk
from tkinter import messagebox

class WindowsController:
    """WindowController is a class that controls the frames with some functions to be imported to other frames
    and use its functions
    
    methods:
        openWindow: opens a new window when this function is called
        destructionDetect: detects when the user closes a window and sends a message or returns to home_frame"""

    def openWindow(self, geometry, title, window):
        window.setup()
        window.frame.mainloop()

    def destructionDetect(self, frame):
        """it detects when the user closes the window and open the welcome window"""
        close = messagebox.askyesno(
                message = "¿estás seguro de que quieeres cerrar la ventana?",
                title = "Confirmación de Cierre",
                icon = "info"
                )
        if close:
            #checking the window closure
            frame.destroy()
