import readchar

nombre_jugador = input('Ingresa el nombre del Jugador: ')

print('Bienvenido al juego, {}'.format(nombre_jugador))

while True:
    keypress = readchar.readkey()
    if keypress == readchar.key.UP:
        break
    print(keypress)