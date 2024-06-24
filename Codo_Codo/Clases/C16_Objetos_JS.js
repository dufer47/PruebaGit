/* Unobjeto de .js tiene propiedades asociadas a el. Una propiedad de un objeto se puede explicar como una variable asociada al objeto. Las propiedades de un objeto
basicamente son lo mismo que las variables comunes de .js, excepto por el nexo con el objeto. Las propiedades de un objeto definen las caracteristicas del mismo.
Se accede a las propiedades de un objeto con la notacion punto. */

texto1 = objectName.propertyName
//nombreDelObjeto.propiedadDelObjeto, ambos nombres son sensibles a las mayusculas y minusculas

// Crear Objeto
var miAuto = new Object()
// Crear propiedades
miAuto.marca = 'Ford'
miAuto.tipo = 'Ranger'
miAuto.modelo = 2019
console.log("El auto es: ",miAuto.marca,miAuto.tipo," y el modelo es ",miAuto.modelo)

/* Se pueden crear tambien mediante un iniciador de objeto, (o literal), que es una lista delimitada por comas de cero o mas pares de nombres de propiedad y valores
asociados al objeto, encerrados entre llaves. Las propiedades de un objeto que no han sido asociadas a un valor en el momento de la creacion del mismo 'undefined' */

var miVehiculo = {
    marca: 'Ford',
    tipo: 'Ranger',
    modelo: 2019
}

var persona = {
    nombre: "Juan",
    apellido: "Perez",
    dni: "11223344",
    // Metodo es una propiedad mas
    nombreCompleto: function() {
        return this.nombre + " " + this.apellido    // El string que devuelve tiene informacion del propio objeto, por eso usamos "this"
    }
}
console.log(persona)                    // Imprimo el objeto
console.log(persona.nombre)             // Imprimo una propiedad del objeto: Juan
console.log(persona.nombreCompleto)     // Imprimo el resultado del metodo: Juan Perez

/* Se puede accede o establecer las propiedades de los objetos mediante la notacion de corchetes []. En los objetos cada propiedad esta asociada con un valor tipo 'str'
que se puede utilizar para acceder a ella */

miAuto['marca'] = 'Ford'
miAuto['tipo'] = 'Ranger'
miAuto['modelo'] = 2019

/* Los metodos son el equivalente de las funciones, pero dentro de un objeto. Proporcionan al objeto la capacidad de interactuar con otros objetos o con el resto del programa.
Para escribirlos, colocamos su nombre seguido de parentisis. El bloque de codigo que compone el metodo se escribe entre llaves, y puede devolver resultados mediante return.
Se invocan desde el resto del programa usando la notacion punto, pero usando parentesis luego de su nombre para diferenciarlas de las propiedades */

// Nuevo Objeto PERRO con metodos quienSoy() y ladrar()
var perro = {
    nombre: "Milo",
    edad: 12,
    vivo: true,
    quienSoy() {return "Soy " + this.nombre},
    ladrar() {return this.nombre + " dice guau!"}
}
console.log(perro.nombre,"tiene",perro.edad,"años")
console.log(perro.quienSoy())
if(perro.vivo) {
    console.log(perro.ladrar())
}

/* Las clases son una suerte de 'molde' que podemos usar para crear varios objetos del mismo tipo. Usamos un contructor y 'this' para asignar valores a las
propiedades de los objetos instanciados. Usamos 'this' para asignar valores a las propiedades del objeto que estamos creando con new Perro. */

// Clase Perro, con su constructor
class Perro {
    constructor(nombre, edad, vivo) {
        this.nombre = nombre
        this.edad = edad
        this.vivo = vivo
    }
}
var perro1 = new Perro ("Lola", 4, true)
var perro2 = new Perro ("Lassie", 10, false)

perro1.nombre = "Toby"      // Modificamos alguna de sus PROPIEDADES
perro2.edad = 6

/* Para definir un tipo (clase) de objeto, creamos una funcion que especificque su nombre, propiedades y metodos. Supongamos que deseas una clase llamada "Auto"
para crear objetos "auto", y deseas que tenga las siguientes propiedades: marca, tipo y modelo. Podrias escribir la siguiente funcion: */

// funcion constructora (clase)
function Auto(marca, tipo, modelo) {
    this.marca = marca
    this.tipo = tipo
    this.modelo = modelo
}
// Creamos el objeto miAuto
var miAuto = new Auto('Ford','Focus', 2019)
// Creamos el objeto miFurgon
var miFurgon = new Auto('Renault','Traffic', 2010)
// Observar el uso de 'this' para asignar valores a las propiedades del objeto en funcion de los valores pasados a la funcion


/* Objeto String. Cuando hablamos de una variable que posee informacion de texto, decimos que su tipo de dato es String. Hay dos formas de crear una variable de txt,
"new String(s)": Crea un objeto de txt a partir del texto 's' pasado como parametro; o "'s'": Simplemente, el txt entre comillas. Notacion preferida.
Los String son tipo de datos primitivos, y como tal, es mas sencillo crearlos de forma literal que usar el constructor 'new'. Para delimitar un txt, se puede
utilizar comillas simples, comillas dobles o backticks (o comilla invertida o francesa) */

// Declaracion literal
const texto1 = "Hola a todos"
var texto2 = "Otro mensj de texto"
var vacio = ""
var texto3 = "123"      // No es de tipo Number

// Declaracion con el constructor new String
const txt1 = new String("Hola a todos")
var txt2 = new String("Otro mensj de texto")

/* String | Propiedades
.length                 -> Devuelve el numero de caracteres de la variable de tipo str en cuestion

String | Metodos
.charAt(pos)            -> Devuelve el caracter en la posicion pos de la variable
.concat(str1,str2...)   -> Devuelve el texto de la variable unido a str1, str2...
.indexOf(str)           -> Devuelve la primera posicion del texto str
.indexOf(str,from)      -> Idem al anterior, partiendo desde la posicion from
.lastIndexOf(str,from)  -> Idem al anterior, pero devuelve la ultima posicion
*/

/* String | .length y .concat(str1,str2...)
La propiedad .length devuelve el numero de caracteres de una cadena */

var txt = "Hola a todos!"
largo = text.length
console.log(largo)  // 14
// Se puede usar directamente
console.log("Hola".length)  // 4

/* .concat(str1,str2...) concatena cadenas. Su funcion es sumilar al operador '+' */

var cad = "Hola "
var saludo = cad.concat("Codo a Codo!")
console.log(saludo)     // "Hola Codo a Codo"

/* String | charAt(pos)
Charat devuelve el caracter ubicado una posicion determinada dentro del string. Podemos guardarlo en una variable, mostrarlo en el documento o en la consola.
Cada caracter esta almacenado en una posicion */

var cad = "Hola como estas"
document.write("CHARAT <br>")
document.write(cad.charAt(0))       // Devuelve H
var pos1 = cad[1]                   // Almaceno en pos1 el caracter 1("o")
var pos2 = cad[20]                  // Indefinido (No hay elemento en nro 20)
document.write(pos1)                // Devuelve "o"
document.write(pos2)                // Undefinded

/* String | .indexOf() y .lastIndexOf()
.indexOf(str) devuelve la posicion de la primera aparicion de str dentro de la cadena, .indexOf(str,from) hace lo propio, pero a partir de la posicion indicada
por from. Y .lastIndexOf(str,from) devuelve el caracter ubicado a partir de la posicion indicada por from pero partiendo desde el final */

var cad = "Hola como estas"
document.write(cad.indexOf("a"))        // Muestra "3" en el documento HTML
document.write(cad.indexOf("a",4))        // Muestra "13" en el documento HTML
document.write(cad.lastIndexOf("o"))        // Muestra "8" en el documento HTML
document.write(cad.lastIndexOf("o",7))        // Muestra "6" en el documento HTML

/* String | Mas metodos
.repeat(n)              -> Devuelve el txt de la variable repetido n veces
.toLowerCase()          -> Devuelve el txt de la variable en minuscula
.toUpperCase()          -> Devuelve el txt de la variable en mayuscula
.trim()                 -> Devuelve el txt sin espacios a la izq y der
.replace(str,newstr)    -> Reemplaza la primera aparicion del texto str por newstr
.substr(ini,len)        -> Devuelve el subtexto desde la posicion ini hasta ini+len
.substring(ini,end)     -> Devuelve el subtexto desde la posicion ini hasta end
*/

/* String | repeat(n), toLowerCase() y toUpperCase() */

var cad = "Aprendiendo JavaScript "
document.write(cad.repeat(3))

var cad = "Aprendiendo JavaScript "
document.write(cad.toLocaleLowerCase())
var cad = "Aprendiendo JavaScript "
document.write(cad.toUpperCase())

/* String | trim() y replace(str, newstr) */

var cad2 = "    Txt de ejemplo"
alert(cad2.trim())

var cad = "Aprendiendo JavaScript "
document.write(cad.replace("JavaScript", "Python"))

/* String | substr(ini, len) y substring(ini, end) */

var cad = "Aprendiendo JavaScript "
document.write(cad.substr(12, 4))       // Muestra en el documento HTML la subcadena "Java"

var cad = "Aprendiendo JavaScript "
document.write(cad.substring(1, 4))       // Muestra en el documento HTML la subcadena "pre"

/* Plantilla de cadena de caracteres (Template string)
Las Template String utilizan las comillas invertidas para delimitar sus contenidos, en vez de las tradicionales comillas simples o dobles de las cadenas de txt normales.
Sus principales funciones son: Interpolacion de cadenas. Posibilidad de incluir (y evaluar) expresiones dentro de cadenas. Definicion de cadenas de txt en varias lineas
sin tener que usar hacks. Formatear cadenas de manera avanzada. Cadenas etiquetadas */

var saludo = "Hola mundo"       // Ejemplo de Template String

/* Una de las mejores caracteristicas de las Template String es la interpolacion de cadenas. La interpolacion permite utilizar cualquier expresion valida de .js (como por ej la
suma de dos variables) dentro de una cadena y obtener como resultado la cadena completa con la expresion evaluada.
Las partes variables de una Template String se denominan placeholders y utilizan la sintaxis ${...} para diferenciarse del resto de la cadena */

var nombre = "Juan"
console.log('Hola ${nombre}')

/* Como dentro de las partes variables de la cadenas se puede incluir cualquier expresion valida de .js, en la practica sirven para mucho mas que mostrar el contenido
de una variable */

var a = 10
var b = 10
console.log('JavaScript se publico hace ${a+b} años')
console.log('Existen ${2*(a+b)} frameworks JavaScript y no ${10*(a+b)}.')

/* Dentro de un valor interpolado tambien se puede utilizar cualquier funcion. La sintaxis ${} tambien funciona con expresiones que invocan metodos y acceden a propiedades.
La ventaja de usar Template String es el uso de expresiones incrustadas y la posibilidad de interpolacion de cadenas de txt con ellas, facilitando la concatenacion
de valores */


/* Objeto Math. Math es un objeto que tiene propiedades y metodos para constantes y funciones matematicas. Todas las propiedades y metodos de Math son estaticos (no es 
necesario llamar al constructor). Las constantes disponibles son:

Math.E
Math.LN2
Math.LN10
Math.LOG2E
Math.LOG10E
Math.PI
Math.SQRT1_2
Math.SQRT2

Metodos disponibles:

Math.abs(x)
Math.sign(x)
Math.exp(x)
Math.expm1(x)
Math.max(a, b, c...)
Math.min(a, b, c...)
Math.pow(base, exp)
Math.sqrt(x)
Math.cbrt(x)
Math.imul(a, b)
Math.clz32(x)

Math.random() retorna un numero al azar entre los valores 0 y 1, con 16 decimales. Si queremos obtener un numero entero al azar entre los limites a y b, se puede hacer: */

let x = Math.random();      // Numero a al azar entr [0, 1) con 16 decimales
x = x*5;                    // Multiplicamos x por el valor maximo que buscamos
x = Math.floor(x)           // Redondeamos hacia abajo y obtenemos un entero

/* Es muy comun necesitar metodos para redondear numeros y reducir el numero de decimales o aproximarse a una cifra concreta. Para ello, de forma nativa, JavaScript
proporciona los siguientes metodos de redondeo:

Math.round(x)   -> Redondeo de x (el entero mas cercano)
Math.ceil(x)    -> Redondeo superior de x (el entero mas alto)
Math.floor(x)   -> Redondeo inferior de x (el entero mas bajo)
Math.fround(x)  -> Redondeo de x (flotante con presicion simple)
Math.trunc(x)   -> Trunca el numero x (devuelve solo la parte entera)
*/

Math.round(3.75);   // 4
Math.round(3.25);   // 3

Math.ceil(3.75);    // 4
Math.ceil(3.25);    // 4

Math.floor(3.75);   // 3
Math.floor(3.25);   // 3

Math.round(3.123456789);    // 3
Math.fround(3.123456789);   // 3.1234567165374756

Math.trunc(3.75);   // 3
Math.round(-3.75);  // -4
Math.trunc(-3.75);  // -3
