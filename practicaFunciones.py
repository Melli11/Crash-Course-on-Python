
# Ejemplo 1 
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

# Ejemplo 2

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