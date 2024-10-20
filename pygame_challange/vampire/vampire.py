import pygame
from os.path import join
from random import randint, uniform


class Game():
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 1280
        self.WINDOW_HEIGHT = 720
        self.display_surface = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption('vampire')
        self.clock = pygame.time.Clock()
        self.running = True
        self.player_frames =[]

        self.all_sprites = pygame.sprite.Group()
        player = Player(self.player_frames, self.all_sprites)
        

        self.player_up = [pygame.image.load(join('images','player','up',str(i)+'.png')).convert_alpha() for i in range(4)]

        self.player_frames.append(self.player_up)

        self.player_down = [pygame.image.load(join('images','player','down',str(i)+'.png')).convert_alpha() for i in range(4)]

        self.player_frames.append(self.player_down)

        self.player_right = [pygame.image.load(join('images','player','right',str(i)+'.png')).convert_alpha() for i in range(4)]

        self.player_frames.append(self.player_right)

        self.player_left = [pygame.image.load(join('images','player','left',str(i)+'.png')).convert_alpha() for i in range(4)]

        self.player_frames.append(self.player_left)


    def run(self):

        while self.running:
            self.dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.all_sprites.update(self.dt)
            self.display_surface.fill('#3a2e3f')
            print(self.player_frames)

            pygame.display.update()


        pygame.quit()


class Player(pygame.sprite.Sprite):
    def __init__(self,frames,groups):
        super().__init__(groups)
        self.frames = frames
        self.image = frames[0][2]
        self.rect = self.image.get_frect(center = (self.WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.math.Vector2()
        self.speed = 300

    def update(self, dt):
        pass
        





#------------------------------------------------------------------
game = Game()
game.run()
