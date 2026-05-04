from multiplicacion import multiplicacion
from resta import resta
from suma import suma

print("Menu de Operaciones")
print("Seleccione una Opcion")
opcion = int(input("Ingrese su opcion: "))
print("Opcion 1: Suma")
print("Opcion 2: Resta")
print("Opcion 3: Multiplicacion")

if opcion == 1 :
  print(suma(5,2))
elif opcion == 2:
  print(resta(5,2))
else:
  print(multiplicacion(5,2))
