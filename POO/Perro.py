class perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def ladrar(self):
        print(f"{self.nombre} esta ladrando: ¡Guau, guau")
        
mi_perro = perro("Rex", "Pastor Aleman")
mi_perro.ladrar()
print(f"El perro se llama: {mi_perro.nombre} su raza es: {mi_perro.raza}")