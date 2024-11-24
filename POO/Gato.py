from Animal import animal

class Gato(animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color
    
    def hacer_sonido(sef):
        print(f"{sef.nombre} dice ¡Miau!")
        
mi_gato = Gato("Pelusa", "Oscuro")
mi_gato.hacer_sonido()
     