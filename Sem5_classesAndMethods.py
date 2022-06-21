# Instance Methods (Optional)

# Bien, ¡ahora es tu turno! Intenta escribir métodos para una clase. 
# Cree una clase Dog con dog_years basada en la clase Piglet que se muestra antes (un año humano es aproximadamente 7 años de perro).

class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7
    
fido =Dog()
fido.years=3
print(fido.dog_years())


# Constructors and Other Special Methods (Optional)

# ¿Quieres ver esto en acción? En este código, hay una clase Person que tiene un nombre de atributo, que se establece al construir el objeto.
#  Rellene los espacios en blanco para que
#  1) cuando se cree una instancia de la clase, el atributo se establezca correctamente y
#  2) cuando se llame al método greeting(), el saludo indique el nombre asignado.

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        aux = "hi, my name is {}".format(self.name)
        # Should return "hi, my name is " followed by the name of the Person.
        return aux 

# Create a new instance with a name of your choice
some_person = Person("Martin")  
# Call the greeting method
print(some_person.greeting())


# Documenting Functions, Classes, and Methods (Optional)

# ¿Recuerdas nuestra clase Person del último video? 
# Agreguemos una cadena de documentación al método de saludo. ¿Qué tal, "Emite un mensaje con el nombre de la persona".

class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person)
