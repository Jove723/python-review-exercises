ventas = [150, 75, 200, 300, 50, 120, 80]

def contar_total(i):
    print(f"El total de ventas fueron ${sum(i)}")

def precios(i):
    print(f"La venta mas baja fue de {min(i)}")
    print(f"La venta mas alta fue de {max(i)}")

def contar_100(i):
    contar_num = 0
    for num in i:
        if num >= 100:
            contar_num += 1
    
    print(f"La cantidad de ventas mayores a $100 son: {contar_num}")


contar_100(ventas)