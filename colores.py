def colores():
    listado = {'negro' : (0, 0, 0), 'blanco' : (255, 255, 255), 'rojo' : (255, 0, 0),
            'verde' : (0, 255, 0), 'azul' : (0, 0, 255), 'amarillo' : (255, 255, 0),
            'naranja' : (255, 165, 0), 'rosa' : (255, 192, 203), "marron" : (165, 42, 42)}
    print("Aqui se muestran tus colores: ")
    for colores in listado:
        print(colores)

def validacion(color):
    lista = {'negro' : (0, 0, 0), 'blanco' : (255, 255, 255), 'rojo' : (255, 0, 0),
            'verde' : (0, 255, 0), 'azul' : (0, 0, 255), 'amarillo' : (255, 255, 0),
            'naranja' : (255, 165, 0), 'rosa' : (255, 192, 203), "marron" : (165, 42, 42)}
    return color in lista

def cambio(color_cambio):
    lista = {'negro' : (0, 0, 0), 'blanco' : (255, 255, 255), 'rojo' : (255, 0, 0),
            'verde' : (0, 255, 0), 'azul' : (0, 0, 255), 'amarillo' : (255, 255, 0),
            'naranja' : (255, 165, 0), 'rosa' : (255, 192, 203), "marron" : (165, 42, 42)}
    return lista[color_cambio]
