lista1 = ["hola",58,True,3.1416]
print(len(lista1))

frutas = ["papaya","fresa","mango"]
print(frutas)
print(frutas[1])

##### Para agregar al final append
frutas.append("naranja")
print(frutas)

#para escoger donde insertarlo insert
frutas.insert(2,"uva")   #queda de tercero
print(frutas)

#reemplazar
frutas[2]="mandarina"
print(frutas)

verduras = ["espinaca","tomate","lechuga"]
fusion =frutas + verduras
print(fusion)

#frutas.extend(verduras)
print(fusion)

#copy
copia = frutas.copy()
print(copia)

copia.append("banano")
print(copia)

#contar
print(verduras)
print(verduras.count("tomate"))

#ver donde esta 
print(verduras.index("tomate"))

#eliminar el ultimo o el que uno le diga
verduras.pop(0)
print(verduras)

#remove me quita la primera que encuentra de lo que le digo
verduras.remove("lechuga")
print(verduras)

#reverse cambia el orden

print(frutas)
frutas.reverse()
print(frutas)

#orden alfabetico
frutas.sort()
print(frutas)