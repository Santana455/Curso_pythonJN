from gerente import Gerente
from programador import Programador

def main():
    #nombre, id_empleado, salario, departamento
    gerente = Gerente("Calos Perez", 101,2000, "Recursos Humanos")
    #nombre, id_empleado, salario, departamento, lenguajes
    programador = Programador("Juan", 3,3000, "Sofware",["Python", "35", "Java"] )
    
    print("INFORMACION DEL GERENTE")
    gerente.mostrar_informacion()
    
    print("\n.........................\n")
    print("Informacion del Programador")
    programador.mostrar_informacion()
    
    main()
