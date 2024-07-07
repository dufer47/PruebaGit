import mysql.connector

# miBaseDeDatos = mysql.connector.connect(host="localhost", user="root", password="")
miBaseDeDatos = mysql.connector.connect(host="localhost", user="root", password="", database="basededatos") # Las consultas se hacen directamente a esa base de datos "basededatos"
#print(miBaseDeDatos)   # Verifico que no devuelva error

cursor = miBaseDeDatos.cursor()

#cursor.execute("")  # Para hacer consultas en la base de datos (fundamental). Ahora las consultas se hacen al cursos

#cursor.execute("CREATE DATABASE basededatos")   # Creo mi base de datos
#cursor.execute("SHOW DATABASES") # Todas mis bases de datos

# for i in cursor:
#     print(i)    # Muestra todas mis bases de datos si en miBaseDeDatos no se especifica la base de datos en donde iremos a consultar

#cursor.execute("CREATE TABLE clientes (nombre VARCHAR (255), direccion VARCHAR (255))")    # Creo una tabla dentro de la base de datos
#cursor.execute("SHOW TABLES") # Todas mis TABLAS en la base de datos basededatos

# for i in cursor:
#     print(i)    # Muestra cada tabla dentro de la base de datos que tengo

#cursor.execute("ALTER TABLE clientes ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") # Modifico la tabla para agregar una columna ID y que esta sea primary key

#sql = "INSERT INTO clientes (nombre, direccion) VALUES (%s, %s)"    # Insertar en la tabla clientes... los valores .... Entonces en la variable sql ponemos la consulta
# valores = [
#     ("Edu", "Cordoba 1234"), # ()=Tuplas. La variable valores son los valores que pasaremos a la consulta
#     ("Miri", "Sanchez 123"), # []=Listas.
#     ("Fabi", "Las Heras 673"),
#     ("Gaby", "Pabellon 666"),
#     ("Mati", "Libertad 5389"),
#     ("Jano", "San Nicolas 663"),
#     ("Tomi", "Mitre 77")
# ]

#valores = ("Lean", "Avellaneda 102")

#cursor.execute(sql, valores)    # (sql, valores) Se concatenan (%s, %s)
#cursor.executemany(sql, valores)    # .execute ejecuta 1, .executemany ejecuta mas de 1. Se concatenan 1x1 (%s, %s)
#cursor.execute("SELECT * FROM clientes")
#cursor.execute("SELECT * FROM clientes WHERE direccion='Mitre 77'")

#resultados = cursor.fetchall()  # Traeme todo lo que te devuelva cursor, y lo guardo en la var resultados
#resultados = cursor.fetchone()  # Me trae el 1ero

#miBaseDeDatos.commit()  # Para pasar/actualizar la base de datos y se vean reflejados las consultas realizadas

#print(cursor.rowcount, "registros insertados")  # Listado de la cantidad de registros que fueron aceptados
#print(cursor.rowcount, "registros insertados. El ID asignado es:", cursor.lastrowid)  # Listado de la cantidad de registros que fueron aceptados y el ultimo ID asignado
# for i in resultados:
#     print(i)

#######################################################
# DELETE
# cursor.execute("DELETE FROM clientes WHERE nombre='Juan'")

# miBaseDeDatos.commit()
# print(cursor.rowcount,"registros actualizados")

#######################################################
# FLASK
from flask import Flask, redirect

app = Flask(__name__)   # Es asi, no se toca. Me crea un objeto app, llamamos a Flask y le pasamos el parametro __name__
# Con esto instanciamos una aplicacion Flask (un obejto de la clase Flask) en app

@app.route("/") # == app.add_url_rule("/","hello",hola_mundo)
def hola_mundo():
    return "Hola chicos de Codo a Codo, estamos desde FLASK con RUTAS/Decoradores"
# app.add_url_rule("/","hello",hola_mundo)

@app.route("/24148")
def hola_24148():
    return "Hola chicos de la comision 24148, estamos desde FLASK con RUTAS/Decoradores"

@app.route("/usuario/<username>")
def hola_usuario(username):
    return "Hola Usuario " + username

@app.route("/redir")
def redireccion():
    return redirect("/24148")   # Si no traemos redirect de la libreria Flask, no funcionara

if __name__ == "__main__":  # Es asi, no se toca. Con esto ya tenemos la aplicacion corriendo
    app.run()   # app.run("localhost",port,debug mode) -> por defecto <- (127.0.0.1:500,False)