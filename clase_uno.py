edad = int(input("Pon tu edad "))

mayoria_de_edad = 18
vip = True

if edad >= mayoria_de_edad:
    print("Eres mayor de edad y puedes ir a la fiesta")
    if vip == True:
        print("Tienes acceso VIP")
    else:
        print("No eres VIP")
elif edad < 8:
    print("tu ni preguntes peque")
else:
    print("Estas loco !! no tienes edad para ir a la fiesta")

