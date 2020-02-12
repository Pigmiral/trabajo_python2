ina = {}
collec = 0
re = 0
mo = ''
while mo != 'T':
    if mo == 'A':
        llave = input('Introduce el número de la factura: ')
        costo = float(input('Introduce el coste de la factura: '))
        ina[llave] = costo
        re += costo
    if mo == 'P':
        llave = input('Introduce el número de la factura a pagar: ')
        costo = ina.pop(llave, 0)
        collec += costo
        re -= costo
    print('Recaudado:', collec)
    print('Pendiente de cobro: ', re)
    mo = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')
