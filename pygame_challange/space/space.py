import pygame
from os.path import join
from random import randint, uniform


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2,WINDOW_HEIGHT / 1.25 ))
        self.direction = pygame.math.Vector2()
        self.speed = 300


        #cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 40


    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, *args):
    #Keyboard Input
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        fire = pygame.key.get_just_pressed()
        if fire[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surf,self.rect.midtop,(all_sprites, laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
            laser_sound.play()

        self.laser_timer()


class Star(pygame.sprite.Sprite):
    def __init__(self, groups, star_surf):
        super().__init__(groups)
        self.image = star_surf
        self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)

    def update(self, dt):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0:
            self.kill()

class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.origin_image = surf
        self.image = self.origin_image
        self.rect = self.image.get_frect(center = pos)
        self.start_time = pygame.time.get_ticks()
        self.life_time = 3000
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 500)
        self.rotation_speed = randint(50,80)
        self.rotation = 0
        
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >=self.life_time:
            self.kill()

        self.rotation += self.rotation_speed * dt
        self.image =pygame.transform.rotozoom(self.origin_image, self.rotation, 1)
        self.rect = self.image.get_frect(center = self.rect.center)



class AnimatedExplosion(pygame.sprite.Sprite):
    def __init__(self, frames, pos, groups):
        super().__init__(groups)
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center=pos)

# mechanizm ciułania klatek ***********ANIMACJA***************
    def update(self, dt):
        self.frame_index += 50 * dt
        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
        else:
            self.kill()





def collisions():
    global running
    global killem
    collision_sprites = pygame.sprite.spritecollide(player, meteor_sprites, True, pygame.sprite.collide_mask)
#    if collision_sprites:
#        running = False
    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()
            killem += 1
            AnimatedExplosion(explosion_frames, laser.rect.midtop, all_sprites)
            explosion_sound.play()





def display_score(killem):
    current_time = pygame.time.get_ticks() // 1000
    text_surf = font.render('Time: '+str(current_time) , True, '#a3a5a9')
    text_rect = text_surf.get_frect(topleft = (30, 20))
    display_surface.blit(text_surf, text_rect)

    text_surf2 = font.render('Killem: '+str(killem) , True, '#a3a5a9')
    text_rect2 = text_surf2.get_frect(topleft = (150, 20))
    display_surface.blit(text_surf2, text_rect2)

    pygame.draw.rect(display_surface, 'darkgoldenrod', text_rect.inflate(20,20).move(0,-3), 2, 5)
    pygame.draw.rect(display_surface, 'darkgoldenrod', text_rect2.inflate(20,20).move(0,-3), 2, 5)



#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('gray')
clock = pygame.time.Clock() 


all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
for x in range(20):
    Star(all_sprites, star_surf)

player = Player(all_sprites)


meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()

font = pygame.font.Font(join('images', 'Oxanium-Bold.ttf'), 20)

explosion_frames = [pygame.image.load(join('images', 'explosion', str(i)+'.png')).convert_alpha()  for i in range(21)]

laser_sound = pygame.mixer.Sound(join('audio', 'laser.wav'))
laser_sound.set_volume(0.1)
explosion_sound = pygame.mixer.Sound(join('audio', 'explosion.wav'))
explosion_sound.set_volume(0.1)

game_music = pygame.mixer.Sound(join('audio', 'music.wav'))
game_music.set_volume(0.1)
game_music.play(loops = -1)



#custom event -> metor event
meteor_event=pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)


running = True
killem = 0

while running:
    dt = clock.tick() / 1000
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print('You closed it bro!!!')

        if event.type == meteor_event:
            x, y = randint(0, WINDOW_WIDTH), randint(-200, -100)
            Meteor(meteor_surf, (x, y), (all_sprites, meteor_sprites))  


    # all sprite's update
    all_sprites.update(dt)
    collisions()
    #draw the game
    display_surface.fill('#3a2e3f')
    display_score(killem) 
    all_sprites.draw(display_surface)

    # frame update?
    pygame.display.update()


pygame.quit()
