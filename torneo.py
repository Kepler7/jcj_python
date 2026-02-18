jugadores = [
    "Ana", "Luis", "Carlos", "Marta", "Sofía", "Diego",
    "Elena", "Pablo", "Lucía", "Raúl", "Carmen", "Iván"
]

equipo_a = jugadores[:4]
equipo_b = jugadores[4:8]
reservas = jugadores[8:]

for jugador in jugadores:
    if jugador in equipo_a:
        print(f"{jugador} juega en el Equipo A")
    elif jugador in equipo_b:
        print(f"{jugador} juega en el Equipo B")
    else:
        print(f"{jugador} es reserva")