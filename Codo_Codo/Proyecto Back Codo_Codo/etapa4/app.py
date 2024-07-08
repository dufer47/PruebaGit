#--------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify   # request captura los datos del formulario. jsonify convierte un diccionario en un JSON para luego enviarlo

# Instalar con pip install flask-cors
# Permite trabajar con todo lo que trabajemos desde distintos lugares. Hacemos una request desde un lugar que no es precisamente el servidor donde estoy alojado, por medidas de seguridad esto no esta permitido, por eso se debe habilitar el CORS (LINEA 21).
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename  # secure_filename es para darle seguridad al nombre de archivo

# No es necesario instalar, es parte del sistema standard de Python
import os   # Interactuar con el sistema operativo
import time # Obtener fecha y hora
#--------------------------------------------------------------------

app = Flask(__name__)
CORS(app)  # Esto habilitará las request de origen cruzado (CORS) a mi app, para todas las rutas
# Es decir desde afuera podemos hacer una consulta y dentro internamente podemos responderle al localhost, que es distinto al host que me esta haciendo la consulta y para evitar este tipo de advertencia o este tipo de inconvenientes, habilitamos CORS.

class Catalogo:
    #----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()
        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")  # Intenta conectarse usando el nombre de la base de datos que nos pasan como parámetro
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:  # errorcode.ER_BAD_DB_ERROR es un error de mysql que indica que la base de datos que nos pasan como parámetro no existe
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database    # Establecemos la base de datos actual
            else:
                raise err    # raise err: Lanza el error, corto el programa

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
            codigo INT AUTO_INCREMENT PRIMARY KEY,
            descripcion VARCHAR(255) NOT NULL,
            cantidad INT NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255),
            proveedor INT(4))''')
        self.conn.commit()
        
        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()     # Cerramos el cursor inicial para abrir uno nuevo y que nos devuelva, una vez realizada la consulta, un diccionario en vez de una tupla
        self.cursor = self.conn.cursor(dictionary=True)

    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()
        return productos
    
    def consultar_producto(self, codigo):
        # Consultamos un producto a partir de su código
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        return self.cursor.fetchone()

    def mostrar_producto(self, codigo):
        # Mostramos los datos de un producto a partir de su código
        producto = self.consultar_producto(codigo)
        if producto:
            print("-" * 40)
            print(f"Código.....: {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen_url']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("-" * 40)
        else:
            print("Producto no encontrado.")

    def agregar_producto(self, descripcion, cantidad, precio, imagen, proveedor):
        sql = "INSERT INTO productos (descripcion, cantidad, precio, imagen_url, proveedor) VALUES (%s, %s, %s, %s, %s)"
        valores = (descripcion, cantidad, precio, imagen, proveedor)

        self.cursor.execute(sql,valores)
        self.conn.commit()
        return self.cursor.lastrowid

    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
        sql = "UPDATE productos SET descripcion = %s, cantidad = %s, precio = %s, imagen_url = %s, proveedor = %s WHERE codigo = %s"
        valores = (nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor, codigo)

        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0 # Retorna True o False

    def eliminar_producto(self, codigo):
        # Eliminamos un producto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM productos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0



#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------
# Crear una instancia de la clase Catalogo
catalogo = Catalogo(host='localhost', user='root', password='', database='miapp') # Cuando hostiemos esto en pythonanywhere, nos va a dar el host, user y password, el database nosotros

# Carpeta para guardar las imagenes
ruta_destino = 'Codo_Codo\Proyecto Back Codo_Codo\etapa4\static\imagenes'

@app.route("/productos", methods=["GET"])   # Definimos que /productos se ingrese como una request GET (Por Defecto)
def listar_productos():
    productos = catalogo.listar_productos()
    return jsonify(productos)

@app.route("/productos/<int:codigo>", methods=["GET"])
def mostrar_producto(codigo):
    producto = catalogo.consultar_producto(codigo)
    if producto:
        return jsonify(producto)
    else:
        return "Producto no encontrado", 404

@app.route("/productos", methods=["POST"])      # Agregar un nuevo producto
def agregar_producto():
    #Recojo los datos del form
    descripcion = request.form['descripcion']   # Recuperar los datos del formulario que estoy mandando en HTML
    cantidad = request.form['cantidad']         # Recuperame del formulario que me esta mandando el usuario a traves de la peticion POST, recuperame el valor cantidad
    precio = request.form['precio']
    imagen = request.files['imagen']
    proveedor = request.form['proveedor']  
    nombre_imagen = ""

    # Genero el nombre de la imagen
    nombre_imagen = secure_filename(imagen.filename)    # Al nombre de la imagen que se esta mandando se pasa a formato seguro y la guarda en la variable
    nombre_base, extension = os.path.splitext(nombre_imagen)    # dividide el nombre de la imagen en base y extension (teclado, .png)
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"  # Genera el nombre de la imagen concatenado con el tiempo (Esto sirve para que no se sobreescriban las imagenes de = nombre). teclado_123456789.png

    nuevo_codigo = catalogo.agregar_producto(descripcion, cantidad, precio, nombre_imagen, proveedor)
    if nuevo_codigo:    
        imagen.save(os.path.join(ruta_destino, nombre_imagen))  # UNIR la ruta de destino con el nombre de la imagen == ./static/imagenes/teclado_123456789.png
        return jsonify({"mensaje": "Producto agregado correctamente.", "codigo": nuevo_codigo, "imagen": nombre_imagen}), 201
    else:
        return jsonify({"mensaje": "Error al agregar el producto."}), 500

@app.route("/productos/<int:codigo>", methods=["PUT"])  # Modificar un producto. ENDPOINTS
def modificar_producto(codigo):
    #Se recuperan los nuevos datos del formulario
    nueva_descripcion = request.form.get("descripcion")
    nueva_cantidad = request.form.get("cantidad")
    nuevo_precio = request.form.get("precio")
    nuevo_proveedor = request.form.get("proveedor")
    
    # Verifica si se proporcionó una nueva imagen
    if 'imagen' in request.files:
        imagen = request.files['imagen']
        # Procesamiento de la imagen
        nombre_imagen = secure_filename(imagen.filename) 
        nombre_base, extension = os.path.splitext(nombre_imagen) 
        nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}" 

        # Guardar la imagen en el servidor
        imagen.save(os.path.join(ruta_destino, nombre_imagen))
        
        # Busco el producto guardado
        producto = catalogo.consultar_producto(codigo)
        if producto: # Si existe el producto...
            imagen_vieja = producto["imagen_url"]
            # Armo la ruta a la imagen
            ruta_imagen = os.path.join(ruta_destino, imagen_vieja)

            # Y si existe la borro.
            if os.path.exists(ruta_imagen):
                os.remove(ruta_imagen)
    else:     
        producto = catalogo.consultar_producto(codigo)
        if producto:
            nombre_imagen = producto["imagen_url"]

    # Se llama al método modificar_producto pasando el codigo del producto y los nuevos datos.
    if catalogo.modificar_producto(codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nombre_imagen, nuevo_proveedor):
        return jsonify({"mensaje": "Producto modificado"}), 200
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 403

@app.route("/productos/<int:codigo>", methods=["DELETE"])     # Eliminar un producto
def eliminar_producto(codigo):
    # Primero, obtiene la información del producto para encontrar la imagen
    producto = catalogo.consultar_producto(codigo)
    if producto:
        # Eliminar la imagen asociada si existe
        ruta_imagen = os.path.join(ruta_destino, producto['imagen_url'])
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)

        # Luego, elimina el producto del catálogo
        if catalogo.eliminar_producto(codigo):
            return jsonify({"mensaje": "Producto eliminado"}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar el producto"}), 500
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)

"""
Método	Propósito	Idempotente	Seguro	Datos en URL/Cuerpo	Cacheable
GET	    Obtener	    Sí	        Sí	    URL	                Sí
POST	Crear	    No	        No	    Cuerpo	            No
PUT	    Actualizar  Sí	        No	    Cuerpo	            No"""