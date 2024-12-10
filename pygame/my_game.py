
import pygame
import random
import os

# Инициализация основных параметров
screen_width = 1024  # Ширина игрового окна
screen_height = 768  # Высота игрового окна
FPS = 60           # Частота кадров в секунду
screen = pygame.display.set_mode((screen_width, screen_height))  # Размер окна
pygame.display.set_caption('First game by 1Prosha')              # Описание игры в поле caption
my_icon = pygame.image.load('i.webp')                            # Своя иконка
pygame.display.set_icon(my_icon)                                 # Свая иконка
pygame.init()                                                    # Основной инициализатор. Запускает pygame
pygame.mixer.init()                                              # Подрубаем звук
clock = pygame.time.Clock()                                      # Заданная частота кадров (проверка)

# Цвета
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((14, 30))  # Загрузка спрайта
        self.image.fill(BLUE)                  # Заполнение нашей фигуры цветом (blue)
        self.rect = self.image.get_rect()      # создание rectangle'a
        self.rect.x = 100                      # Позиция персонажа на экране
        self.rect.y = screen_height - 300      # т.к мы создаем куб это его высота
        self.velocity_y = 0
        self.on_ground = False                 # проверка позиции нашего персонажа
        self.speed = 5                         # Скорость игрока

    def update(self):
        self.rect.y += self.velocity_y
        # Передвижение персонажа
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:                   # Движение влево
            self.rect.x -= self.speed
        if keys[pygame.K_d]:                   # Движение вправо
            self.rect.x += self.speed
        # Проверка выхода за пределы экрана
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width

        if not self.on_ground:                  # Проверка персонаж на земле или нет
            self.velocity_y += 1            # Гравитация

    def jump(self):
        if self.on_ground:                      # Проверка если персонаж на земле (проверка)
            self.velocity_y = -15            # сила прыжка

    def reset(self):
        self.rect.x = 100
        self.rect.y = screen_height - 150       # Расстояние генерации платформ от персонажа

# Класс платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load('ground.webp').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()       # Создаем наш rectangle
        self.rect.x = x
        self.rect.y = y

# Загружаем фон
try:
    background = pygame.image.load('platform.png').convert()  # Загрузка текстуры фона
except pygame.error as e:
    print(f"Не удалось загрузить фон: {e}")
    pygame.quit()
    exit()
background = pygame.transform.scale(background, (screen_width, screen_height))

# Класс уровня
class Level:
    def __init__(self, level_data):
        self.level_data = level_data
        self.platforms = pygame.sprite.Group()
        self.create_platforms()
        
    def create_platforms(self):
        for platform in self.level_data:
            new_platform = Platform(*platform)
            self.platforms.add(new_platform)
            
    def draw(self, surface):
        self.platforms.draw(surface)

# Определение уровней
level_1 = [
    [0, screen_height - 50, screen_width, 50],  # Земля
    [200, screen_height - 150, 70, 20],
    [300, screen_height - 250, 70, 20],
    [400, screen_height - 350, 70, 20],
    [600, screen_height - 430, 70, 20],
    [800, screen_height - 350, 70, 20],
    [960, screen_height - 400, 70, 710]
]

level_2 = [
    [0, screen_height - 50, screen_width, 50],  # Земля
    [300, screen_height - 450, 70, 20],
    [500, screen_height - 550, 70, 20]
]

levels = [level_1, level_2]
current_level = 0

# Создание игрока
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Создание первого уровня
current_level_obj = Level(levels[current_level])
all_sprites.add(current_level_obj.platforms)

# Главный игровой цикл
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            jumnp = True
            player.jump()

    # Обновление объектов
    all_sprites.update()

    # Проверка на столкновение с платформами
    player.on_ground = False
    for platform in current_level_obj.platforms:
        if player.rect.colliderect(platform.rect) and player.velocity_y >= 0:
            player.rect.bottom = platform.rect.top
            player.velocity_y = 0
            player.on_ground = True

    # Проверка достижения конца уровня
    if player.rect.right >= screen_width:
        current_level += 1
        if current_level < len(levels):  # Если есть еще уровни
            current_level_obj = Level(levels[current_level])  # Переход на следующий уровень
            all_sprites.empty()
            all_sprites.add(player)
            all_sprites.add(current_level_obj.platforms)
            player.reset()
        else:
            print("Вы прошли все уровни!")  # Конец игры
            running = False

    # Отображение фона и спрайтов
    screen.blit(background, (0, 0))     # Отрисовка фона
    all_sprites.draw(screen)            # Отрисовка спрайтов

    # Обновление экрана
    pygame.display.flip()