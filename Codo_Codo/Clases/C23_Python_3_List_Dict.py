"""
Cadenas de caracteres

Python, al igual que la mayoría de los lenguajes de programación actuales, provee un tipo de datos específico para tratar las cadenas de
caracteres (strings). Se trata de un tipo de dato con longitud variable, ya que deben adecuarse a la cantidad de caracteres que albergue la cadena.
Este tipo de datos posee una buena cantidad de métodos y propiedades que facilita su uso.

Una cadena de caracteres está compuesta por cero o más caracteres. Las cadenas pueden delimitarse con comillas simples o dobles. """

# Definición de cadenas usando comillas dobles
dia1 = "Lunes"
x = "" # x es un string de longitud cero

# Definición de cadenas usando comillas simples
dia2 = 'Martes'
z = "121" # z contiene dígitos, pero es un string

"""
Una ventaja del hecho de poder delimitar cadenas con comillas simples o dobles es que si usamos comillas de una clase, las de otra clase puede
utilizarse como parte de la cadena. Una cadena puede replicarse con el operador *. """

print("Mi perro 'Toby'") # Mi perro 'Toby'
print('Mi perro "Toby"') # Mi perro "Toby"

risa = 'ja'
carcajada = risa*5 # jajajajaja
asteriscos = "*"*10 # **********

"""
También pueden usarse triples comillas simples o dobles, que proveen un método sencillo para crear cadenas usando más de una línea de código: """

# Definición de cadenas usando comillas dobles triples:
cadena1 = """En Python es posible definir cadenas de caracteres utilizando más de una línea de código"""

# Definición de cadenas usando comillas simples triples:
cadena2 = '''Por supuesto, se puede hacer
lo mismo utilizando comillas simples'''

"""
Cadenas de caracteres | Concatenación

Para concatenar dos o más cadenas se utiliza el operador + (más). El mismo operador se usa para sumar números o concatenar cadenas. Pero no
podemos utilizarlo con datos mixtos, porque se obtiene un error. Este error se puede evitar mediante las funciones de conversión de tipos.: """

nombre= input("Ingrese su nombre: ")
saludo= "Hola "+ nombre
print(saludo)

var1 = 3 + 5 # 8 (entero)
var2 = "3" + "5" # 35 (cadena)
# var3 = 3 + "5" # TypeError
var4 = str(3) + "5" # 35 (cadena)
var5 = 3 + int("5") # 8 (entero)

# Dos cadenas se pueden comparar mediante los operadores relacionales.
cadena1 = "Hola"
cadena2 = "Codo a Codo"
print(cadena1 > cadena2)
print(cadena1 == cadena2)
print(cadena1 < cadena2)

# La comparación es case sensitive, es decir, se distingue entre mayúsculas y minúsculas.
cadena1 = "Hola"
cadena2 = "hola"
print(cadena1 == cadena2)

"""
Cadenas de caracteres

En Python disponemos de la función len(), que retorna la cantidad de caracteres que contiene un string: """

nombre='Codo a Codo'
print(len(nombre)) #se imprime 11

""" Se accede a los elementos de la cadena utilizando subíndices. El primer caracter tiene subíndice cero. Si usamos subíndices negativos, se cuentan desde el final de la
cadena.: """

cadena = "Hola Codo a Codo"
print(cadena[0])
print(cadena[5])
print(cadena[-1])
print(cadena[-2])

"""
Cadenas de caracteres | Métodos

Las cadenas tienen una serie de métodos (funciones) que simplifican el desarrollo de código. Tres de estos métodos son:
● .upper(): devuelve la cadena con todos sus caracteres en mayúsculas.
● .lower(): devuelve la cadena con todos sus caracteres en minúsculas.
● .capitalize(): devuelve la cadena con su primer caracter en mayúscula y todos los demás en minúsculas.
Existen los métodos .isupper() e .islower() que devuelven True si todos los caracteres alfabéticos de una cadena están en mayúsculas o minúsculas respectivamente."""

cadena = "Codo a Codo"
print(cadena.upper()) # CODO A CODO
print(cadena.lower()) # codo a codo
print(cadena.capitalize()) # Codo a codo

"""
Una "rebanada" es un subconjunto de una cadena que se obtiene mediante la definición de un índice inicio y/o fin. El subconjunto devuelto incluye el
valor del índice de inicio, pero no el valor final. Un tercer valor permite determinar un paso, que incluso puede ser negativo: """

cadena = "¡Hola mundo!"
print(cadena[6:11]) # mundo | Del indice 6 hasta 10 inclusive
print(cadena[2:12:2]) # oamno | Del indice 2 hasta 11 inclusive en saltos de 2 en 2
print(cadena[6:]) # mundo!  | Del indice 6 hasta final
print(cadena[:5]) # ¡Hola   | Del principio hasta indice 5
print(cadena[:]) # ¡Hola mundo! | Todo
print(cadena[::2]) # ¡oamno | Todo en saltos de 2 en 2
print(cadena[::-1]) # !odnum aloH¡ | Todo pero al reves

"""
Cadenas de caracteres | in / not in

Los operadores de pertenencia se utilizan para comprobar si un caracter o cadena se encuentran dentro de otra.

Operador    |   Descripcion
in              Devuelve True si el valor se encuentra en una secuencia; False en caso contrario.
not in          Devuelve True si el valor no se encuentra en una secuencia; False en caso contrario. """

cadena = "Codo a Codo"
print("C" in cadena) # True
print("n" in cadena) # False
print("Codo" in cadena) # True
print("A" not in cadena) # True
print("o" not in cadena) # False

"""
Cadenas de caracteres | for , min() y max()

Un bucle for puede iterar sobre una cadena, y la variable recibe en cada iteracion uno de los caracteres de la misma.
min() y max() devuelven el elemento con el codigo ASCII mas pequeño o mas grande respectivamente. """

# for con cadenas
cadena = "Python"
for letra in cadena:
    print(letra)

# min() y max()
cadena = "Programador"
cont = 0
print(max(cadena)) # R
print(min(cadena)) # P

"""
Cadenas de caracteres | .join(), .split() y .replace()

cadena.join(separador) devuelve una cadena con el separador entre cada caracter. cadena.split(separador) convierte una cadena en lista, y cadena.replace(viejo,nuevo,max)
reemplaza una cadena por otra hasta un maximo. Si se omite max reemplaza todas las apariciones: """

cadena = "12345"
cadena = '-'.join(cadena)
print(cadena)   # 1-2-3-4-5

cadena = "Codo a Codo"
lista = cadena.split(' ')
print(lista)    # ['Codo','a','Codo']

cadena = "Codo a Codo"
cadena = cadena.replace('Codo','Mano')
print(cadena)   # Mano a Mano

"""
Cadenas de caracteres | Detección de tipos

cadena.isalpha() devuelve True si todos los caracteres de una cadena son alfabeticos. cadena.isdigit() devuelve True si todos los caracteres de una cadena son digitos.
cadena.isalnum() devuelve True si todos los caracteres de una cadena son alfabeticos o numericos: """

#.isalpha()
cad1 = "Python"
cad2 = "Python3"
print(cad1.isalpha())
# True
print(cad2.isalpha())
# False

#.isdigit()
cad1 = "1234"
cad2 = "1234a"
print(cad1.isdigit())
# True
print(cad2.isdigit())
# False

#.isalnum()
cad1 = "12Ab"
cad2 = "12Ab%"
print(cad1.isalnum())
# True
print(cad2.isalnum())
# False

"""
Cadenas de caracteres | Recorte

cadena.lstrip(str) y cadena.rstrip(str) devuelven cadenas a las que se les han quitado los caracteres indicados por str a la izquierda o derecha, respectivamente.
cadena.strip(str) devuelve una cadena sin los caracteres indicados en str al inicio y al final de la cadena. """

#.lstrip()
cad1 = "---Hola-Mundo----"
cad1 = cad1.lstrip('-')
print(cad1)
# Hola-Mundo----

#.rstrip()
cad1 = "---Hola-Mundo----"
cad1 = cad1.rstrip('-')
print(cad1)
# ---Hola-Mundo

#.strip()
cad1 = "---Hola-Mundo----"
cad1 = cad1.strip('-')
print(cad1)
# Hola-Mundo

"""
Cadenas de caracteres | Búsquedas

cadena.find(<str>,[[inicio],[fin]]) devuelve la posición donde encuentra str en la cadena. Si no lo encuentra devuelve -1. Se puede indicar los subíndices
desde (inicio) y hasta (fin) donde buscar. <cadena>.rfind(<str>,[[inicio],[fin]]) es similar a find, pero busca la última
aparición. """

#.find()
cad="Codo a Codo"
pos= cad.find("Codo")
print(pos) # 0

#.rfind()
cad="Codo a Codo"
pos= cad.rfind("Codo")
print(pos) # 7

"""
Cadenas de caracteres | f-Strings

f-Strings tiene una sintaxis simple y fluida que simplifica la tarea de dar formato a cadenas de texto. Para mostrar variables se coloca el nombre de las
variables entre llaves {}, en una cadena que antepone f a su contenido. Al ejecutar el código, todos los nombres de las variables se reemplazan por sus
respectivos valores: """

legajo = 12212
nombre = "María"
nota = 10
print(f"Legajo: {legajo} Nombre: {nombre} Nota: {nota}")
# Legajo: 12212 Nombre: María Nota: 10


"""
Listas

Una lista es una secuencia ordenada de elementos. Pueden tener elementos del mismo tipo o combinar distintos tipos de datos, aunque esto último es poco frecuente.
Las listas en Python son un tipo contenedor, compuesto, y se usan para almacenar conjuntos de elementos relacionados.
Junto a las tuplas, diccionarios y conjuntos, constituyen uno de los tipos de datos más versátiles del lenguaje, con la particularidad de ser mutables. Esto ultimo
quiere decir que su contenido se puede modificar despues de haber sido creadas. 

Las listas se crean asignando a una variable una secuencia de elementos encerrados entre corchetes [ ] y separados por comas. Se puede crear una
lista vacía, y las listas pueden ser elementos de otras listas. Las listas se suelen nombrar en plural. Para incluir una lista como parte de
otra, basta con incluirla separada por comas de los otros elementos. """

numeros = [1,2,3,4,5] #Lista de números
dias = ["Lunes", "Martes", "Miércoles"] #Lista de strings
elementos = [] #Lista vacía
sublistas = [ [1,2,3], [4,5,6] ] # lista de listas

"""
Listas | Acceso por subíndice

Las listas se pueden imprimir directamente, y el acceso a sus elementos se hace mediante subíndices. El primer elemento tiene subíndice cero. Un subíndice negativo
hace que la cuenta comience desde atrás. Un subíndice fuera de rango genera un error: out of range """

dias = ["Lunes", "Martes", "Miércoles"]
print(dias)
print(dias[0])
print(dias[1])
print(dias[-1])
# print(dias[3])

"""
Listas | Recorrer listas con for y while

Es posible recorrer una lista utilizando for y range o while para generar la secuencia de índices.
len(lista) retorna la cantidad de elementos que posee una lista y resulta muy útil, entre otras cosas, para determinar la cantidad de ciclos de un bucle. """

# for con listas
lista = [2,3,4,5,6]
suma = 0
for i in range(len(lista)):
    suma = suma + lista[i]
print(suma) # 20

# while con listas
lista = [2,3,4,5,6]
suma = 0
i = 0
while i < len(lista):
    suma = suma + lista[i]
    i = i + 1
    print(suma)
print(suma) # 20

"""
Listas | Recorrer listas con for.. in

También se puede iterar en forma directa los elementos de la lista, sin necesidad de generar la secuencia de subíndices.
En este caso la variable i toma el elemento de la lista: """

# for .. in
vocales = ['a','e','i','o','u']
# El bucle recorre la lista
for i in vocales:
    print(i)

"""
Listas | Desempaquetado y concatenado

El proceso de desempaquetado consiste en asignar cada elemento de una lista a una variable. Además, las listas pueden concatenarse con el operador suma: """

# Desempaquetado
dias = ["Lunes", "Martes", "Miércoles"]
d1, d2, d3 = dias
print(d1)   # Lunes
print(d2)   # Martes
print(d3)   # Miercoles

# Concatenado
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2
print(lista3)   # [1,2,3,4,5,6]

"""
Listas | max(), min() y sum()

La función max() devuelve el mayor elemento de una lista.
● La función min() devuelve el menor elemento de una lista.
● La función sum() devuelve la suma de los elementos de una lista: """

# max(), min() y sum()
lista = [3,4,5,6]
print(max(lista))   # 6
print(min(lista))   # 3
print(sum(lista))   # 18

"""
Listas | in / not in y list()

Los operadores de pertenencia in / not in permiten determinar si un elemento está o no en una lista. La función list() convierte cualquier secuencia a una lista.
Se puede utilizar con rangos, cadenas y otros. """

# in/not in
lista = list(range(6))
print(lista)

cadena = "Hola"
print(list(cadena))

lista2 = [3,4,5,6]
print(4 in lista2)
print(8 in lista2)
print("A" not in lista2)

"""
Listas | .append() e .insert()

El método append() agrega un elemento al final de la lista. insert(<pos>, <elemento>) inserta un elemento en una posición determinada. """

#.append()
lista = [3,4,5]
lista.append(6)
print(lista)

#.insert()
lista=[3,4,5]
lista.insert(0,2)
print(lista)
lista.insert(3,25)
print(lista)

"""
Listas | .pop() y .remove()

pop(<posición>) Elimina un elemento en una posición determinada de la lista. Si no se pasa un argumento, pop() elimina el último elemento de la lista.
remove(<valor>) elimina un elemento en la lista, identificado por su valor. """

#.pop
lista = [6,9,8]
lista.pop()
#Resultado: [6,9]

#.pop(posicion)
lista = [3,4,5]
lista.pop(1)
#Resultado: [3,5]

#.remove(valor)
lista = [3,4,5]
lista.remove(3)
#Resultado: [4,5]

"""
Listas | .index(), count() y reverse()

index(<valor>) busca un valor y devuelve su posición. Admite como argumento adicional un índice inicial a partir de donde comenzar la
búsqueda. count() devuelve la cantidad de repeticiones de un elemento, cero si no lo encuentra. Y reverse() Invierte el orden de los elementos de una lista. """

#.index(valor)
lista = [3,4,5]
print(lista.index(5))
#Resultado: 2

#.count()
lista = [3,4,5,3,5,8,5]
print(lista.count(5))
# Resultado: 3
print(lista.count(2))
# Resultado: 0

#.reverse()
lista = [3,4,5]
lista.reverse()
print(lista)
# Resulado: [5,4,3]

"""
Listas | .sort() y clear()

sort() ordena los elementos de la lista, de menor a mayor. sort(reverse=True) ordena la lista de mayor a menor. En ambos casos, el orden depende del tipo
de dato contenido en la lista. Y clear() elimina todos los elementos de la lista. """

#.sort()
lista = [5, 1, 7, 2]
lista.sort()
print(lista)
#Resultado: [1,2,5,7]

#.sort(reverse=True)
lista = [5, 1, 7, 2]
lista.sort(reverse=True)
print(lista)
#Resultado: [7,5,2,1]

#.clear()
lista = [3,4,5]
lista.clear()
print(lista)
#Resultado: []


"""
Diccionarios

Los diccionarios en Python son un conjunto no ordenado de pares clave: valor. Estas claves son únicas, y si se intenta guardar un valor a
una clave ya existente se pierde dicho valor. Las claves pueden ser cualquier elemento de tipo inmutable (cadenas,
números o tuplas (si estás sólo contienen cadenas, números o tuplas). Se representan como una lista de pares (las claves y valores) separados
por comas y encerrados entre llaves.

Los diccionarios se pueden crear mediante la simple enumeración de los elementos, o por comprensión. Para acceder a las claves, Python utiliza un método de hash. """

# Creación: Por extensión
diccionario = {'Juan': 56, 'Ana': 15}
# Creación: Por compresión
diccionario = {x: x ** 2 for x in (2, 4, 6)}

{} # diccionario vacío
{'Juan': 56} # diccionario de un elemento
{'Juan': 56, 'Ana': 15} # diccionario de dos elementos

"""
Diccionarios | Acceso

Puede accederse a un diccionario de diferentes maneras:
● A las claves, utilizando método keys()
● A los valores, utilizando la clave como índice
● A la clave-valor, utilizando método ítems()
● No es posible obtener porciones de un diccionario usando [:] """

diccionario = {1: 'uno', 2:'dos', 3:'tres'}
print(diccionario.keys())                   # dict_keys([1,2,3])
for i in diccionario.keys():
    print(diccionario[i])                   # 'uno' / 'dos' / 'tres'
for clave, valor in diccionario.items():
    print(clave, ':', valor, end= '; ')     # 1 : 'uno'; 2 : 'dos'; 3 : 'tres';

"""
Diccionarios | Métodos, funciones y operadores

Los siguientes diagramas resumen los métodos, funciones y operadores disponibles para los diccionarios:

Metodos: keys, get, items, values, renive, pop, update, clear, copy, fromkeys, setdefault.
Funciones: len, max-min-sum, del, dict.
Operadores: Pertenencia(in), Identidad(is).


Tuplas

Las tuplas en Python son conjunto de elementos separados por comas y encerrados entre paréntesis. Los paréntesis no son obligatorios.
Las tuplas son inmutables y en general contienen una secuencia heterogénea de elementos. Los elementos de una tupla si pueden ser mutables.
Podemos pensar en una tupla como si fuese una lista, pero recordando que su inmutabilidad hace que muchos de sus métodos y funciones no puedan utilizarse.

Las tuplas se pueden crear por extensión, o mediante un empaquetado (pack). Y se pueden “desempaquetar” (unzip), volcando su contenido a variables.
Se requiere que la cantidad de variables a la izquierda del signo igual sea el tamaño de la tupla. """

# Creación: Por extensión
tupla1 = ('uno', 'dos', 'tres')
# Creación: Mediante empaquetado
tupla2 = 'Palotes, Juan de', (1930, 11, 13), 3000936

nombre, nacimiento, dni =( 'Palotes, Juan de', (1930, 11, 13), 3000936)

"""
Tuplas | Acceso

Se accede a los elementos desempaquetando, mediante un índice o usando rebanadas (slices). """

()                                              # tupla vacía
'un valor',                                     # tupla con un valor
('uno', 'dos', 'tres')                          # cadenas
('Palotes, Juan de', (1930, 11, 13), 3000936)   # datos de persona

tupla = ('Palotes, Juan de', (1930, 11, 13), 3000936)
nombre, fecha, dni = tupla # Desempaque

# Acceso por índices:
print('Nombre: ', tupla[0], '. Fecha nac.: ', tupla[1], '. DNI: ', tupla[2])
print(tupla[::]) # Acceso mediante rebanadas

"""
Conjuntos

Los conjuntos en Python son una metáfora de los conjuntos del área de la matemática. Al igual que aquellos, en Python son conjuntos de elementos únicos,
no ordenados y sus elementos no son mutables. Se definen sus elementos encerrándolos entre llaves y separados por comas.
No puede accederse a los elementos de un diccionario a través de un subíndice pues sus elementos no están ordenados."""

set() # conjunto vacío
{'un valor'} # conjunto con un valor
{'uno', 'dos', 'tres'} # conjunto de cadenas
{'Palotes, Juan de', (1930, 11, 13), 3000936} # datos de persona

# Se accede a los elementos iterando o usando el método pop().

conjunto = {'Empleado', (1930, 11, 13), 36}     # {'Empleado', 36, (1930, 11, 13)}
a = set(conjunto)                               # Empleado
print(a)                                        # 36
[print (elem) for elem in a]                    # (1930, 11, 13)
print(a)                                        # {'Empleado', 36, (1930, 11, 13)}

"""
Conjuntos | Métodos, funciones y operadores

Los siguientes diagramas resumen los métodos, funciones y operadores disponibles para los conjuntos:

Metodos: clear, Remove-discard, union-intersection-difference-symmetric_difference, issubset-ilssupperset, isdisjoint, add, pop.
Funciones: len, max-min-sum, set-frozenset.
Operadores: Identidad(is), Pertenencia(in), Union(|)-Interseccion(&)-Diferencia(-)-Diferencia simetrica(^). """

