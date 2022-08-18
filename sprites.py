import pygame as pg
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT,)


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
P = 'assets/player1_011.png'
L2 = 'assets/lava_l131.png'
L1 = 'assets/lava_r161.png'



class Player(pg.sprite.Sprite):
    def __init__(self,coords):
        super().__init__()
        self.surf = pg.image.load(P).convert_alpha()
        self.rect = self.surf.get_rect(bottomleft = (coords[0]-20,coords[1]-20))

        self.pos = vec((coords[0],coords[1]-20))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def move(self):
        self.acc = vec(0,0.5)
    
        pressed_keys = pg.key.get_pressed()            
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
             
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x > WIDTH-8:
            self.pos.x = WIDTH-8
        if self.pos.x < 18:
            self.pos.x = 18
        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT
        if self.pos.y < 18:
            self.pos.y = 18
            
        self.rect.midbottom = self.pos
    def update(self,tiles):
        hits = pg.sprite.spritecollide(self ,tiles, False)
        if self.vel.y > 0:
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0 
    def jump(self,tiles):
        hits = pg.sprite.spritecollide(self, tiles, False)
        if hits:
            self.vel.y = -10






class Platform(pg.sprite.Sprite):
    def __init__(self,image,coords):
        super().__init__()
        self.surf = pg.image.load(image).convert_alpha()
        self.rect = self.surf.get_rect(center = coords)














        
