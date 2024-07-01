"""
Estructuras de control

A diario actuamos de acuerdo a la evaluación de condiciones, incluso de manera inconsciente. Si el semáforo está en verde, cruzamos la calle. Si no,
esperamos. También es frecuente evaluar más de una condición a la vez: Si llega la factura de un servicio y tengo dinero, entonces lo pago.
En Python utilizamos las estructuras de control de flujo condicionales para tomar decisiones similares, evaluando expresiones en las que suelen
intervenir variables, para determinar qué parte del código que hemos escrito se va a ejecutar.
También disponemos de bucles, estructuras que permiten que un bloque de instrucciones se repita mientras que una condición sea verdadera.

En programación, las estructuras de control permiten modificar el flujo de ejecución de las instrucciones de un programa. Con ellas se puede:
● Ejecutar un grupo u otro de sentencias, según se cumpla o no una condición (if)
● Ejecutar un grupo de sentencias mientras se cumpla una condición (while)
● Repetir un grupo de sentencias un número determinado de veces (for)

En el código de un programa podemos encontrar estructuras de los siguientes tipos:
● Secuenciales: las instrucciones se ejecutan una después de la otra, en el orden en que están escritas, es decir, en secuencia.
● Condicionales (Selección o de decisión): ejecutan un bloque de instrucciones u otro, o saltan a un subprograma o subrutina según se cumpla o no una condición.
● Iterativas (Repetitivas): inician o repiten un bloque de instrucciones si se cumple una condición o mientras se cumple una condición.

Secuencia   -> A-> B-> C

Seleccion   -> si/no-> A
                    -> B-> C->
        
Iteracion   -> si/no-> A
                    -> B-> C-> si/no(...)
            
Estructuras secuenciales

Las acciones se ejecutan una seguida de la otra, es decir que se ejecuta una acción o instrucción y continúa el control a la siguiente. La ejecución es lineal
y de arriba hacia abajo. Todas las instrucciones se ejecutan una sola vez y finaliza el programa."""

#Programa Suma: suma dos números enteros ingresados por teclado
nro1= int(input("Ingrese el primer número: "))
nro2= int(input("Ingrese el segundo número: "))
suma= nro1 + nro2
print("La suma es:", suma)

"""
El código del ejemplo pide un número, luego pide otro, realiza la suma de ambos valores guardando el resultado en suma y finalmente muestra un mensaje por pantalla.

Estructuras condicionales

Las estructuras condicionales tienen como objetivo ejecutar un bloque de instrucciones u otro en base a una condición que puede ser verdadera
o falsa. La palabra clave asociada a esta estructura es if. Si la condición es True se ejecuta el bloque dentro del if. Luego, independientemente del valor de
verdad de la condición, el programa continúa con la ejecución del resto del programa.

Tipos de Operadores

En la presentación anterior vimos los distintos tipos de operadores que podíamos encontrar en Python:
● Operadores de Asignación
● Operadores Aritméticos
● Operadores de pertenencia
● Operadores Relacionales
● Operadores Lógicos
A continuación, abordaremos los operadores relacionales y lógicos.

Operadores relacionales

Los operadores de relacionales o de comparación se utilizan, como su nombre indica, para comparar dos o más valores. El resultado de estos operadores siempre es T o F.
Donde, los operandos podrán ser variables, constantes o expresiones aritméticas.

Operador    |   Descripcion

    >           Mayor que. Ture si el operando de la izquierda es estrictamente mayor que el de la derecha; False en caso contrario
    >=          Mayor o igual que. True si el operando de la izquierda es mayor o igual que el de la derecha; False en caso contrario
    <           Menor que. True si el operando de la izquierda es estrictamente menor que el de la derecha; False en caso contrario
    <=          Menor o igual que. True si el operando de la izquierda es menor o igual que el de la derecha; False en caso contrario
    ==          Igual. True si el operando de la izquierda es igual que el de la derecha: False en caso contrario
    !=          Distinto. True si los operadores son distintos; False en caso contrario

Operadores lógicos

Se utiliza un operador lógico para tomar una decisión basada en múltiples condiciones. Los operadores lógicos utilizados en Python son and, or y not.

OPERADOR    DESCRIPCIÓN                                       USO

and         Devuelve True si ambos operandos son True         a and b
or          Devuelve True si alguno de los operandos es True  a or b
not         Devuelve True si el operandos False, y viceversa  not a

a y b son expresiones lógicas. Cada una de ellas puede ser verdadera o falsa. Si a y/o b son valores numéricos, se tratan como True o False según su valor sea cero o no.

Estructura condicionales | if """

nota = float(input("Ingrese la calificación: "))
if nota >= 7:
    print("Aprobado.")

"""
Estructuras condicionales | if .. else

En Python podemos utilizar la cláusula else para determinar un grupo de instrucciones que se ejecutará en caso de que la evaluación de la condición resulte ser falsa.
Con este agregado, una estructura if tiene la posibilidad de ejecutar un bloque de instrucciones u otro, dependiendo de si la condición es verdadera o falsa."""

edad = float(input("Ingrese su edad: "))

if edad >= 18:
    print("Puedes pasar.")
else:
    print("No admitido.")

"""
Estructuras condicionales anidadas

En una estructura condicional anidada, cada else se corresponde con el if más próximo que no haya sido emparejado, y deben tener la misma indentación.
En el esquema anterior, se evalúa primero la condición 1. En caso de ser falsa se ejecuta el Bloque3 que se encuentra en su else, y finaliza la ejecución de la estructura.
En caso de que la condición 1 sea verdadera, se procede a evaluar la condición 2, que se encuentra dentro (anidada) del primer if.
Si la segunda condición resulta verdadera se ejecuta el Bloque3, si resulta falsa se ejecuta el Bloque2.

Estructuras condicionales | if .. elif .. else

A menudo solemos hacer una pregunta a partir de la respuesta de una pregunta anterior. Python tiene una estructura adecuada para implementar este
comportamiento, y se conoce como if .. elif .. else.
La sección de código dentro del elif se ejecuta cuando la condición del primer if ha resultado ser falsa (False) y la condición del elif es verdadera (True). Si la
condición del elif es falsa, entonces se ejecuta el código del bloque else. Además, en situaciones más complejas se pueden utilizar múltiples instancias
de elif, dando lugar a estructuras condicionales elaboradas y que permiten resolver prácticamente cualquier situación, aunque utilizando varios bloques de
instrucciones diferentes."""

nota = 5
if nota >= 0 and nota < 4:
    print("Insuficiente.")
elif nota >=4 and nota < 7:
    print("En proceso.")
else:
    print("Suficiente")

"""
Estructuras condicionales

Se pueden utilizar operadores lógicos para tomar una decisión basada en múltiples condiciones, reduciendo la cantidad de ifs anidados."""

#if con operadores logicos
condición1 = 1
condición2 = 2
if (condición1) and (condición2):
    condición1+condición2
if (condición1) or (condición2):
    condición2-condición1

"""
Las tablas de verdad muestran los valores de verdad de una proposición en función del valor lógico de sus operadores.

Cond 1  Cond 2   Y(and)
V       V        V
V       F        F
F       V        F
F       F        F

Cond 1 Cond 2    O(or)
V      V         V
V      F         V
F      V         V
F      F         F

Cond   NO(not)
V      F
F      V

Estructuras condicionales | and

Veamos un ejemplo de un condicional con and:
En un aviso del diario piden ingenieros en sistemas con 5 años de experiencia como mínimo, para ocupar un puesto laboral. A la convocatoria se presenta:
● Un licenciado en sistemas con 6 años de experiencia: NO LO TOMAN, pues la primera condición es falsa.
● Un ingeniero en sistemas con 4 años de experiencia: NO LO TOMAN, pues la segunda condición es falsa.
● Un analista programador con 4 años de experiencia: NO LO TOMAN, pues las 2 condiciones son falsas.
● Un ingeniero en sistemas con 7 años de experiencia: LO TOMAN, pues las 2 condiciones son verdaderas.

Estructuras condicionales | or

Veamos un ejemplo de un condicional con or:
Tengo invitados en casa y voy a comprar 1 kilo de helado. Sé que los únicos gustos que comen son chocolate o vainilla. Después de ir a varias heladerías encontré:
● Hay chocolate pero no hay vainilla. LO COMPRO, pues la primera condición es verdadera.
● Sólo hay vainilla, no chocolate. LO COMPRO, pues la segunda condición es verdadera.
● Hay chocolate y vainilla. LO COMPRO, pues las dos condiciones son verdaderas.
● Hay crema americana y dulce de leche. NO LO COMPRO, pues ninguna de las condiciones es verdadera.

Estructuras repetitivas

Repiten un código dependiendo de una condición o de un contador. Si se cumple la condición se ejecuta un bloque de código y se comprueba
nuevamente la condición. Pueden ser de dos clases:
● Ciclos Exactos: Conocemos la cantidad exacta de repeticiones. Ese valor es aportado al iniciar el programa o por el usuario antes de que se
inicie el ciclo. Los bucles While y For pertenecen a este grupo.
● Ciclos Condicionales: No se conoce de antemano la cantidad de repeticiones. Dependen de una condición que puede variar. Finaliza
cuando la condición es falsa. Se puede repetir una vez, varias veces o ninguna vez. En este grupo se encuentra el bucle While.

Estructuras repetitivas | While

Ejecuta un bloque de código mientras la condición del while es verdadera. Finaliza cuando la condición es falsa, y no sabemos de antemano el número de veces que
se va a repetir.

while condición:
    sentencia 1
    sentencia 2
siguiente sentencia fuera del while

Podemos usar contadores (se incrementan o decrementan en 1 en cada ciclo) y acumuladores (suman algún valor en cada ciclo)."""

cont= 1
suma= 0
while cont <= 5:
    num= int(input("Ingrese un número: "))
    suma = suma + num # Acumulamos, es equivalente suma += num
    cont = cont + 1 # Incrementamos, es equivalente cont += 1
print("La suma es:", suma)
print("El promedio es:", suma/cont)

"""
Estructuras repetitivas | For

Esta estructura se utiliza cuando sabemos la cantidad de repeticiones a efectuar. Tiene el siguiente formato:

for i in range(inicio, fin, paso):
    sentencia1
    sentencia2
primer sentencia fuera del for

i: variable que incrementa su valor en paso unidades en cada iteración.
inicio: Es el valor inicial de i
fin: El ciclo se repite mientras i sea menor que fin.
paso: valor en que se incrementa i en cada iteración.

Si solo se escribe un número en range, indica el valor de fin (inicio y paso se asumen 1). Si se escriben dos valores, se asume que son el de inicio y fin y que paso es uno.
for i in range(fin):         -> Se asume que inicio = 0 y paso = 1
for i in range(inicio, fin): -> Se asume que paso = 1

Con el bucle for no necesitamos usar contadores, ya que la variable del ciclo asume esa función. Esto permite escribir algunos programas de una manera más compacta. """

suma= 0
for cont in range(5):
    num= int(input("Ingrese un número: "))
    suma = suma + num # Acumulamos, es equivalente suma += num
print("La suma es:", suma)
print("El promedio es:", suma/(cont+1))

"""
Estructuras repetitivas | Break

Break permite salir de un bucle for o while en el momento que se cumpla alguna condición. Sin embargo, break puede evitarse, y su uso no se considera una buena práctica."""

# Break en un bucle for
suma= 0
for cont in range(15):
    print(cont)
    suma = suma + cont
    if cont == 3:
        break
print("La suma es:", suma)

# Break en un bucle while
cont= 0
suma= 0
while cont < 15:
    print(cont)
    suma = suma + cont
    if cont == 3:
        break
    cont = cont + 1
print("La suma es:", suma)

