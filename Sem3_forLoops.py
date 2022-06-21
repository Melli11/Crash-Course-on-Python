# Ejercicio 1
# Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x (not included).
#  Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).
# Rellena los huecos de la función sum_squares, para que devuelva la suma de todos los cuadrados de los números entre 0 y x (no incluidos). 
# Recuerda que puedes usar la función range(x) para generar una secuencia de números del 0 al x (no incluidos).
# def square(n):
#     return n*n

# def sum_squares(x):
#     sum = 0
#     for n in range (x):
#         sum += square(n)
#     return sum
# print(sum_squares(10)) # Should be 285

# Ejercicio 2
# En matemáticas, el factorial de un número se define como el producto de un número entero y todos los números enteros debajo de él. 
# Por ejemplo, el factorial de cuatro (¡4!) es igual a 1*2*3*4=24. Completa los espacios en blanco para que la función factorial devuelva el número correcto.

# def factorial(n):
#     result = 1
#     for i in range (1,n+1):
#         result = i * result
#     return result
 
# print(factorial(4)) # should return 24
# print(factorial(5)) # should return 120

#Ejercicio 3

# The validate_users function is used by the system to check if a list of users is valid or invalid. A valid user is one that is at least 3 characters long. 
# For example, ['taylor', 'luisa', 'jamaal'] are all valid users. When calling it like in this example, something is not right. Can you figure out what to fix?

# def validate_users(users):
#   for user in users:
#     # if is_valid(users):
#       print(users + " is valid")
#     else:
#       print(users + " is invalid")

# validate_users("purplecat")

# Nota: utiliza la funcion is_valid, que viene definida en el programa

#Eejercicios Quizz

# Pregunta 2 Completa los espacios en blanco para que la función factorial devuelva el factorial de n. Luego, imprime los primeros 10 factoriales (del 0 al 9) con el número correspondiente. 
# Recuerda que el factorial de un número se define como el producto de un número entero y todos los números anteriores.
# Por ejemplo, el factorial de cinco (¡5!) es igual a 1*2*3*4*5=120. Recuerda también que el factorial de cero (0!) es igual a 1

# def factorial(n):
#     result = 1
#     for x in range(1,n):
#         result = result * x
#     return result

# for n in range(0,10):
#     print(n, factorial(n+1))


# Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.
# Escriba un script que imprima los primeros 10 números al cubo (x**3), comenzando con x=1 y terminando con x=10.

for x in range(1,10+1): #debe empezar en 1 pues no existe la potencia = 0
  print(x**3)

# Escriba un script que imprima los múltiplos de 7 entre 0 y 100.
# Imprima un múltiplo por línea y evite imprimir números que no sean múltiplos de 7. Recuerde que 0 también es un múltiplo de 7.

for x in range (0,100+1,7):
    multiplos =+ x
    print (multiplos)

#La función de reintento intenta ejecutar una operación que podría fallar, vuelve a intentar la operación varios intentos.
#  Actualmente, el código seguirá ejecutando la función incluso si tiene éxito. 
# Rellene el espacio en blanco para que el código deje de intentarlo después de que la operación se haya realizado correctamente.

# def retry(operation, attempts):
#   n = 1
#   for n in range(attempts):
#     if operation():
#       print("Attempt " + str(n) + " succeeded")
#       n = attempts
#       break 
#     else:
#       print("Attempt " + str(n) + " failed")

# retry(create_user, 3) 
# retry(stop_service, 5)


