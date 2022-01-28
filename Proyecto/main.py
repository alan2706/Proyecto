from ast import While
from helpers import Helper
from cargo import Cargo
from empleado import Empleado
from departamento import Departamento
import os


def buscacargo(cod):
    cod=int(cod)
    cat = 0     
    for pos in range(0,len(Cargo.cargos)):
        cargos = Cargo.cargos[pos]
        if cargos["codigo"] == cod:
            cat = cargos["cargo"]
            break
    return cat 
def buscadepartamento(depa):
    depa=int(depa)
    cat=0
    for pos in range(0,len(Departamento.departamentos)):
        departamento=Departamento.departamentos[pos]
        if departamento["codigo"]== depa:
            cat=departamento["departamento"]
            break
        return cat
       
helper = Helper()
lista=["1) Cargo","2) Departamentos","3) Empleados","4) Salir"]
opcion=""
while opcion != "4":
    os.system("clear")
    opcion = helper.menu(lista,"Menu Ficha Personal")
    if opcion == "1":
        opc1=""
        while opc1 != "3":
            os.system("clear")
            print("*"*20,"Mantenimento De Cargo","*"*20)
            opc1 = helper.menu(["1) Ingreso","2) Consulta","3) Salir"],"")
            os.system("clear")
            if opc1 == "1":
                print("*"*20,"Ingreso de Cargos","*"*20)
                nombre=input("Nombre del cargo:")
                while ((len (nombre))>20 or (len (nombre))<1):
                    print("Puedes ingresar de 1 a 20 caracteres, intentalo de nuevo.")
                    nombre=input("Nombre del cargo:")
                    os.system("clear")
                    print("*"*20,"Ingreso de Cargos","*"*20)
                car = Cargo(nombre)
                car1 = car.registro()
                Cargo.cargos.append(car1)
                input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
            elif opc1 == "2":
                print("*"*20,"Consulta de Cargos","*"*20)
                print("Codigo"," "*5,"Descripción")
                for car in Cargo.cargos:
                    cod=car["codigo"]
                    des=car["cargo"]
                    print(" "*2,cod," "*8,des )
                print("*"*67)
                input("Presione una tecla para continuar")
    elif opcion=="2":
        opc1=""  
        while opc1!="3":    
            os.system("clear")
            print("*"*20,"Mantenimento De Departamento","*"*20)
            opc1 = helper.menu(["1) Ingreso","2) Consulta","3) Salir"],"")
            os.system("clear")  
            if opc1 == "1":
                print("*"*20,"Ingreso de Departamentos","*"*20)
                nombre=input("Departamento     :") 
                while ((len (nombre))<5 or (len (nombre))>20):
                    print("Ingrese de nuevo")
                    nombre=input("Departamento         :")
                    os.system("clear")
                    print("*"*20,"Ingreso de Empleados","*"*20)
                car=Departamento(nombre)
                car1=car.registro()
                Departamento.departamentos.append(car1)
                input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
            elif opc1 == "2":
                print("*"*20,"Consulta de Departamentos","*"*20)
                print("Codigo"," "*5,"Descripción")
                for car in Departamento.departamentos:
                    cod=car["codigo"]
                    dep=car["departamento"]
                    print(" "*2,cod," "*10,dep )
                print("*"*67)
                input("Presione una tecla para continuar")
                
            
    elif opcion == "3":
        opc1=" "
        while opc1 != "3":
            os.system("clear")
            print("*"*20,"Mantenimento De Empleados","*"*20)
            opc1 = helper.menu(["1) Ingreso","2) Consulta","3) Salir"],"")
            os.system("clear")
            if opc1 == "1":
                print ("*"*20,"Ingreso de Empleados","*"*20)
                nombre=input("Nombre       :")
                while ((len (nombre))<4 or len(nombre)>20):
                    print("Ingrese menos caracteres")
                    nombre=input("Nombre         :")
                    os.system("clear")
                    print("*"*20,"Ingreso de Empleados","*"*20)
                cedula=(input("Cedula       :"))
                while (cedula.isnumeric() == True) and (len(cedula)<10): #es una función da True o False
                    print("Solo enteros")
                    print("y Solo 10 digitos, te doy un ejemplo: 1206859819")
                    cedula = input("Cedula     :")
                cargo=input("Cargo          :")
                while (cargo.isnumeric() == False):
                    print("Solo enteros")
                    cargo=input("Cargo ")
                while True:
                    if buscacargo(cargo)==0:
                        print("error")
                        cargo=input("Cargo ")
                    else:
                        break
                        
                depa=input("Departamento :")
                while (depa.isnumeric() == False):
                    print("Solo enteros")
                    depa=input("Departamento :")
                while True:
                    if buscadepartamento(depa)==0:
                        print("error")
                        depa=input("Departamento :")
                    else:
                        break
                sueldo=(input("Sueldo         :"))
                while ("." in sueldo) or (sueldo.isnumeric()== True):
                    print("Dato guardado")
                    break
                art2=Empleado(nombre,cedula,cargo,depa,sueldo)
                articulo=art2.registro()
                Empleado.Empleados.append(articulo)
                input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
            elif opc1=="2":
                print("*"*27,"Consulta de Empleados","*"*27)
                print("Codigo"," "*5,"Nombre"," "*5,"Cedula"," "*5,"Cargo"," "*5,"Departamento"," "*5,"Sueldo")
                for art2 in Empleado.Empleados:
                    cod=art2["codigo"]
                    nom=art2["nombre"]
                    ced=art2["cedula"]
                    car1=art2["cargo"]
                    car=buscacargo(car1)
                    dep=art2["departamento"]
                    dep1=buscadepartamento(dep)
                    sue=art2["sueldo"]
                    print(" "*2,cod," "*8,nom," "*(10-len(nom)),ced," "*(9-len(ced)),car,
                          " "*(16-len(str(dep1))),sue)
                print("*"*77)
                input("Presione una tecla para continuar")
    elif opcion=="4":
        print("Saliendo...pero no contigo mi ciela XD")

print("Gracias por visistarnos")                
            
                
                    
                    
                
        
                        
                    
                    

