import random
numero_secreto = random.randint(1,100)
intento=None
print("¡ADIVINA EL NUMERO SECRETO ENTRE 1 Y 100")

while intento!=numero_secreto:
    intento = int(input("Introduce tu intento: "))
    if intento<numero_secreto:
        print("El numero es mayor: ")
    elif intento>numero_secreto:
        print("El numero es menor: ")    
    else:
        print("Felicidades has adivinado: ")    
