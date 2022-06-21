# Repita el enunciado del problema del ejemplo del video.

# Opciones:

# Cada evento de inicio de sesión es una instancia de la clase de evento. 

# Los atributos de la clase Evento son fecha, usuario, máquina y tipo.

#  El gerente de la empresa quiere saber qué usuarios están actualmente conectados a qué máquinas.

#  Necesitamos procesar una lista de objetos de evento utilizando sus atributos para generar un informe que enumere  <----RTA
#  todos los usuarios que actualmente iniciaron sesión en las máquinas.

# ------------------------------------------------------------------------------------------------------------------------------------

#Hay dos métodos estándar para ordenar una lista en Python, ordenar y ordenar. ¿Cuál es la diferencia entre estos dos métodos?

# Opciones:

# sort devuelve una nueva lista, mientras que sorted devuelve la misma lista reorganizada. 

# sort  lista alfabéticamente, mientras que las listas ordenadas por longitud de palabra.

# sorted devuelve una nueva lista, mientras que sort devuelve la misma lista reorganizada. <---RTA

# ------------------------------------------------------------------------------------------------------------------------------------
# Tener un plan es la mitad de la batalla. Al planificar su programa, ¿por qué suele ser una buena idea separar las funciones? 

# Opciones:

# Simplifica la realización de cambios y la corrección de errores.

# Nos permite utilizar la misma función para múltiples propósitos. 

# Facilita la clasificación de listas.

# Tanto A como B. <----RTA


# Es importante saber por qué hemos escrito una función. En el ejemplo utilizado en el video (que se muestra aquí), ¿cuál es el propósito de "si len (usuarios)> 0:" ?
def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

# Se asegura de  no imprimir ninguna máquina en la que nadie haya iniciado sesión actualmente  <------- RTA
# Genera una cadena de usuarios registrados para una máquina determinada 
# Ordena la lista de usuarios 
# Iterar sobre las claves y valores en el diccionario


# ¿Qué línea del programa que acabamos de escribir combina cada atributo de usuario registrado en una variable?

#  eventos.sort(key=get_event_date) 
# self.usuario = usuario
#  user_list = ", ".join(usuarios) <--RTA
#  máquinas[evento.máquina].add(evento.usuario)
