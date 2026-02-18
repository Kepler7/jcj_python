frutas = {
    "manzana": {
        "precio": 10,
        "stock": 5
    },
    "banana": {
        "precio": 8, 
        "stock": 0
    },
    "uva": {
        "precio": 12,
          "stock": 5
    }
}

buscar_fruta = input("Ingrese el nombre de la fruta que desea comprar: ")

if buscar_fruta in frutas:
    if frutas[buscar_fruta]["stock"] > 0:
        frutas[buscar_fruta]["stock"] -= 1
        print(f"Has comprado una {buscar_fruta}")
    else:
        print(f"Lo siento, no hay stock de {buscar_fruta}")
else:
    print(f"Lo siento, no tenemos {buscar_fruta} en nuestra tienda")

