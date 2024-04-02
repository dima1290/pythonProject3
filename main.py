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
dis_x = 1000
dis_y = 800
en_rad = 50
sp_e_x, sp_e_y = 10, 10
display = pg.display.set_mode((dis_y, dis_x))
display.blit(fon, (0, 0))
en_x, en_y = en_rad, en_rad
FPS = 1000
while True:
    clock.tick(FPS)
    display.blit(fon, (0, 0))
    pg.draw.circle(display, (255, 0, 0), (en_x, en_y), en_rad, 10)
    en_y = en_y + sp_e_y
    en_x = en_x + sp_e_x
    if en_x - en_rad <= 0:
        sp_e_x = sp_e_x * -1
    elif en_x + en_rad >= dis_y:
        sp_e_x = sp_e_x * -1
    elif en_y - en_rad <= 0:
        sp_e_y = sp_e_y * -1
    elif en_y + en_rad >= dis_x:
        sp_e_y = sp_e_y * -1
    x, y = pg.mouse.get_pos()
    pg.draw.circle(display, (0, 0, 0), (x, y), rad)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()
# elif event.type == pg.KEYDOWN:
        #     if event.key == pg.K_a:
        #         if x - rad != 0:
        #             display.blit(fon, (0, 0))
        #             x = x - 10
        #     elif event.key == pg.K_d:
        #         if x + rad != dis_x:
        #             display.blit(fon, (0, 0))
        #             x = x + 10
        #     elif event.key == pg.K_w:
        #         if y - rad != 0:
        #             display.blit(fon, (0, 0))
        #             y = y - 10
        #     elif event.key == pg.K_s:
        #         if y + rad != dis_y:
        #             display.blit(fon, (0, 0))
        #             y = y + 10
        #     print(x)
        #     print(y)
        # print("Mouse position: ( {}, {})".format(x, y))


