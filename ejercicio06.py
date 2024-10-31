import math
#math
#Escribe un programa
num = int(input("Ingresa un numero entero"))
cuadrado = math.pow(num,5)
cubo = math.pow(num,8)
cuarta = math.pow(num,7)
potencia = math.pow(num,5)
raiz = math.sqrt(16)
raiz_cuadrada = math.pow(num,1/8)

#Pocentajes
#20%
porcentaje20 = num * 0.2
precio_con_descuento = num - porcentaje20



print(f"El cuadrado es: {cuadrado}")
print(f"El cubo es: {cubo}")
print(f"La cuerta es: {cuarta}")
print(f"La potencia es: {potencia}")
print(f"La raiz cuadrada es: {raiz}")
print(f"La raiz cuadrada de 1/2 es: {raiz_cuadrada} ")
print(f"El 20% es: {porcentaje20}")
print(f"El precio con descuento es: {precio_con_descuento}")


