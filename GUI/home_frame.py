import tkinter as tk
from tikets_frame import TiketsFrame
from inventory_frame import InventoryFrame
from sales_point_frame import SalesPointFrame

class HomeFrame:
    """HomeFrame es la clase que representa a la ventana principal
    atributos:
        frame: es el atributo guarda el valor del objeto tk.Tk()
        geometry: es el atributo que guarda el string que representa el tamaño del frame
        title: es el atributo que guarda el string que representa el título del frame

    métodos:
        __init__: es el constructor de la clase HomeFrame
        callNewFrame: llama a un frame existente por su nombre
        showHomeFrame: muestra el frame principal con la configuración y disposición iniciales"""
    
    def __init__(self, frame, geometry, title):
        """__init__ es el constructor de la clase HomeFrame"""
        self.frame = frame
        self.geometry = geometry
        self.title = title

    def callNewFrame(self, name): 
        genericFrame = tk.Tk()
        """Llama a un frame existente por su nombre"""
        #DEUDA TÉCNICA: Buscar una mejor forma de hacer esta función
        if(name == "tikets"): 
            tiketsFrame = TiketsFrame(genericFrame, "500x500", "Historial de Tikets")
            tiketsFrame.showTiketsFrame()
            self.frame.destroy()
        elif(name == "inventory"):
            inventoryFrame = InventoryFrame(genericFrame, "500x500", "Inventario")
            inventoryFrame.showInventoryFrame()
            self.frame.destroy()
        elif(name == "sales"):
            salesPointFrame = SalesPointFrame(None, "500x500", "Punto de Venta")
            salesPointFrame.showSalesPointFrame()
            self.frame.destroy()
        else:
            print(f"No existe un frame con el nombre '{name}'")

    def showHomeFrame(self):
        """show_home_frame es la función que muestra el frame con su disposición y configuración inicial"""
        self.frame.geometry(self.geometry)
        self.frame.title(self.title)

        inventoryButton = tk.Button(self.frame, text="Inventario", command=lambda: self.callNewFrame("inventory"))
        inventoryButton.grid(row=1, column=1)

        tiketHistoriesButton = tk.Button(self.frame, text="Historial de tikets", command=lambda: self.callNewFrame("tikets"))
        tiketHistoriesButton.grid(row=2, column=1)

        salesButton = tk.Button(self.frame, text="Punto de Venta", command= lambda: self.callNewFrame("sales"))
        salesButton.grid(row=3, column=1)

if __name__ == "__main__":
    genericFrame = tk.Tk()
    home = HomeFrame(genericFrame, "500x500", "Ventana Principal")
    home.showHomeFrame()
    home.frame.mainloop()
