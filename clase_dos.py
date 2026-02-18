edad = int(input("Introduce tu edad: "))
mayoria_de_edad = 18
eres_vip = input("es vip ?")

if edad >= mayoria_de_edad:
    print("eres mayor de edad")
    if eres_vip == "si":
        print("Tienes acceso libre a la barra de alcohol")
    else:
        print("Puedes beber pero tienes que pagar")
elif edad <= mayoria_de_edad and edad > 8:
    print("si puedes ir a la fiesta pero no tomar alcohol")
    if eres_vip == "si":
        print("tienes acceso libre a gansitos")
    else:
        print("tienes que pagar por los gansitos")
else:
    print("ERES un bebito")

    
