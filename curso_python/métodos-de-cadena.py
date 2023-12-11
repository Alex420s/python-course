# Métodos de tipo string

""" Funcion len()
 Toma un input o un argumento y regresara el número
 de caracteres en la cadena

"""

# nombre = input("Escriba su nombre: ")
# mensaje = input("Escriba su mensaje (max 20 caracteres): ")

# mensaje_correcto = " "
# error = "El mensaje es demaciado largo :("

# # Operador ternario para aceptar datos
# mensaje_correcto += mensaje if len(mensaje) < 20 else mensaje_correcto + error
# print(mensaje_correcto)




# Acceder a un carácter de nuestro string por su posición
cadena = "012345"
print(cadena[4])

# Podemos acceder usando valores negativos -1 para la última letra y restamos uno para acceder a la letra anterior
string = "543210"
print(string[-5])

# Método slicing

# Slicing "una rebanada" de esa cadena 
texto=  "suscríbete al canal"

# Imprime desde el principio al final de la cadena
print(texto[:])

# Es equivalente a [:]
x = len(texto)# Esta funcion nos devuelve el número de carácteres de nuestra cadena

print(texto[0:x])