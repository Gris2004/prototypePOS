import tkinter as tk
#TODO: simplify the importing of libraries
from GUI.utils.windows_controller import WindowsController
from GUI.frames.db_control_frame import DBControlFrame
from GUI.frames.home_frame import HomeFrame
from GUI.frames.inventory_frame import InventoryFrame
from GUI.frames.sales_point_frame import SalesPointFrame
from GUI.frames.tikets_frame import TiketsFrame

#objects
windowsController = WindowsController()

#opening homeFrame
windowsController.openWindow(HomeFrame(lambda: tk.Tk(), "500x500", "main window"))
