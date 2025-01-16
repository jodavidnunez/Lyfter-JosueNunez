"""1. Cree un diagrama que le pida un `precio de producto` al usuario, calcule su
 descuento y muestre el precio final tomando en cuenta que:
 1. Si el precio es menor a 100, el descuento es del 2%.
 2. Si el precio es mayor o igual a 100, el descuento es del 10%.
 3. *Ejemplos*:
 1. 120 -> 108
 2. 40 -> 39.2"""


precio_usuario = int(input("Cual es el precio a consultar?: "))
if (precio_usuario < 100):
    descuento = round((precio_usuario * 0.02), 2)
else:
    descuento = round((precio_usuario * 0.1), 2)
precio_final = precio_usuario - descuento
print(f'El precio final es : {precio_final}')