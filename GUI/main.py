import tkinter as tk
from frames.home_frame import HomeFrame
from utils.windows_controller import WindowsController

wController = WindowController()
wController.openWindow("500x500", "ventana principal", HomeFrame(lambda: tk.Tk(), geometry, title))
