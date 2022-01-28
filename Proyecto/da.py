import os
os.system("clear")
# while True:
#     ncargo = input("Ingrese el cargo: ")
#     if len(ncargo) <= 20 and len(ncargo) >3:
#         print("Datos ingresados correctamente")
#         break
#     else:
#         print("Maximo de 4 - 20 caracteres, ingrese nuevamente")

# cedula=int(input("Cedula     :"))
# if cedula != int:
#     print("Ingrese sólo números")
# digit=len(str(cedula))
# print(digit)
# while len(str(cedula)) != 10:
#     print("Ingrese los 10 dígitos")
#     cedula=(input("Cedula     :"))


# cedula = input("Cedula     :")
# while (cedula.isnumeric() == False) and len(cedula)!=10:
#         print("Revisa")
#         cedula = input("Cedula     :")
        
# print("corect")
# dato=input("ingrsa")
# while True:
#     while ("." in dato) or dato.isnumeric()== True:
#         input("presione una tecla para continuar")
#     print("s")
        
    
# def es_flotante(variable):
#     	try:
#             float(variable)
#             return True
#         except:
# 	        return False

# datos = ["123", "asd", "eeee", "----", "-5", "1.60"]
# for dato in datos:
# 	print("¿'{}' es un flotante? {}".format(dato, es_flotante(dato)))
    
# a=input("j: ")
# while (isinstance(a,float)==True) or (isinstance(a,int)==True):
#     print("r") 
cedula = input("Cedula     :")
while (cedula.isnumeric() == False) and (len(cedula)!=10): #es una función da True o False
         print("Solo enteros")
         print("y Solo 10 digitos, te doy un ejemplo: 1206859819")
         cedula = input("Cedula     :")   
    
    

    
 
