from flask import Flask, request, jsonify

from flask_cors import CORS

import mysql.connector

import conexion as bd

app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas

class Registro:
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
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS inscriptos (
            codigo INT AUTO_INCREMENT PRIMARY KEY,
            nombre CHAR(30) NOT NULL,
            email VARCHAR(50) NOT NULL,
            telefono INT (12) NOT NULL,
            mensaje VARCHAR(255))''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

    def listar_inscriptos(self):
        self.cursor.execute("SELECT * FROM inscriptos")
        inscriptos = self.cursor.fetchall()
        return inscriptos

    def consultar_inscripto(self, codigo):
        # Consultamos un inscripto a partir de su código
        self.cursor.execute(f"SELECT * FROM inscriptos WHERE codigo = {codigo}")
        return self.cursor.fetchone()

    def mostrar_inscripto(self, codigo):
        # Mostramos los datos de un inscripto a partir de su código
        inscripto = self.consultar_inscripto(codigo)
        if inscripto:
            print("-" * 40)
            print(f'Codigo............: {inscripto["codigo"]}')
            print(f'Nombre............: {inscripto["nombre"]}')
            print(f'Email.............: {inscripto["email"]}')
            print(f'Telefono..........: {inscripto["telefono"]}')
            print(f'Mensaje...........: {inscripto["mensaje"]}')
            print("-" * 40)
        else:
            print("inscripto no encontrado.")

    def agregar_inscripto(self, nombre, email, telefono, mensaje):
        sql = "INSERT INTO inscriptos (nombre, email, telefono, mensaje) VALUES (%s, %s, %s, %s)"
        valores = (nombre, email, telefono, mensaje)

        self.cursor.execute(sql,valores)
        self.conn.commit()
        return self.cursor.lastrowid

    def modificar_inscripto(self, codigo, nuevo_nombre, nuevo_email, nuevo_telefono, nuevo_mensaje):
        sql = "UPDATE inscriptos SET nombre = %s, email = %s, telefono = %s, mensaje = %s WHERE codigo = %s"
        valores = (nuevo_nombre, nuevo_email, nuevo_telefono, nuevo_mensaje, codigo)

        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def eliminar_inscripto(self, codigo):
        # Eliminamos un inscripto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM inscriptos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0

#--------------------------------------------------------------------
#--------------------------------------------------------------------

# Crear una instancia de la clase Registro
registro = Registro(host=bd.host, user=bd.user, password=bd.password, database=bd.database)

@app.route("/inscriptos", methods=["GET"])
def listar_inscriptos():
    inscriptos = registro.listar_inscriptos()
    return jsonify(inscriptos)

@app.route("/inscriptos/<int:codigo>", methods=["GET"])
def mostrar_inscripto(codigo):
    inscripto = registro.consultar_inscripto(codigo)
    if inscripto:
        return jsonify(inscripto)
    else:
        return "inscripto no encontrado.", 404

@app.route("/inscriptos", methods=["POST"])
def agregar_inscripto():
    #Recojo los datos del form
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    mensaje = request.form['mensaje']

    nuevo_codigo = registro.agregar_inscripto(nombre, email, telefono, mensaje)
    if nuevo_codigo:
        return jsonify({"mensaje": "inscripto agregado correctamente.", "codigo": nuevo_codigo}), 201
    else:
        return jsonify({"mensaje": "Error al agregar el inscripto."}), 500

@app.route("/inscriptos/<int:codigo>", methods=["PUT"])
def modificar_inscripto(codigo):
    #Se recuperan los nuevos datos del formulario
    nuevo_nombre = request.form.get("nombre")
    nuevo_email = request.form.get("email")
    nuevo_telefono = request.form.get("telefono")
    nuevo_mensaje = request.form.get("mensaje")

   # Se llama al método modificar_inscripto pasando el codigo del inscripto y los nuevos datos.
    if registro.modificar_inscripto(codigo, nuevo_nombre, nuevo_email, nuevo_telefono, nuevo_mensaje):
        return jsonify({"mensaje": "inscripto modificado."}), 200
    else:
        return jsonify({"mensaje": "inscripto no encontrado."}), 403

@app.route("/inscriptos/<int:codigo>", methods=["DELETE"])
def eliminar_inscripto(codigo):
    
    inscripto = registro.consultar_inscripto(codigo)
    if inscripto:

        # Luego, elimina el inscripto del registro
        if registro.eliminar_inscripto(codigo):
            return jsonify({"mensaje": "inscripto eliminado."}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar el inscripto."}), 500
    else:
        return jsonify({"mensaje": "inscripto no encontrado."}), 404


if __name__ == "__main__":
    app.run(debug=True)

