oportunidades = 1
is_ok_uno = False
is_ok_dos = False
is_ok_tres = False
is_complete = False
contador = 0
print("Bienvenido a tu Examen tienes 3 oportunidades, y si ganas te damos unos chilaquiles rojos")
for o in range(3):
    print(f"Esta es tu oportunidad {oportunidades}")
    if contador == 3:
        break
    if not is_ok_uno:
        respuesta_uno = input("Cual es la capital de Francia? ")
        if respuesta_uno.lower() == "paris":
            is_ok_uno = True
            contador += 1
            print("Respuesta Correcta")
        else:
            print("respuesta Incorrecta")
    if not is_ok_dos:
        respuesta_dos = input("Cual es la capital de Colima? ")
        if respuesta_dos.lower() == "colima":
            is_ok_dos = True
            contador += 1
            print("Respuesta Correcta")
        else:
            print("respuesta Incorrecta")
    if not is_ok_tres:
        respuesta_tres = input("Cual es la capital de Jalisco? ")
        if respuesta_tres.lower() == "guadalajara":
            is_ok_tres = True
            contador += 1
            print("Respuesta Correcta")
        else:
            print("respuesta Incorrecta")
    oportunidades += 1
    print(f"Numeros de aciertos: {contador}")