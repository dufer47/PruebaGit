/* Arrays. Son objetos similares a una lista cuyo prototipo proporciona metodos para efectuar operaciones de recorrido y mutacion.
Tanto de longitud como el tipo de los elementos de un array son variables. Si hemos pensado a las variables como una 'caja' en la que se almacenaun dato,
un array podria considerarse una coleccion de cajas, cada una de ellas con un dato en su interior.
Toda la coleccion comparte un nombre (el nombre del array) y cada caja puede referenciarse para poder acceder a su contenido.

Un Array, tambien conocido como arreglo o vector, es una coleccion o agrupacion de elementos en una misma variable.
Los elementos del array pueden ser datos de diferentes tipos. Sin embargo, algunos de los metodos que poseen solo funcionaran correctamente en arrays que
tengan todos sus elementos del mismo tipo.
Cada elemento dentro del array posee un indice, un valor que nos permite identificarlo. Pensabamos a las variables como una 'caja'. De forma similar, podemos
imaginar un array como los vagones de un tren, donde cada vagon posee un contenido y un orden. El indice es orden y el contenido dentro del vagon es el dato.

Constructor     |      Descripcion 

new Array(len)  ->     Crea un array de len elementos usando un constructor
new Array(e1..) ->     Crea un array vacio o con elementos
[e1, e2...]     ->     Enumeracion de los elementos dentro de corchetes([]). Notacion preferida */

// Definicion mediante un constructor (forma tradicional)
const array = new Array("a","b","c")

// Mediante la enumeracion de sus elementos (forma preferida)
const array2 = ["a","b","c"]    // Array con 3 elementos
const empty = []    // Array vacio (0 elementos)
const mixto = ["a",5,true]  // Array mixto (str, number, boolean)

/* Las posiciones de un array se numeran a partir de 0. Cuando usamos array[0] estamos haciendo referencia a la posicion 0 del array cuyo contenido
es el primer elemento */

const array3 = ["a","b","c"]

console.log(array3[0])   // 'a'
console.log(array3[2])   // 'c'
console.log(array3[5])   // 'Undefined', hace referencia a una posicion que no existe, dado que el array tiene solamente 3 posiciones: 0, 1 y 2

const array4 = ["a","b","c"]
console.log(array4.length)   // 3 -> .length es un metodo que devuelve la cantidad de elementos que posee el array

// Para acceder al ultimo elemento del array. Debemos restar 1 al valor devuelto por .length porque los valores de los indices del arreglo comienzan en 0.
let ultimo = nombreArray[nombreArray.length-1]
const vector = [1,3,5,8]    // 0, 1, 2, 3: cantidad de elementos -1
const vectorVacio = []      // Vector vacio
const vectorDos = new Array ["a","b","c"]
const vectorTres = new Array [1,5,10,15,20]

console.log(vector)
document.write(vector)
console.log("Vector vacio: ",vectorVacio)
console.log(vectorDos)
console.log(vectorDos[1])
console.log(vectorTres[2])
console.log(vectorTres[6])


/* Array | Bucle For
Utilizando un bucle for y la propiedad .length recorremos un vector. vectorDos.length devuelve la longitud del vector, 3. Usamos < (menor que) para recorrer
las posiciones desde 0 a 2, sino la ultima regresa undefined */

console.log("Elementos del vectorDos:")
for(i=0; i<vectorDos.length; i++){
    console.log(vectorDos[i])
}

// En este caso mostramos en el body cada elemento del vectorTres, separados por una coma
document.write("Elementos del vectorTres: <br>")
for(i=0; i<vectorTres; i++){
    document.write(vectorTres[i]+", ")
}


/* Array | Metodos (funciones)

.push(obj1, obj2...)    -> Añade uno o varios elementos al final del array. Devuelve el tamaño del array
.pop()                  -> Elimina y devuelve el ultimo elemento del array
.unshift(obj1, obj2...) -> Añade uno o varios elementos al inicio del array. Devuelve el tamaño del array
.shift()                -> Elimina y devuelve el primer elemento del array
.concat(obj1, obj2...)  -> Concatena los elementos (o elementos de los arrays) pasados por parametro
.idexOf(obj, from)      -> Devuelve la posicion de la primera aparicion de obj desde from
.lastIndexOf(obj, from) -> Devuelve la posicion de la ultima aparicion de obj desde from */

var frutas = ["Banana", "Naranja"]
console.log(frutas)
frutas.push("Kiwi", "Pera")                     // Agrega elementos al final de la lista y regresa la nueva longitud del mismo
console.log(frutas)                             // (4) Banana, Naranja, Kiwi, Pera

console.log(frutas.pop())                       // Elimina desde el final de la lista y regresa la nueva longitud del mismo
console.log(frutas)                             // (3) Banana, Naranja, Kiwi

var colores = ["Rojo", "Celeste"]
console.log(colores)
console.log(colores.unshift("Azul", "Naranja")) // Agrega elementos al comienzo de un array y regresa la nueva longitud del mismo
console.log(colores)                            // (4) Azul, Naranja, Rojo, Celeste

console.log(colores.shift())                    // Elimina el primer elemento y devuelve su valor
console.log(colores)                            // (3) Naranja, Rojo, Celeste

var masColores = ["Verde", "Negro"]
console.log(masColores)
var todos = colores.concat(masColores)          // Los elementos de masColores se concatenan al final de los elementos de colores
console.log(todos)                              // (3) Naranja, Rojo, Celeste, Verde, Negro

/* Estos metodos devuelven la posicion (indice) en la que se encuentra el valor buscado, a partir de la posicion dada. indexOf lo hace contando desde el
principio del arreglo, y lastIndexOf lo hace desde el final. */

var letras = ["A","B","C","D","E","B","C"]
var posB1 = letras.indexOf("B")                 // Buscamos de izquierda a derecha
console.log("La primera B tiene indice ",posB1) // La primera B tiene indice 1
var posB2 = letras.indexOf("B",2)
console.log("La segunda B tiene indice ",posB2) // La segunda B tiene indice 5
var posA = letras.lastIndexOf("A")              // Buscamos de derecha a izquierda
console.log("La ultima A tiene indice ",posA)   // La ultima A tiene indice 0
var posB = letras.lastIndexOf("B")
console.log("La ultima B tiene indice ",posB)   // La ultima B tiene indice 5


/* Array | Otros Metodos

.splice()               -> Agrega o elimina elementos a un array. Regresa los elementos eliminados
.slice()                -> Devuelve los elementos seleccionados en un array como un array nuevo
.reverse()              -> Invierte el orden de elementos del array
.sort()                 -> Ordena los elementos del array bajo un criterio de ordenacion alfabetica
.sort(func)             -> Ordena los elementos del array bajo un criterio de ordenacion func */

const arreglo = ['a','b','c','d','e','f']

// slice(inicio, fin) retorna la copia de un arreglo desde el indice inicio hasta final, excluyendo el final. No modifica el arreglo original

let trozo1 = arreglo.slice(1,3)     // ['b','c']
let trozo2 = arreglo.slice(5)       // ['f']

const arreglo2 = ['a','b','c','d']

// splice() realiza operaciones sobre el arreglo, modificandolo. Es muy versatil, y permite tanto quitar elementos como agregarlos

arreglo.splice(2,0,'n')             // Insertamos un elemento en la posicion 2
console.log(arreglo2)               // ['a','b','n','c','d']
arreglo.splice(1,1,'t')             // Reemplazamos un elemento en la posicion 1
console.log(arreglo2)               // ['a','t','n','c','d']

/* sort y reverse ordenan e invierten el orden, respectivamente, de un arreglo.
Para que funcione correctamente, debemos asegurarnos que todos los elementos del arreglo sean del mismo tipo */

const arreglo3 = ['c','d','a','b','e']  // Arreglo de cadenas: Orden alfabetico

arreglo3.sort()
console.log(arreglo3)                   // ['a','b','c','d','e']

const a = ['3','10','1','31','5']

a.sort()
console.log(a)                          // ['1','10','3','31','5']

const arreglo4 = [4,45,5,59,1,2]        // Orden de numeros: Orden "Alfabetico"

arreglo.sort()
console.log(arreglo4)                   // [1,2,4,45,5,59]

const cuidado = ['a',2,"b",1,true]      // Arreglo mixtos: cuidado

cuidado.sort()
console.log(cuidado)                    // [1,2,'a','b',true]


/* Array | Metodos con funciones
Podemos aplicar funciones a cada elemento del array:

.forEach(cb, arg)       -> Realiza la operacion definida en cb por cada elemento del array
.every(cb, arg)         -> Comprueba si todos los elementos del array cumplen la condicion de cb
.some(cb, arg)          -> Comprueba si al menos un elemento del array cumple la condicion de cb
.map(cb, arg)           -> Construye un array con lo que devuelve cb por cada elemento del array
.filter(cb, arg)        -> Construye un array con los elementos que cumplen el filtro de cb
.findIndex(cb, arg)     -> Devuelve la posicion del elemento que cumple la condicion de cb
.find(cb, arg)          -> Devuelve el elemento que cumple la condicion de cb
.reduce(cb, arg)        -> Ejecuta cb con cada elemento (de izquierda a derecha), acumulando el resultado
.reduceRight(cb, arg)   -? Idem al anterior, pero en orden de derecha a izquierda */


// For in. Recorre las propiedades de un objeto, por ejemplo, un string o un array

for (let variable in object) {
    // Bloque de codigo a ser ejecutado
}
// variable es variable que itera a traves  de las propiedades del objeto. Y object es el objeto sobre el que iteramos

let arreglo5 = ['p','r','u','e','b','a']
for (let letra in arreglo5) {
    console.log(letra)              // 0, 1, 2, 3, 4, 5 (una debajo de la otra)
}

for (let letra in arreglo5) {
    console.log(arreglo5[letra])    // p, r, u, e, b, a (una debajo de la otra)
}

/* For in con objetos. Tambien recorre las propiedades de un objeto, de principio a fin, sin necesidad de indicar 'desde donde' ni 'hasta donde' ni 'el paso'
como con un for "normal". */

let persona = {
    nombre: "Ana",
    apellido: "Paz",
    edad: 25
};

for (let x in persona) {
    console.log(x)                  // Muestra los nombres de las propiedades
    console.log(x +": "+persona[x]) // Muestra los nombres de las propiedades y el valor asociado a c/u
}

// For of. Recorre una cadena str o arreglo array, proporcionando acceso a cada uno de sus elementos

for (variable of iterable) {
    // Statement
}
// En cada iteracion el elemento (propiedad enumerable) correspondiente es asignado a variable

for (let letra of arreglo5) {
    console.log(letra)              // p, r, u, e, b, a (una debajo de la otra)
}
// Definimos un arreglo, y lo recorremos guardando cada elemento en la variable letra, que mostramos por consola


/* WEB STORAGE. JavaScript provee mecanismos para almacenar informacion en formato de txt en el dispositivo del usuario. La API de almacenamiento web
proporciona los mecanismos mediante los cuales el navegador puede almacenar informacion de tipo clave/valor, de una forma mucho mas intuitiva que utilizando
cookies. Existen dos formas de hacerlo:
    A nivel local (localStorage): Al cerrar el navegador la informacion permanece en el dispositivo, y puede ser recuperada en una sesion posterior.
    A nivel de sesion (sessionStorage): Al finalizar la sesion la informacion almacenada se elimina.
Los objetos localStorage y sessionStorage permiten guardar pares clave / valor desde el navegador web

LocalStorage. dicho objeto almacena datos sin fecha de vencimiento. Los datos no se eliminaran cuando se cierre el navegador y estaran disponibles en
cualquier momento futuro.
localStorage puede realizar esta tarea mediante los metodos setItem y getItem, que permiten guardar y recuperar informacion. Los datos se almacenan en formato
de txt, como pares clave / valor.
No todos los navegadores soportan estas tecnologias. Si proporciona soporte, la condicion (typeof(storage)!== "undefined") es verdadera (true). Esto puede
utilizarse para determinar si es posible grabar los datos o no. */

// El siguiente codigo almacena y recupera datos mediante localStorage
if (typeof(Storage) !== "undefined") {          // El navegador soporta esta funcion?
    // setItem guarda datos en el dispositivo
    localStorage.setItem("apellido", "Perez")
    localStorage.setItem("nombre", "Juan")
    console.log("Datos guardados.")
} else {
    console.log("Web Storage no soportado.")
}

if (typeof(Storage) !== "undefined") {          // El navegador soporta esta funcion?
    // getItem recupera datos del dispositivo
    ape = localStorage.getItem("apellido")
    nom = localStorage.getItem("nombre")
    console.log(ape + ", " + nom)
} else {
    console.log("Web Storage no soportado.")
}

/* SessionStorage. Los datos almacenados aca son eliminados cuando finaliza la sesion de navegacion, habitualmente al cerrar la pestaña en la que se muestra
la pagina. Para ver el web storage en Chrome: F12/Application/Storage. */

if (typeof(Storage) !== "undefined") {          // El navegador soporta esta funcion?
    // setItem guarda datos en el dispositivo
    sessionStorage.setItem("curso", "Full Stack Python")
    // getItem recupera datos del dispositivo
    curos = sessionStorage.getItem("curso")
    console.log("recuperado: " + curso)
} else {
    console.log("Web Storage no soportado.")
}


/* JSON: JavaScript Object Notation
JSON es una sintaxis propia de objeto JS utilizada para almacenar e intercambiar datos. Dado que JSON utiliza un formato de txt, es posible convertir
cualquier objeto a JSON y enviarlo al servidor y viceversa. Esto permite procesar datos como objetos JS sin dificultades.
    Servidor -> JSON -> Navegador
    Navegador => JSON => Servidor
Reglas de sintaxis JSON:
La sintaxis JSON se deriva de la sintaxis de notacion de objetos de JavaScript:
    Los datos se guardan en pares de nombre/valor
    Los datos estan separados por comas
    Las {} contienen Objetos
    Los [] se usan para indicar un array
En JSON, los valores deben ser uno de los siguientes tipos de dato:
    str
    number
    object (JSON object)
    array
    boolean
    null
La extension por defecto para los arhivos JSON es ".json" */

// El siguiente JSON posee una propiedad "empleados" compuesta por un arreglo de 3 elementos. Cada uno de ellos es un objeto con dos propiedades.
{
    "empleados"; [
        {"nombre": "Juan", "apellido": "Perez"},
        {"nombre": "Ana", "apellido": "Lopez"},
        {"nombre": "Pedro", "apellido": "Uriarte"},
    ]
}

// El siguiente objeto JSON tiene varias propiedades con su valor. En el caso de la propiedad "hijos" el valor es un array.
{
    "nombre"; "Luis",
    "apellido"; "Fernandez",
    "segundoNombre"; null,
    "edad"; 30,
    "hijos"; ["Ana", "Luisa", "Marcelo"]
}

// Podemos convertir datos almacenados en un objeto JavaScript al formato JSON
var myObj = { name: "Jhon", age: 31, city: "New York" }
var myJSON = JSON.stringify(myObj)      // myJson= {"name":"Jhon","age":31,"city":"New York"}

// Si los datos estan almacenados en JSON los podemos convertir a un objeto JS
var myObj1 = JSON.parse(myJSON)         //  { name: "Jhon", age: 31, city: "New York" }

// EJEMPLO API https://randomuser.me/api    Recomendable ingresar con Firefox Developer Edition
// https://randomuser.me/api/?results=5
/* Muestra datos de usuarios aleatorios, se utiliza para hacer pruebas. Es un str de JSON con un formato particular.
Devuelve un usuario aleatorio, un array con un solo elemento */
