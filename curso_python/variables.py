# Variables y tipos de datos

""" Comentario|
Las variables son "contenedores" donde almacenamos datos o información.
En python, las variables son nombres o etiquetas que hacen referencia al objeto o valor asignado.
Puedes usar el mismo nombre de variable para referenciar diferentes tipos de datos,
python es un lenguaje dinámicamente tipado
"""
# Se usa el simbolo = para asignar un valor a una variable, este valor puede ser literal o una expresion (código que se ejecuta)

# variable = literal o expresión
literal = "Hola, soy un texto 'fijo'"
print(literal)

# Importando un modulo que nos devuelve fechas y horarios
import datetime
expresion = datetime.datetime.now()
print(expresion)

''' Reglas para definir variables

    1.- Los nombres sólo pueden contener caracteres alfanúmericos
    2.- Debe iniciar con una letra o con una barra baja (_)
    3.- No puede iniciar con un número ni incluir espacios 
    4.- Python es case-sensitive (distingue mayúsculas y minúsculas)
    5.- Se recomienda usar un nombre que describa el dato a guardar
    6.- Podemos usar camelCase (primer palabra minúsculas y primer letra    sig. palabra en Mayúscula)
        o snake_case (todo en minuscúlas separado las palabras con _ )
    7.- No podemos usar las palabras reservadas en Python
'''
""" 
    Nombres válidos

    _nombre = "Toño"
    numero_seis6 = 6
    cadenaTexto42 = "changoleon56"
    print(_nombre)

    ##################

    Nombres no válidos

    -gato = "Tomy"
    }puma = "Rosa"
    .marca = "Tesla"
    1uno 2dos = 1
"""



# # Nos muestra las palabras reservadas en Python
# import keyword
# print("Las palabras reservadas en Python son:\n", keyword.kwlist)
# print()

# # Tipos de datos Inmutables 
# # Una vez creados su estado no se puede cambiar

#  # Strings o cadena de caracteres
#  # STR

# """ Función input()
#  Permite obtener datos del usuario
#  Por defecto devuelve un dato de tipo str()
#  Podemos imprimir un texto o mensaje    
# """ 
# nombre = input("Escribe tu nombre: ")
# nombre = nombre.capitalize()
# print(f"Bienvenido, {nombre}")

# # texto = "Cadena de texto"
# # texTo = 'cadena de texTo'
# # texto_multiple = """ 
# # El Texto              se guarda
# # tal           y       como
# # se escribe        .       """

# # Operaciones con cadenas de texto

# """ Concatenación de cadenas """

# nombre = "Edgar"
# apellido = "Hernández"
# nombre_completo = nombre + " " + apellido
# # print(nombre + 77)
# print(nombre_completo)


# # # Integers o enteros
# # INT
# x = 1234533 
# o = 1_123_455_654_345
# print(o)
# print(type( x + 3.14))

# # # float o punto flotante
# y = 6.1433333
# z = 6.0
# c = 6.
# d = float(6)
# print(type(d))

# # Python sigue una jerarquia de operaciones
# """
#     () []   Paréntesis y corchetes
#     ** 1/2  Potencias y Raices 
#     * /     Multiplicación y división
#     + -     Suma y resta
# """



# # Operadores aritmeticos 
# # Se pueden usar con INT y Float

# num1 = 400
# num2 = 20
# print(""" \nOperadores aritméticos \n """)
# # print("suma: ", num1 + num2)
# print(f"suma: {num1 + num2}")

# print(f"resta: {num1 - num2}")
# print(f"multiplicación: {num1 * num2}")
# print(f"división: {num1 / num2}")
# print(f"potencia: {num1 ** num2}")
# print(f"La parte entera de la división de 10 / 3 es: {10 // 3}")
# print(f"El resto de la division de 10 / 3 es: { 10 % 3}")





# # # Boolean
# """
#  Los booleanos sólo pueden contener dos valores:
#  verdadero (True) o falso (False)
#  En ausencia de valores o si existe un 0 se interpreta como False
#  Cualquier valor diferente de 0 devolvera True
# """
# on = True
# print(bool())
# print(bool(0))
# print(bool(2))
# print(bool("w"))
# print(bool(""))

# # Operadores relacionales

# """
# Podemos realizar comparaciones entre objetos en python.
# El resultdo de la comparación será un valor booleano.
# """

# print("""\nOperadores relacionales\n""")
# print(f"Mayor que: {1 > 2}")
# print(f"Menor que: {1 < 2}")
# print(f"Igual a: {1 == 1}")
# print(f"Mayor o igual que: {1 >= 2}")
# print(f"Menor o igual que: {1 <= 2}")
# print(f"Distinto a: { 1 != 2}")

# # Operadores lógicos

# print("""\nOperadores lógicos\n""")

# # Operador de negacion ( Lo contrario a )

# falso = not True
# print(falso)

# # Operador de disyunción ( solo uno debe ser verdadero )

# booleano = 1 > 2 or 2 > 1
# print(booleano)

# # Operador de conjunción

# variable = 1 < 3 and 2 > 1
# print(variable)


# print("""\nOperador Ternario\n""")
# # Operador ternario
# credit = 200
# print("Cargo aceptado") if credit > 210 else print("Saldo insuficiente")


# # Conversion de tipos

# uno = 1
# uno_texto = str(uno)
# uno_decimal = float(uno)
# uno_boolean = bool(uno)
# print(uno_decimal)
# print(uno_boolean)
# print(uno_texto + " " + "concatenado")
# # print(uno + " " + "concatenado")
# print(uno)

# num = input("Ingresa un número: ")
# num2 = input("Suma un número: ")
# # El dato devuelto por input es de tipo string, tenemos que convertirlo a integer
# print(f"El resultado sin cambiar el tipo de dato es: { num + num2}")
# print(f"El resultado correcto es: {int(num) + int(num2)}")



