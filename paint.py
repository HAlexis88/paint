"Este modulo, es el principal aqui cada comando que entra es ejecutado"
#pylint: disable = C0103
#pylint: disable = E1101
import pygame
import colores
import lineas
import ayuda
# Inicializar Pygame
pygame.init()

# Crear una superficie de 800x600 píxeles
width = 800
height = 600
surface = pygame.display.set_mode((width, height))
color_fondo = (255, 0, 0)

color = (0, 0, 0)

def comando(instruccion):
    """Esta funcion nos ayuda para obtener el resultado de cada comando"""
    global color
    partes = instruccion.strip().split()
    if len(partes) > 0 and partes[0] == "ayuda":
        ayuda.ayuda()
    elif partes[0] == "grosor":
        nuevo_grosor = int(partes[1])
        lineas.grosor(nuevo_grosor)
    elif len(partes) > 0 and partes [0] == "color":
        if partes[1] == "list":
            colores.colores()
        elif partes[1] == "set":
            nuevo_color = partes[2]
            if colores.validacion(nuevo_color):
                color = colores.cambio(nuevo_color)
        else:
            print("Color inválido")
    elif len(partes) > 0 and partes[0] == "fondo":
        nuevo_color_fondo = partes[1]
        if colores.validacion(nuevo_color_fondo):
            color_fondo = colores.cambio(nuevo_color_fondo)
            surface.fill(color_fondo)
        else:
            print("Color inválido")
    elif len(partes) > 0 and partes[0] == "linea":
        if partes[1] == "=":
            x1, y1, x2, y2 = map(int, partes[2:])
            lineas.linea(surface, color, x1, y1, x2, y2)
    elif len(partes) > 0 and partes[0] == "triangulo":
        if len(partes) >= 8:
            x1, y1, x2, y2, x3, y3 = map(int, partes[2:8])
            lineas.triangulo(surface, color, x1, y1, x2, y2, x3, y3)
    elif partes[0] == "cuadrado":
        x, y, lado = map(int, partes[1:])
        lineas.cuadrado(surface, color, x, y, lado)
    elif partes[0] == "circulo":
        centro_x, centro_y, radio = map(int, partes[1:])
        lineas.circulo(surface, color, centro_x, centro_y, radio)
    elif partes[0] == "rectangulo":
        x,y,b,a = map(int, partes[1:])
        lineas.rectangulo(surface,color,x,y,b,a)
    elif partes[0] == "equilatero":
        if partes[1] == "=":
            centro_x, centro_y, lado = map(int, partes[2:6])
            lineas.equilatero(surface, color, centro_x, centro_y, lado)
    elif len(partes) > 0 and partes[0] == "isosceles":
        if partes[1] == "=":
            x1, y1, base, altura = map(int, partes[2:6])
            lineas.isoceles(surface, color, x1, y1, base, altura)
# Establecer el color de fondo inicial
surface.fill(color_fondo)
pygame.display.flip()

# Esperar a que el usuario cierre la ventana
myfile = open("comandos.cmd", "r", encoding="utf-8")
for cmd in myfile:
    cmd = cmd.strip()
    comando(cmd)
    print(f"-{cmd}-")
myfile.close()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
