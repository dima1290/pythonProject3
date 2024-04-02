import pygame as pg
import sys
import random
import time as s
pg.init()
fon = pg.image.load("orig.jpeg")
clock = pg.time.Clock()
x = 1000
y = 800
rad = 50
back = (0, 0, 0)
dis_x = 500
dis_y = 500
en_rad = 50
sp_e_x, sp_e_y = 10, 10
display = pg.display.set_mode((dis_y, dis_x))
display.blit(fon, (0, 0))
en_x, en_y = 100, 100
FPS = 1000
while True:
    x, y = pg.mouse.get_pos()
    if x < en_x:
        en_x -= 0.5
    if x > en_x:
        en_x += 0.5
    if y < en_y:
        en_y -= 0.5
    if y > en_y:
        en_y += 0.5
    print(en_x,en_y)
    clock.tick(FPS)
    display.blit(fon, (0, 0))
    pg.draw.circle(display, (255, 0, 0), (en_x, en_y), en_rad, 10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()