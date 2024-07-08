
class Catalogo:
    productos = []
    
    def agregar_producto(self, codigo, descripcion, cantidad, precio, imagen, proveedor):
        # Verificamos la existencia del producto
        if self.consultar_producto(codigo): # Si encontraste el producto ...
            return False #... salí de la función
        
        nuevo_producto = { # Generamos un diccionario con los datos del producto
            'codigo': codigo,
            'descripcion': descripcion,
            'cantidad': cantidad,
            'precio': precio,
            'imagen': imagen,
            'proveedor': proveedor
        }
        self.productos.append(nuevo_producto)
        return True # Confirmación de que el producto se agregó ok

    def consultar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                return producto
        return False # indica que el producto no se encontró

    # Modificar un producto (update)

    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                producto['descripcion'] = nueva_descripcion
                producto['cantidad'] = nueva_cantidad
                producto['precio'] = nuevo_precio
                producto['imagen'] = nueva_imagen
                producto['proveedor'] = nuevo_proveedor
                return True
        return False # Cuando el producto no fue encontrado

    # Listar productos (read)
    def listar_productos(self):
        print("*" * 50)
        for producto in self.productos:
            print(f'Código.......: {producto['codigo']}')
            print(f'Descripción..: {producto['descripcion']}')
            print(f'Cantidad.....: {producto['cantidad']}')
            print(f'Precio.......: {producto['precio']}')
            print(f'Imagen.......: {producto['imagen']}')
            print(f'Proveedor....: {producto['proveedor']}')
            print("*" * 50)

    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                self.productos.remove(producto)
                return True
        return False

    def mostrar_producto(self, codigo):
        producto = self.consultar_producto(codigo)
        if producto:
            print("*" * 50)
            print(f'Código.......: {producto['codigo']}')
            print(f'Descripción..: {producto['descripcion']}')
            print(f'Cantidad.....: {producto['cantidad']}')
            print(f'Precio.......: {producto['precio']}')
            print(f'Imagen.......: {producto['imagen']}')
            print(f'Proveedor....: {producto['proveedor']}')
            print("*" * 50)
        else:
            print(f'El producto {codigo} no existe')
            
# -------------------------------------------------------------------
# Programa principal
# -------------------------------------------------------------------
print("\033[H\033[J")  # Limpiamos la pantalla

catalogo = Catalogo() # cada catalogo es una tienda

# Agregamos y consultamos productos
catalogo.agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500, 'teclado.jpg', 101)
catalogo.agregar_producto(2, 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)
catalogo.agregar_producto(3, 'Monitor LCD 22 pulgadas', 15, 52500, 'monitor22.jpg', 103)
catalogo.agregar_producto(4, 'Monitor LCD 27 pulgadas', 25, 78500, 'monitor27.jpg', 104)
catalogo.agregar_producto(5, 'Pad mouse', 5, 500, 'padmouse.jpg', 105)

print("*--------------------------------------*")
print(catalogo.consultar_producto(1))

catalogo.modificar_producto(1, 'Teclado PS2 101 teclas', 8, 45000, 'tecladoPS2.jpg', 103)
print(catalogo.consultar_producto(1))

print("*--------------------------------------*")
catalogo.listar_productos()

print("*--------------------------------------*")
print("Eliminamos el producto con Código 3")
catalogo.eliminar_producto(3)
print("*--------------------------------------*")
catalogo.listar_productos()

print("*--------------------------------------*")
catalogo.mostrar_producto(2)

