inicio = int(input("Introduce el número de inicio del rango: "))
final = int(input("Introduce el número final del rango: "))

if inicio > final:
    inicio, final = final, inicio

print(f"Números pares entre {inicio} y {final}:")

for numero in range(inicio, final + 1):
    if numero % 2 == 0: 
        print(numero)
