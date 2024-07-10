from flask import Flask, request, jsonify

from flask_cors import CORS

import mysql.connector

app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas

class Registro:
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
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS visitantes (
            codigo INT AUTO_INCREMENT PRIMARY KEY,
            nombre CHAR(30) NOT NULL,
            email VARCHAR(50) NOT NULL,
            telefono INT (12) NOT NULL,
            mensaje VARCHAR(255))''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

    def listar_visitantes(self):
        self.cursor.execute("SELECT * FROM visitantes")
        visitantes = self.cursor.fetchall()
        return visitantes

    def consultar_visitante(self, codigo):
        # Consultamos un visitante a partir de su código
        self.cursor.execute(f"SELECT * FROM visitantes WHERE codigo = {codigo}")
        return self.cursor.fetchone()

    def mostrar_visitante(self, codigo):
        # Mostramos los datos de un visitante a partir de su código
        visitante = self.consultar_visitante(codigo)
        if visitante:
            print("-" * 40)
            print(f'Codigo............: {visitante["codigo"]}')
            print(f'Nombre............: {visitante["nombre"]}')
            print(f'Email.............: {visitante["email"]}')
            print(f'Telefono..........: {visitante["telefono"]}')
            print(f'Mensaje...........: {visitante["mensaje"]}')
            print("-" * 40)
        else:
            print("Visitante no encontrado.")

    def agregar_visitante(self, nombre, email, telefono, mensaje):
        sql = "INSERT INTO visitantes (nombre, email, telefono, mensaje) VALUES (%s, %s, %s, %s)"
        valores = (nombre, email, telefono, mensaje)

        self.cursor.execute(sql,valores)
        self.conn.commit()
        return self.cursor.lastrowid

    def modificar_visitante(self, codigo, nuevo_nombre, nuevo_email, nuevo_telefono, nuevo_mensaje):
        sql = "UPDATE visitantes SET nombre = %s, email = %s, telefono = %s, mensaje = %s WHERE codigo = %s"
        valores = (nuevo_nombre, nuevo_email, nuevo_telefono, nuevo_mensaje, codigo)

        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def eliminar_visitante(self, codigo):
        # Eliminamos un visitante de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM visitantes WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0

#--------------------------------------------------------------------
#--------------------------------------------------------------------

# Crear una instancia de la clase Registro
registro = Registro(host="localhost", user="root", password="", database="mihoroscopo")

@app.route("/visitantes", methods=["GET"])
def listar_visitantes():
    visitantes = registro.listar_visitantes()
    return jsonify(visitantes)

@app.route("/visitantes/<int:codigo>", methods=["GET"])
def mostrar_visitante(codigo):
    visitante = registro.consultar_visitante(codigo)
    if visitante:
        return jsonify(visitante)
    else:
        return "Visitante no encontrado.", 404

@app.route("/visitantes", methods=["POST"])
def agregar_visitante():
    #Recojo los datos del form
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    mensaje = request.form['mensaje']

    nuevo_codigo = registro.agregar_visitante(nombre, email, telefono, mensaje)
    if nuevo_codigo:
        return jsonify({"mensaje": "Visitante agregado correctamente.", "codigo": nuevo_codigo}), 201
    else:
        return jsonify({"mensaje": "Error al agregar el visitante."}), 500

@app.route("/visitantes/<int:codigo>", methods=["PUT"])
def modificar_visitante(codigo):
    #Se recuperan los nuevos datos del formulario
    nuevo_nombre = request.form.get("nombre")
    nuevo_email = request.form.get("email")
    nuevo_telefono = request.form.get("telefono")
    nuevo_mensaje = request.form.get("mensaje")

   # Se llama al método modificar_visitante pasando el codigo del visitante y los nuevos datos.
    if registro.modificar_visitante(codigo, nuevo_nombre, nuevo_email, nuevo_telefono, nuevo_mensaje):
        return jsonify({"mensaje": "Visitante modificado."}), 200
    else:
        return jsonify({"mensaje": "Visitante no encontrado."}), 403

@app.route("/visitantes/<int:codigo>", methods=["DELETE"])
def eliminar_visitante(codigo):
    
    visitante = registro.consultar_visitante(codigo)
    if visitante:

        # Luego, elimina el visitante del registro
        if registro.eliminar_visitante(codigo):
            return jsonify({"mensaje": "Visitante eliminado."}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar el visitante."}), 500
    else:
        return jsonify({"mensaje": "Visitante no encontrado."}), 404


if __name__ == "__main__":
    app.run(debug=True)

"""
Método	Propósito	Idempotente	Seguro	Datos en URL/Cuerpo	Cacheable
GET	    Obtener	    Sí	        Sí	    URL	                Sí
POST	Crear	    No	        No	    Cuerpo	            No
PUT	    Actualizar  Sí	        No	    Cuerpo	            No"""