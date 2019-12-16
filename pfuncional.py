clientes = [
    {'Nombre':'hector','apellidos':'costa','DNI':'136627283'},
    {'Nombre':'maria','apellidos':'ramirez','DNI':'883883883'}
]

def mostrar_cliente(clie, dni):
    for c in clie:
        if (dni == c['DNI']):
            print('{} {}'.format(c['Nombre'], c['apellidos']))
            #return
            break
        print("cliente no existe")

mostrar_cliente(clientes,'883883883')