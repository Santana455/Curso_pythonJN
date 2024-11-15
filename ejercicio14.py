import random
numero_secreto = random.randint(1,100)
intento=None
print("Adivina el numero  1 Y 100")

while intento!=numero_secreto:
    intento = int(input("Introduce el numero: "))
    if intento<numero_secreto:
        print("El numero es mayor: ")
    elif intento>numero_secreto:
        print("El numero es menor: ")
    else:
        print("FELICIDADES ADIVINASTES EL NUMERO: ")
                 