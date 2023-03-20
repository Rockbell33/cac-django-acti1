#7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase: 
"""• Un constructor, donde los datos pueden estar vacíos. 
• Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. 
• mostrar(): Muestra los datos de la cuenta. 
• ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
• retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.""" 

class Cuenta:
    def __init__(self, titular, cantidad):
        self.__titular = titular
        self.__cantidad = 0

    @property
    def __str__(self):
        print("{} tiene depositada la suma de{}".format(self._titular, self._cantidad))

    def ingresar(self, cantidad):
        self.cantidad=self.cantidad+cantidad
        if cantidad<0:
            print('sin cambios')

    def retirar(self, cantidad):
        self.cantidad=self.cantidad-cantidad
        print("\033[31mCuenta\033[0m")

#_____________________________________________________________________________________________________

#8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase: 
"""• Un constructor. 
• Los setters y getters para el nuevo atributo. 
• En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario. 
• Además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
• El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta."""


class CuentaJoven (Cuenta):
    def __init__(self, titular, cantidad, edad, bonificacion):
        self.__edad = edad
        self.__bonificacion = 0

    
    @property
    def titular_valido(self.edad)
        if self.edad >= 21 and <=25
            return(True)
        else:
            return(False)

    def __str__(self):
        print("{} CuentaJoven {}".format(self._titular, self._bonificacion))

    def retirar(self, cantidad):
        if titular_valido(true)
        return super().retirar(cantidad)