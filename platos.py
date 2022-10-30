##############################################################
from random import randint, choice
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 1.1 ###
class Plato():
    def __init__(self, nombre:str, calidad, dificultad) -> None:
        self.nombre = nombre
        self.calidad = calidad
        self.dificultad = dificultad

### FIN PARTE 1.1 ###

### INICIO PARTE 1.2 ###
class Bebestible(Plato):
    def __init__(self, nombre, calidad, dificultad, tamano):
        super.__init__(nombre, calidad, dificultad)
        self.tamano = tamano
### FIN PARTE 1.2 ###

### INICIO PARTE 1.3 ###
class Comestible(Plato):
    def __init__(self, nombre, calidad, dificultad, cubiertos):
        super.__init__(nombre, calidad, dificultad)
        self.cubiertos = cubiertos
### FIN PARTE 1.3 ###


if __name__ == "__main__":
    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        un_bebestible = Bebestible("Coca-Cola")
        un_comestible = Comestible("Sopa")
        print(f"Esto es una {un_bebestible.nombre} de tamaño {un_bebestible.tamano} y calidad {un_bebestible.calidad}.")
        print(f"Esto es una {un_comestible.nombre} de dificultad {un_comestible.dificultad} y calidad {un_comestible.calidad}.")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
