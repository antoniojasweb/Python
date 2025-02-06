valor=input("Dame un número: ")
if valor.isdigit():
    numero = int(valor)
    resultado = numero / 2
    print("El número divido entre 2 es:", resultado)
else:
    print("El valor introducido no es un número.")
