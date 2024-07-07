# -------------------------------------------------------------------
# VER PDF EN DRIVE PARA HACER SEGUIMIENTO DEL PROYECTO
# Escribimos una serie de funciones para crear una pequeña app que
# maneje un arreglo que contenga datos de productos.
#
# Nuestras funciones harán lo siguiente:
#
# - Agregar un producto al arreglo
# - Consultar un producto a partir de su código
# - Modificar los datos de un producto a partir de su código
# - Obtener un listado de los productos que existen en el arreglo.
# - Eliminar un producto de la lista
#
# Cada producto tiene:
#
# - codigo: int, código numérico del producto.
# - descripcion: str, descripción alfabética del producto.
# - cantidad: int, cantidad en stock del producto.
# - precio: float, precio de venta del producto.
# - imagen: str, nombre de la imagen del producto.
# - proveedor: int, número de proveedor del producto.
# -------------------------------------------------------------------
# { 'cod' : 1, 'desc': "Mouse 3 botones", 'cantidad': 34}


# productos = [
    # { 'cod' : 1, 'desc': "Mouse 3 botones", 'cantidad': 34, 'codigo': 1},
    # { 'cod' : 1, 'desc': "Mouse 3 botones", 'cantidad': 34, 'codigo': 2},
    # { 'cod' : 1, 'desc': "Mouse 3 botones", 'cantidad': 34, 'codigo': 3},
    # { 'cod' : 1, 'desc': "Mouse 3 botones", 'cantidad': 34, 'codigo': 4}]


# Definimos una lista de diccionarios
productos = []

# -------------------------------------------------------------------
# Funcion que añade un producto a la lista
# -------------------------------------------------------------------

def agregar_producto(codigo, descripcion, cantidad, precio, imagen, proveedor):
    
    # Verificamos la existencia del producto
    if consultar_producto(codigo): # Si encontraste el producto ...
        print("El producto ya existe por ende no se agrega.")
        return False #... salí de la función
    
    nuevo_producto = { # Generamos un diccionario con los datos del producto
        'codigo': codigo,
        'descripcion': descripcion,
        'cantidad': cantidad,
        'precio': precio,
        'imagen': imagen,
        'proveedor': proveedor
    }
    productos.append(nuevo_producto)
    return True # Confirmación de que el producto se agregó ok


# -------------------------------------------------------------------
# Funcion que devuelve los datos de un producto
# -------------------------------------------------------------------
def consultar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            return producto
    return False # indica que el producto no se encontró
            

# -------------------------------------------------------------------
# Funcion que modifica un producto
# -------------------------------------------------------------------
def modificar_producto(codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
    for producto in productos:
        if producto['codigo'] == codigo:
            producto['descripcion'] = nueva_descripcion
            producto['cantidad'] = nueva_cantidad
            producto['precio'] = nuevo_precio
            producto['imagen'] = nueva_imagen
            producto['proveedor'] = nuevo_proveedor
            return True
    return False # Cuando el producto no fue encontrado
            
# -------------------------------------------------------------------
# Funcion lista los productos
# -------------------------------------------------------------------
def listar_productos():
    print("*" * 50)
    for producto in productos:
        print(f'Código.......: {producto['codigo']}')
        print(f'Descripción..: {producto['descripcion']}')
        print(f'Cantidad.....: {producto['cantidad']}')
        print(f'Precio.......: {producto['precio']}')
        print(f'Imagen.......: {producto['imagen']}')
        print(f'Proveedor....: {producto['proveedor']}')
        print("*" * 50)

# -------------------------------------------------------------------
# Funcion eliminar un producto
# -------------------------------------------------------------------
def eliminar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            productos.remove(producto)
            return True
    return False
        
        
        
        
# -------------------------------------------------------------------
# Programa principal
# -------------------------------------------------------------------

print("\033[H\033[J")  # Limpiamos la pantalla


# AGREGAMOS PRODUCTOS
agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500, 'teclado.jpg', 101)
agregar_producto(2, 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)
agregar_producto(3, 'Monitor LCD 22 pulgadas', 15, 52500, 'monitor22.jpg', 103)
agregar_producto(4, 'Monitor LCD 27 pulgadas', 25, 78500, 'monitor27.jpg', 104)
agregar_producto(5, 'Pad mouse', 5, 500, 'padmouse.jpg', 105)
agregar_producto(6, 'Pad mouse', 5, 500, 'padmouse.jpg', 105)


print(consultar_producto(3))
modificar_producto(3, 'Monitor LCD 24 pulgadas', 20, 60000, 'monitor24.jpg', 104)
print(consultar_producto(3))

print("--------Vamos a eliminar----------")
eliminar_producto(3)
print(consultar_producto(3))
listar_productos()

