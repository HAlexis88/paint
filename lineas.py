#pylint: disable = C0103
#pylint: disable = E1101
import pygame
def linea(surface, color, x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    error = dx - dy

    while x1 != x2 or y1 != y2:
        surface.set_at((x1, y1), color)
        e2 = 2 * error
        if e2 > -dy:
            error -= dy
            x1 += sx
        if e2 < dx:
            error += dx
            y1 += sy
    pygame.display.flip()

def triangulo(surface, color, x1, y1, x2, y2, x3, y3):
    linea(surface, color, x1, y1, x2, y2)
    linea(surface, color, x2, y2, x3, y3)
    linea(surface, color, x3, y3, x1, y1)
    pygame.display.flip()

def equilatero(surface, color, center_x, center_y, lado):
    """Dibuja un triángulo equilátero"""
    altura = int((3**0.5) / 2 * lado)

    x1 = center_x - lado // 2
    y1 = center_y + altura // 3

    x2 = center_x
    y2 = center_y - (2 * altura) // 3

    x3 = center_x + lado // 2
    y3 = center_y + altura // 3

    linea(surface, color, x1, y1, x2, y2)
    linea(surface, color, x2, y2, x3, y3)
    linea(surface, color, x3, y3, x1, y1)

    pygame.display.flip()

def isoceles(surface, color, x1, y1, base, altura):
    x2 = x1 + base // 2
    x3 = x1 + base
    y2 = y1 + altura
    y3 = y1

    linea(surface, color, x1, y1, x2, y2)
    linea(surface, color, x2, y2, x3, y3)
    linea(surface, color, x3, y3, x1, y1)

    pygame.display.flip()

def cuadrado(surface, color,lado, x, y):
    x2 = x + lado
    y2 = y + lado
    linea(surface, color, x, y, x2, y)
    linea(surface, color, x2, y, x2, y2)
    linea(surface, color, x2, y2, x, y2)
    linea(surface, color, x, y2, x, y)

def circulo(surface, color, centro_x, centro_y, radio):
    x = radio
    y = 0
    error = 1 - radio

    while x >= y:
        surface.set_at((centro_x + x, centro_y + y), color)
        surface.set_at((centro_x - x, centro_y + y), color)
        surface.set_at((centro_x + x, centro_y - y), color)
        surface.set_at((centro_x - x, centro_y - y), color)
        surface.set_at((centro_x + y, centro_y + x), color)
        surface.set_at((centro_x - y, centro_y + x), color)
        surface.set_at((centro_x + y, centro_y - x), color)
        surface.set_at((centro_x - y, centro_y - x), color)

        y += 1

        if error < 0:
            error += 2 * y + 1
        else:
            x -= 1
            error += 2 * (y - x) + 1

    pygame.display.flip()

def rectangulo(surface, color, x, y, ancho, alto):

    x2 = x + ancho
    y2 = y + alto


    for i in range(x, x2 + 1):
        surface.set_at((i, y), color)
        surface.set_at((i, y2), color)


    for i in range(y, y2 + 1):
        surface.set_at((x, i), color)
        surface.set_at((x2, i), color)

    pygame.display.flip()

def grosor(nuevo_grosor):
    global grosor
    grosor = max(1, nuevo_grosor)
