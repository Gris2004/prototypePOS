# INSTALACIÓN
existe un archivo llamado "installLibraries.bat" y pronto haré ajustes para que también pueda funcionar en linux con otro archivo si es necesario
por ahora, este sirve para hacer instalaciones necesrias para que funcione el programa

# YOU DONT HAVE POSTMAN?
i´m gonna develop a cli tool using curl for windows 

# CARACTERÍSTICAS A AGREGAR:
## GUI
- Hecha en python con tkinter
- Ventana de bienvenida
    - Botón de tickets
    - Botón de inventario
    - Botón de punto de venta
- Ventana de tickets
    - Tabla con el historial de tickets
    - Opción de eliminar un elemento del historial
    - Opción de modificar un elemento del historial
- Ventana de inventario
    - Al entrar pide solicitud a la API para la tabla de la base de datos desde el cliente (GUI)
    - Botones para ELIMINAR, AGREGAR y ACTUALIZAR (tanto cantidad de productos como otros datos) un registro
    - Botón para ver una ventana de estadísticas según el producto seleccionado
    - Tabla de la base de datos de inventario donde se pueda seleccionar el registro
    - Buscador de productos
    - celdas en color distintivo para cuando se rebase o iguala el límite de productos existentes
- Ventana de estadísticas
    - muestra cuantos productos se han vendido en el mes actual y los de los meses anteriores representados en una gráfica
    - el limite de meses es ajustable
    - Las estadísticas del producto se basan en el historial de tickets
- Ventana de base de datos
    - al elegir alguna opcion de la ventana de inventario que no sean las estadísticas, se abrirá una ventana pequeña de acorde
      a la opción seleccionada
- Ventana de punto de venta
    - panel de ticket que muestra los productos que el usuario va agregando
    - panel que muestra los productos en existencia
    - buscador de productos para ser agregados
    - Botón para generar ticket (lo manda al historial y lo vuelve pdf para luego preguntar si se quiere imprimir) y luego vacía
      la caja de productos donde se realiza la venta de los productos y se resta en existencias al igual que suma a los ingresos
    - vaciar el panel de tickets
## TICKET
- guardado en base de datos tabla historial
- se guardan tickets en una carpeta que se vacía cada ciertos pedidos
- productos comprados
- costo total
- fecha de ticket
- IVA
## API
- Hecha en node.js
- Endpoins para funciones de base de datos
- Endpoint para estadísticas sobre producto
- logs que se guardan cada 10 pedidos o transacciones
