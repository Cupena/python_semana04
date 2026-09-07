"""Desarrollen un programa para una ferretería que cumpla estos requerimientos:

Solicitar el nombre del producto, precio y cantidad.
Crear una función que calcule el subtotal.
Crear una función que aplique 8 % de descuento cuando el subtotal sea mayor o igual a C$ 3,000.
Crear una función que calcule el IVA del 15 % después del descuento.
Crear un procedimiento que muestre producto, subtotal, descuento, IVA y total.
Utilizar variables locales dentro de las funciones.
Probar el programa con una compra que reciba descuento y otra que no lo reciba.
Explicar qué parámetros presentan comportamiento similar al paso por valor."""

nombreProducto = input("Ingrese el nombre del producto: ")
precioProducto = int(input("Ingrese el precio del producto: "))
cantidadProducto = int(input("Ingrese cuanto llevara: "))
descuento = 0.08

def calcular_subtotal(precioProducto, cantidadProducto):
    subtotal = precioProducto * cantidadProducto
    return subtotal

def aplicar_descuento(subtotal, descuento):
    descuentado = subtotal * descuento
    return descuentado

def aplicar_impuesto(subtotal, descuentado):
    impuesto = (subtotal - descuentado) * 0.15
    return impuesto

def calcular_total(subtotal, descuentado, impuesto):
    total = (subtotal - descuentado) + impuesto
    return total

def mostrar_listado(subtotal, descuentado,  impuesto, total):
    print("Subtotal: C$", subtotal)
    

subtotal = calcular_subtotal(precioProducto, cantidadProducto)
descuentado = aplicar_descuento(subtotal, descuento)
impuesto = aplicar_impuesto(subtotal, descuentado)
total = calcular_total(subtotal, descuentado, impuesto)

mostrar_listado(subtotal, descuentado, impuesto, total)

