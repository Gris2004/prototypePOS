import tkinter as tk
from tikets_frame import TiketsFrame
from inventory_frame import InventoryFrame

class HomeFrame:
    def __init__(self, geometry="500x500", title="Ventana Inicial"):
        self.geometry = geometry
        self.title = title
        self.frame = None

        # Mapeo de nombres a clases de frames
        self.frames_map = {
            "tikets": (TiketsFrame, "500x500", "Historial de Tikets"),
            "inventory": (InventoryFrame, "500x500", "Inventario")
        }

    def call_new_frame(self, name):
        """Llama a un frame existente por su nombre"""
        frame_data = self.frames_map.get(name)
        if frame_data:
            frame_class, geometry, title = frame_data
            new_frame = frame_class(self.frame, geometry, title)
            # Llamar al método correspondiente según el tipo de frame
            if hasattr(new_frame, "showTiketsFrame"):
                new_frame.showTiketsFrame()
            elif hasattr(new_frame, "showInventoryFrame"):
                new_frame.showInventoryFrame()
        else:
            print(f"No existe un frame con el nombre '{name}'")

    def show_home_frame(self):
        """Inicializa la ventana principal y sus botones"""
        self.frame = tk.Tk()
        self.frame.geometry(self.geometry)
        self.frame.title(self.title)

        # Botones
        inventory_button = tk.Button(self.frame, text="Inventario", command=lambda: self.call_new_frame("inventory"))
        inventory_button.grid(row=1, column=1)

        tiket_histories_button = tk.Button(self.frame, text="Historial de tikets", command=lambda: self.call_new_frame("tikets"))
        tiket_histories_button.grid(row=2, column=1)

        sales_button = tk.Button(self.frame, text="Punto de Venta")
        sales_button.grid(row=3, column=1)

        self.frame.mainloop()


if __name__ == "__main__":
    home = HomeFrame()
    home.show_home_frame()

