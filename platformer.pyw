import pygame as pg
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT,)

pg.init()


SKY = (135,206,250)

HEIGHT=560
WIDTH =1160

vec = pg.math.Vector2  # 2 for two dimensional
 
ACC = 0.5
FRIC = -0.12
FPS = 60
 


size = (WIDTH,HEIGHT)

screen = pg.display.set_mode(size)
pg.display.set_caption("Platformer")



running = True


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.image.load('assets/player1_01.png').convert_alpha()
        self.rect = self.surf.get_rect(center = (10, 530))

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

class platform(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))


#sprites
player = Player()


clock = pg.time.Clock()

# Main loop
while running:
    # events
    for event in pg.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key?.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False


    pressed_keys = pg.key.get_pressed()


    # Update the player sprite based on user keypresses
    player.update(pressed_keys)



    #draw
    screen.fill(SKY)

    screen.blit(player.surf, player.rect)


    #update
    pg.display.flip()

pg.quit()
