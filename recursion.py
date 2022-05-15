
#recursión
# caso base : es la condicion de corte recursivo
# caso recursivo = donde la f se llama a si misma


#ejemplo 1
# La función suma_números_positivos debe devolver la suma de todos los números positivos entre el número n recibido y 1. 
# Por ejemplo, cuando n es 3, debe devolver 1+2+3=6, y cuando n es 5, debe devolver 1+2+3 +4+5=15. Rellena los huecos para que esto funciones

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

#Quizz Ejercicios

# Pregunta 3 Completa los espacios en blanco para que la función is_power_of devuelva si el número es una potencia de la base dada. Nota: se supone que la base es un número positivo. 
# Sugerencia: para las funciones que devuelven un valor booleano, puede devolver el resultado de una comparación.

#  def is_power_of(number, base):
#   # Base case: when number is smaller than base.
#   if number < base:
#     # If number is equal to 1, it's a power (base**0).
#     return __

#   # Recursive case: keep dividing number by base.
#   return is_power_of(__, ___)

# print(is_power_of(8,2)) # Should be True
# print(is_power_of(64,4)) # Should be True
# print(is_power_of(70,10)) # Should be False

# La función count_users cuenta recursivamente la cantidad de usuarios que pertenecen a un grupo en el sistema de la empresa, pasando por cada uno de los miembros de un grupo 
# y si uno de ellos es un grupo, llama recursivamente a la función y cuenta los miembros. ¡Pero tiene un error! ¿Puedes detectar el problema y solucionarlo?

