import tkinter as tk
#TODO: simplify the importing of libraries
from GUI.utils. import *
from GUI.frames. import *

#objects
wController = WindowsController()
hf = HomeFrame(tk.Tk(), "500x500", "home")

#Example: oppening homeFrame
wController.openWindow(hf)
