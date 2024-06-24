// Declaracion de la funcion 'saludar'
function saludar() {
    // Nombre simple, claro, representativo de la tarea que realiza, verbo inf, nomeclatura camelCase
    // Contenido de la funcion
    console.log ("Hola, soy una funcion")
}
// Ejecucion de la funcion
saludar()


// Tabla multiplicacion de 5
for (i = 1; i <= 10; i++) {
    console.log("1x", i, "=", 5*i)
}

// Tabla de multiplicar por 5 tres veces. Codigo repetido
for(i = 1; i <= 10; i++) {console.log("5x", i, "=", 5*i)}
for(i = 1; i <= 10; i++) {console.log("5x", i, "=", 5*i)}
for(i = 1; i <= 10; i++) {console.log("5x", i, "=", 5*i)}

// Solucion codigo anterior
function tablaDelCinco(){
    for(i = 1; i <= 10; i++) {console.log("5x", i, "=", 5*i)}   // Codigo que itera 10 veces
}
// Codigo que itera 3 veces
for(i = 1; i <= 3; i++) {tablaDelCinco}


// Funciones con parametros/argumentos
function sumar (a, b) {     // A y B son parametros
    console.log (a + b)
}
// Llamo funcion
var suma = sumar(7, 4)      // 7 y 4 son argumentos, reemplazan A y B

// Funcion con un solo parametro que indica hasta que valor calculara
function tablaMultiplicar(hasta) {
    for (var i = 1; i <= hasta; i++)
        console.log ("1x", i, "=", 1 * i)
}
tablaMultiplicar(4)

// Funcion muestra un texto concatenado a un argumento pasado por parametro
function saludarDos(miNombre) {
    console.log("Hola " + miNombre)
}
saludarDos("Eduardo")   // Argumento Fijo
var nombre = prompt("Ingrese su nombre")
saludarDos(nombre)      // Argumento variable

// Funcion con dos parametros, el valor de la tabla a generar y hasta que valor calcular
function tablaMultiplicarNueva(tabla, hasta) {
    for (var i = 1; 1 <= hasta; i++)
        console.log(tabla + " x " + i + " = ", tabla *i)
}
tablaMultiplicarNueva(1, 10)    // Tabla del 1, desde el 1 hasta el 10
tablaMultiplicarNueva(5, 8)     // Tabla del 5. desde el 1 hasta el 8

// Funcion con tres parametros, se evalua la mayoria de edad de una persona
function mayoriaEdad(miApellido, miNombre, miEdad) {
    console.log("Apellido y nombre: " + miApellido + ", " + miNombre)
    if(miEdad >+ 18) {
        console.log("Es mayor de edad " + "(" + miEdad + ")")
    }
    else {
        console.log("No es mayor edad " + "(" + miEdad + ")")
    }
}
var ape= prompt ("Ingrese su apellido")
var nom= prompt ("Ingrese su nombre")
var edad= prompt ("Ingrese su edad")
mayoriaEdad(ape, nom, edad)

// Parametros predeterminados
function multiplicar(a, b = 3) {
    return a * b;
}
console.log(multiplicar(5, 2));     // Salida: 10
console.log(multiplicar(5));        // Salida: 15

// Devolucion de valores 'return'
var suma = function sumar(numero1, numero2) {       // Al retornar un valor, esta se guarda en la variable suma
    return numero1 + numero2
}
console.log(suma(40,15))

var numeroMaximo = function(valor1, valor2) {       // En este caso se piden dos valores y si la condicion no se cumple se asume que el valor2 es el maximo (no es necesario un else)
    if(valor1 > valor2) { return valor1 }
    return valor2
}
var v1= parseInt(prompt("Ingrese un numero entero"))
var v2= parseInt(prompt("Ingrese otro numero entero"))
console.log("El numero maximo es:", numeroMaximo(v2,v2))


// Funcion flecha (=>), en js es una abreviacion a las funciones simples
function cuadrado(x) {
    return x*x
}
console.log(cuadrado(2))
// Funcion flecha
var aCuadrado = x => x*x
console.log(aCuadrado(2))


// Funciones Anonimas
const saludo = function() {
    return "Hola"
}
const saludo2 = function(nombre) {
    var mensaje = "Hola " + nombre
    return mensaje
}


/* let vs var -> let declara una variable de alcance global, limitando su alcance (scope) al bloque, declaracion, o expresion donde se esta usando.
var define una variable global o local en una funcion sin importar el ambito del bloque */
var a = 5
var b = 10
if (a === 5) {
    let a = 4       // El alcance es dentro del bloque if
    var b = 15      // El alcance es global, sobreescribe a 10
    console.log(a)  // 4, por alcance a nivle de bloque
    console.log(b)  // 15, por alcance global
}
console.log(a)      // 5, por alcance global
console.log(b)      // 15, por alcance global


/* callbacks. Las funciones en .js son objetos. Como cualquier otro objeto, se pueden pasar como parametros. Podemos usar una funcion como argumento de otra funcion.
Esto se llama funcion de devolucion de llamada (callback). Las funciones tambien se pueden devolover como resultado de otra funcion */
function saludarTres(nombre) {
    alert('Hola ' + nombre)
}
function procesarEntradaUsuario(callback) {
    var nombre = prompt( 'Por favor ingrese tu nombre. ')
    callback(nombre)
}
procesarEntradaUsuario(saludar)


/* Clausuras (clousure). La funcion iniciar() crea una variable local llamada nombre y una funcion interna llamada mostrarNombre(). Por ser una funcion interna, esta
ultima solo esta disponible dentro de iniciar(). mostrarNombre() no tiene ninguna variable propia; pero puede acceder a la variable nombre declarada en la funcion iniciar() */
function iniciar () {
    var nombre = "Codo a Codo"      // La variable es una var local creada por iniciar()
    function mostrarNombre() {      // La funcion mostrarNombre es una funcion interna, una clausura
        alert(nombre)               // Usa una variable declarada en la funcion externa
    }
    mostrarNombre()
}
iniciar()

function creaSumador(x) {
    return function(y) {
        return x + y;
    };
}
var suma5 = creaSumador(5);
var suma10 = creaSumador(10);

console.log(suma5(2));      // Muestra 7
console.log(suma10(2));     // Muestra 12
