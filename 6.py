#6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase: 
"""• Un constructor, donde los datos pueden estar vacíos. 
• Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos. 
• mostrar(): Muestra los datos de la persona. 
• Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad."""

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def __str__(self):
        return 'Nombre: {} Edad: {} DNI: {}'
        
    def mostrar(self.nombre, self.edad, self.dni)
        if edad >= 21:
            print("mayor de edad")

Juan = Persona ('Juan', '33', '35906989')

print(Juan)