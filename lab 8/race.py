import random
import pygame

clock = pygame.time.Clock()
fps = 60  

RED = (255, 0, 0) 
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
SPEED = 6  
SCORE = 0  

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 393, 600  
pygame.init() 
screen = pygame.display.set_mode(WINDOW_SIZE)

font = pygame.font.SysFont('Verdana', 63)  
font_small = pygame.font.SysFont('Verdana', 18) 
game_over_text_label = font.render('Game Over!', True, WHITE)  

background = pygame.image.load(r"C:\Users\YOGA\Desktop\PP-2\lab 8\road.png")  
background = pygame.transform.scale(background, WINDOW_SIZE)  

pygame.display.set_caption('CARs')  

# Музыка
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\YOGA\Desktop\PP-2\lab 8\background.mp3")  # Фоновая музыка
pygame.mixer.music.play(-1)  # Бесконечный повтор

crash_sound = pygame.mixer.Sound(r"C:\Users\YOGA\Desktop\PP-2\lab 8\crash.wav")  # Звук аварии


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load(r"C:\Users\YOGA\Desktop\PP-2\lab 8\coin.png" )  
        self.image = pygame.transform.scale(original_image, (40, 40))  
        self.rect = self.image.get_rect()
        self.set_random_position()

    def move(self):
        self.rect.move_ip(0, 3)
        if self.rect.top > WINDOW_HEIGHT:
            self.set_random_position()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_random_position(self):
        self.rect.center = (random.randint(65, WINDOW_WIDTH - 65), 0)
        self.rect.bottom = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load(r"C:\Users\YOGA\Desktop\PP-2\lab 8\redcar.png")  
        self.image = pygame.transform.scale(original_image, (50, 100))  
        self.rect = self.image.get_rect()
        self.set_random_position()

    def move(self):
        global SPEED, SCORE
        self.rect.move_ip(0, SPEED)

        if self.rect.top > WINDOW_HEIGHT:
            SCORE += 1
            self.set_random_position()

    def set_random_position(self):
        self.rect.center = (random.randint(64, WINDOW_WIDTH - 64), 0)
        self.rect.bottom = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load(r"C:\Users\YOGA\Desktop\PP-2\lab 8\bluecar.png")  
        self.image = pygame.transform.scale(original_image, (50, 100))  
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 100)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 43:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WINDOW_WIDTH - 43:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group(player, enemy, coin)
enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group(coin)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 4000)

captured_coins = 0
running = True


def generate_new_coin():
    global coin
    coin = Coin()
    coins.add(coin)
    all_sprites.add(coin)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == INC_SPEED:
            SPEED += 0.5

    screen.blit(background, (0, 0))
    screen.blit(font_small.render(f'Score: {SCORE}', True, BLUE), (293, 10))
    screen.blit(font_small.render(f'Coins: {captured_coins}', True, BLUE), (293, 30))

    for sprite in all_sprites:
        sprite.move()
        sprite.draw(screen)

    if pygame.sprite.spritecollideany(player, coins):
        coin.kill()
        captured_coins += 1
        SCORE += 1
        generate_new_coin()

    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.music.stop()  # Останавливаем фоновую музыку
        crash_sound.play()  # Проигрываем звук аварии
        running = False  

    pygame.display.update()
    clock.tick(fps)


game_over_screen = True

while game_over_screen:
    screen.fill((69, 172, 116))
    screen.blit(game_over_text_label, (12, 190))
    screen.blit(font_small.render(f'Your score: {SCORE}', True, WHITE), (15, 270))
    screen.blit(font_small.render(f'Captured coins: {captured_coins}', True, WHITE), (15, 290))
    screen.blit(font_small.render('Press ESC or ENTER to exit', True, WHITE), (15, 350))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over_screen = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                game_over_screen = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()