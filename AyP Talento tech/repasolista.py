###EJERCICIO: almacenar nombres hasta que encuentre la x 
""""
usuarios = []


while True:
    nombre = input("Dijite el nombre: ")
    if (nombre =="X") or (nombre =="x"):
        break

    usuarios.append(nombre)
    
print(f'los usuarios registrados son:  {usuarios}')

 #### TUPLA    
nombres1 = {"luis","carlos","diana"}
nombres2 = {"luis","sofia","diana"}

print(nombres1.intersection(nombres2))

print("una prueba para ver si se actualizo el hub")
"""

### TUPLAS

frutas = ("fresa","manzana","papaya","manzana")

#contar
print(frutas.count("manzana"))
print(frutas.index("manzana"))

#modificar una tupla
temporal = list(frutas)  #esto se llama castear 
print(temporal)
temporal.append("mango") #adicionamos 
print(temporal)

frutas = tuple(temporal) #casteando la volvemos tupla 
print(frutas)



########### CONJUNTOS
# los componentes no tienen un orden o una posicion, sirve para ver que compene la lista pq cuando se imprime no repite 
conjunto = {"casa", "carro","beca","empresa"}

frutas2 = {"fresa","manzana","papaya","manzana"}
print(frutas2)
frutas2.add("guanabana")
print(frutas2)
numero = {1,2,3,4}


