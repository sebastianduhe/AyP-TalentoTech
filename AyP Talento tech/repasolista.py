###EJERCICIO: almacenar nombres hasta que encuentre la x 
""""
usuarios = []


while True:
    nombre = input("Dijite el nombre: ")
    if (nombre =="X") or (nombre =="x"):
        break

    usuarios.append(nombre)
    
print(f'los usuarios registrados son:  {usuarios}')
"""
 #### TUPLA    
nombres1 = {"luis","carlos","diana"}
nombres2 = {"luis","sofia","diana"}

print(nombres1.intersection(nombres2))

print("una prueba para ver si se actualizo el hub")
