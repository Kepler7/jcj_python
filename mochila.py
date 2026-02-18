mochila = {
    "libreta": 5,
    "lapiz": 3,
    "borrador": 0
}

objeto = input("Que objeto quieres usar? ").lower()

if objeto in mochila:
    if mochila[objeto] > 0:
        mochila[objeto] -= 1
        print(f"Has usado un {objeto}. Quedan {mochila[objeto]} en la mochila.")
    else:
        print(f"No quedan {objeto}es en la mochila.")
else:
    print(f"Objeto {objeto} no encontrado en la mochila.")