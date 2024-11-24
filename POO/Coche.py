class Coche:
    def __init__(self,marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False
        
    def encender(self):
        self.encendido = True
        print(f"El {self.marca} {self.modelo} esta encendido")
        
    def apagar(self):
        self.encendido = False
        print(f"El {self.marca} {self.modelo} es apagado")
        
mi_coche = Coche("Toyota", "Corolla", 2022)
mi_coche.encender()
mi_coche.apagar()
                