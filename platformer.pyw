import pygame as pg
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT,K_SPACE)
import sys


from sprites import Player, Platform

pg.init()


SKY = (135,206,250)

HEIGHT=560
WIDTH =1160

vec = pg.math.Vector2  # 2 for two dimensional
 
ACC = 0.5
FRIC = -0.12
FPS = 60

cr=[20,60,100,140,180,220,260,300,340,380,420,460,500,540,580,620,660,700,740,780,820,860,900,940,980,1020,1060,1100,1140]
 
G = 'assets/grass1.png'
D = 'assets/soil1.png'
P = 'assets/player1_01.png'
V = 'assets/lava_l131.png'
L = 'assets/lava_r161.png'
T = 'assets/t1.png'

size = (WIDTH,HEIGHT)

screen = pg.display.set_mode(size)
pg.display.set_caption("Platformer")



running = True



def read(file):
    with open(file,'r', encoding="utf-8") as f:
        r = f.read()
        s = r.splitlines()
        l = []
        for x in s:
            l.append(x.replace('  ',' ').split(' '))

        for y in range(14):
            for x in range(29):
                if l[y][x] == 'g':
                    h = Platform(G,(cr[x],cr[y]))
                    tiles.add(h)
                    asl.add(h)
                if l[y][x] == 'd':
                    h = Platform(D,(cr[x],cr[y]))
                    tiles.add(h)
                    asl.add(h)
                if l[y][x] == 'l':
                    h = Platform(L,(cr[x],cr[y]))
                    bads.add(h)
                    asl.add(h)
                if l[y][x] == 'v':
                    h = Platform(V,(cr[x],cr[y]))
                    bads.add(h)
                    asl.add(h)
                if l[y][x] == 't':
                    h = Platform(T,(cr[x],cr[y]))
                    tops.add(h)
                    asl.add(h)



#sprites

asl   = pg.sprite.Group()
bads  = pg.sprite.Group()
tiles = pg.sprite.Group()
tops = pg.sprite.Group()

player = Player((cr[0],cr[7]),3)
asl.add(player)

read('data/a.lvl')


clock = pg.time.Clock()

# Main loop
while running:
    # events
    for event in pg.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key?
            if event.key == K_ESCAPE:
                running = False    
            if event.key == K_SPACE:
                player.jump(tiles,tops)

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False


    pressed_keys = pg.key.get_pressed()


    # Update the player sprite based on user keypresses
    player.update(tiles,tops)



    #draw
    screen.fill(SKY)

    if player.move():
        l = player.lives -1
        if l == 0:
            running = False
        player.kill()
        player = Player((cr[0],cr[8]),l)
        asl.add(player)
        

    for entity in asl:
        screen.blit(entity.surf, entity.rect)


    #update
    pg.display.flip()
    clock.tick(FPS)

pg.quit()
