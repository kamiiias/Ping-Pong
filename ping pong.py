import pygame
w = 750
h = 550
pygame.mixer.init()
sound = pygame.mixer.Sound("feels.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
window = pygame.display.set_mode((w,h))
pygame.display.set_caption("Pin-Pong")
background = pygame.transform.scale(pygame.image.load("ng.jpg"),(w,h))
class GameSprite(sprite.Sprite):
    def __init__ (self, width, height, player_image,player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect() # Створити рамку навколо картинки спрайта
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self): # Функція для того щоб намалювати спрайт на екрані
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y <= 600:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.x >= 5:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x <= 600:
            self.rect.x += self.speed
game = True
finish = False
clock = time.Clock()
FPS = 80

racket1 = Player('mishka', 5, 50, 10)
racket2 = Player('mishka2', 5, 50, 10)
ball = ('', 5, 50, 10)


