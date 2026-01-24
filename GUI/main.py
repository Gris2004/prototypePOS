import tkinter as tk
#TODO: simplify the importing of libraries
from GUI.utils.windows_controller import *
from GUI.frames.home_frame import *;

#objects
wController = WindowsController()
hf = HomeFrame(tk.Tk(), "500x500", "home")

#Example: oppening homeFrame
wController.openWindow(hf)
