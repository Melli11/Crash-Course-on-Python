# Pregunta 1
# Fill in the blanks of this code to print out the numbers 1 through 7.

# number = 1
# while number <= 7:
# 	print(number, end= " ")
# 	number = number +1

# Pregunta 2
# La función show_letters debe imprimir cada letra de una palabra en una línea separada. Complete los espacios en blanco para que eso suceda.

# def show_letters(word):
# 	for x in word:
# 		print(str(x),end = "\n")

# show_letters("Hello")

# Should print one line per letter

#Pregunta 3

# Completa la función dígitos(n) que devuelve cuántos dígitos tiene el número. 
# Por ejemplo: 25 tiene 2 dígitos y 144 tiene 3 dígitos. Consejo: puedes averiguar los dígitos de un número dividiéndolo por 10 una vez por dígito 
#  hasta que no queden dígitos.

# def digits(n):
# 	count = 0
# 	if n == 0:
# 	  count = 1
# 	while (n>=1):
# 		count += 1
# 		n=n/10
# 	return count


#Pregunta 4 (NO ENTENDI EL REQUEREMIENTO)
# Esta función imprime una tabla de multiplicar (donde cada número es el resultado de multiplicar
# el primer número de su fila por el número en la parte superior de su columna). Completa los espacios en blanco para que al llamar a multiplication_table(1, 3) se imprima:

# def multiplication_table(start, stop):
# 	for x in ___:
# 		for y in ___:
# 			print(str(x*y), end=" ")
# 		print()

# multiplication_table(1, 3)

# Should print the multiplication table shown above
# 1 2 3 

# 2 4 6 

# 3 6 9

#Pregunta 5
# La función de contador cuenta hacia atrás de principio a fin cuando el inicio es mayor que el final, 
# y cuenta hacia adelante de principio a fin en caso contrario. Complete los espacios en blanco para que esto funcione correctamente.

# def counter(start, stop):
# 	x = start
# 	if x >= stop:
# 		return_string = "Counting down: "
# 		while x >= stop:
# 			return_string += str(x)
# 			if x!= stop:
# 				return_string += ","
# 			stop = stop + 1 
# 	else:
# 		return_string = "Counting up: "
# 		while x <= stop:
# 			return_string += str(x)
# 			if x!=stop:
# 				return_string += ","
# 			x = x +1
# 	return return_string

# print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# print(counter(2, 1)) # Should be "Counting down: 2,1"
# print(counter(5, 5)) # Should be "Counting up: 5"

#Pregunta 6
# La función even_numbers devuelve una cadena separada por espacios de todos los números positivos que son divisibles por 2, 
# hasta el máximo que se pasa a la función incluido. Por ejemplo, even_numbers(6) devuelve "2 4 6". Complete el espacio en blanco para que esto funcione.

# def even_numbers(maximum):
# 	return_string = ""
# 	if maximum != 0:
# 		for x in range (2,maximum+1,2):
# 			return_string += str(x) + " "
# 	return return_string.strip()

# print(even_numbers(6))  # Should be 2 4 6
# print(even_numbers(10)) # Should be 2 4 6 8 10
# print(even_numbers(1))  # No numbers displayed
# print(even_numbers(3))  # Should be 2
# print(even_numbers(0))  # No numbers displayed

#Pregunta 7
# The following code raises an error when executed. What's the reason for the error?

# def decade_counter():
# 	while year < 50:
# 		year += 10
# 	return year
# Rta = 
# Failure to initialize variables

#Pregunta 8
# for x in range(1, 10, 3):
#     print(x)

# Rta = 7
#Pregunta 9
# What is the value of y at the end of the following code?
for x in range(10):
    for y in range(x):
        print(y)


#Pregunta 10
# ¿Cómo se debe llamar a esta función para imprimir sí, no y tal vez como posibles opciones para votar?

# def votes(params):
# 	for vote in params:
# 	    print("Possible option:" + vote)
# votes(['yes', 'no', 'maybe']) ##RTA

