tope = 10
contador = 0
while contador < tope:
    print("El contador es:", contador)
    contador += 1

print("El bucle ha terminado.")

contador = 0
while contador < tope:
    if contador == 5:
        break
    else:
        continue
    
    print("El bucle ha terminado.")
