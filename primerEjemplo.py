# print("algo")
# print((((1+2) * 3)/4) **5)
# correr programa en consola : Py primerEjemplo.py
print(26 **6)
#imprimir tipo
print(type("Cadena"))
# imprime en pantalla <class 'str'>
bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total/2 
print("Each person needs to pay:"+str(share))
# practica de funciones
def funcionPractica(nombre,barrio):
    print ("Hola soy " + nombre)
    print ("de " + barrio)

# Ejecuto funcion
funcionPractica("Martin","Bajo Flores")

# # Ejercicio practico
# def get_seconds(hours, minutes, seconds):
#   return 3600*hours + 60*minutes + seconds

# amount_a = get_seconds(2,30,0)
# amount_b = get_seconds(0,45,15)
# result = amount_a + amount_b
# print(result)

# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
def month_days(month,days):
    print(month + "has" + str(days))

month_days("June",30)
month_days("July",33)


# june_days = 30
# print("June has " + str(june_days) + " days.")
# july_days = 31
# print("July has " + str(july_days) + " days.")

# Esta función para calcular el área de un rectángulo no es muy legible. ¿Puede refactorizarlo y luego llamar a la función para calcular el área con base de 5 y altura de 6?
#  Sugerencia: una función que calcula el área de un rectángulo probablemente debería llamarse rectángulo_área, y si está recibiendo la base y la altura, así deberían llamarse los parámetros.

# def rectangle_area(base, height):
# 	rectangle_area = base*height # the area is base*height
# 	print("The area is " + str(rectangle_area))
# rectangle_area (5,6)

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km
my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str((my_trip_km)*2))

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller,bigger = order_numbers(100, 99)
print(smaller, bigger)

def lucky_number(name):
  number = len(name) * 9
  msj= "Hello " + name + ". Your lucky number is " + str(number)
  return msj
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))

print("A dog" > "A mouse")
print(9999+8888)
print(100*100)
print(9999+8888 > 100*100)
print ("big" > "small")
print((10 >= 5*2) and (10 <= 5*2))
print(5//4)
# # HOLASOYPRIMERCOMNEY
# Usando if, elif ,else y operadores 
# def number_group(number):
#   if number > 0:
#     return "Positive"
#   elif number == 0:
#     return "Zero"
#   else:
#     return "Negative"

# print(number_group(10)) #Should be Positive
# print(number_group(0)) #Should be Zero
# print(number_group(-5)) #Should be Negative