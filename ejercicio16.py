def NuevoTotal(cantidad, iva = 21):
    montototal = cantidad + cantidad * iva / 100
    return montototal
print(NuevoTotal(1000,10))
print(NuevoTotal(1000))
