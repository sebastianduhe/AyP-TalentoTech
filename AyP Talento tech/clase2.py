"""
print("HOLA MUNDO")
## Boraa con cls 

num1 = 60
num2=4

nombre = "Sebastian"
print("Hola "+nombre)

suma = num1+num2
multi = num1*num2
dif = abs(num1-num2)
print(suma)
print(multi)
print(dif)
##################################################
nombre = input("¿Cual es tu nombre? ")
print("Hola "+nombre )


num1 = int(input("Deme el numero 1: "))
num2 = int(input("Deme el numero 2: "))

suma = num1+num2
multi = num1*num2
dif = abs(num1-num2)
div = num1/num2

print("EL resultado de la suma es: ", suma)
print("EL resultado de la multiplicacion es ", multi)
print("EL resultado de diferencia es ", dif)
print("EL resultado de division  es ", div)

###########################################

nomb = str(input("Hola cual es tu nombre?:  "))
apell = str(input("Hola cual es tu apellido?:  "))
edad = int(input(" Digita tu edad: "))

print("Hola usuario, tu nombre es",nomb,"",apell, "Y tu edad es ",edad, "años")
print("Hola usuario, tu nombre es",nomb + " "+  apell, "Y tu edad es ",edad, "años")
print(f'Hola usuario {nomb} {apell} tu edad es {edad} años')


###############################

condi = int(input("Digite su edad: "))
if condi > 1 and condi <18 :
    print("niño o adolecente")
elif condi ==1 or 0:
    print("Recien nacido ")
elif condi >19 and condi< 90:
    print("Adulto o tercera edad")
else:
    print("que edad mas rara mi parcero ")


#################################################
prod1 = 8000
prod2 = 10000
prod3 = 2000


print("Bienvenido a la tienda, espero tenga una buena experiencia")
nombre = input("digite su nombre para comenzar la facturacion ")
total = int(prod1+prod2+prod3)
print(f'el valor a pagar es {total}')
billete = int(input(" con que valor desea pagar la cuenta "))
devuelta = int(billete-total)
if billete > total:
    print(f'su devuelta es {devuelta}')
    print(f'Gracias por elegirnos, el total de su compra es {total}, por lo que su devuelta es {devuelta}, esperamos que vuelva pronto señor/a {nombre}' )
else:
    print(f'no es posible realizar su compra, ESPERAMOS PODER RESOLVER EL PROBLEMA SEÑOR {nombre}')

"""
##############################################
prod1 = 8000
prod2 = 10000
prod3 = 2000
comp1 = int(input("cuantas unidades del producto 1 vas a llevar: "))
comp2 = int(input("cuantas unidades del producto 2 vas a llevar: "))
comp3 = int(input("cuantas unidades del producto 3 vas a llevar: "))

tot1 = prod1*comp1
tot2 = prod2*comp2
tot3 = prod3*comp3

total = tot1+tot2+tot3
print(f'el total de su compra es {total}')
pago = int(input("Con cuanto dinero vas a pagar: "))
devuelta = pago-total

if devuelta >=0 :
    print(f'el valor de su compra es {total}, como usted pago con {pago} su devuelta es {devuelta}')
else:
    print("el dinero ingresado es insuficiente por lo que no se puede procesar la compra")














