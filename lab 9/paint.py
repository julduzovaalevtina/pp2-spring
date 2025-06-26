import pygame  # Импортируем библиотеку pygame для работы с графикой
import math  # Импортируем библиотеку math для математических вычислений

# Инициализируем pygame
pygame.init()
running = True  # Переменная для управления циклом игры

# Определяем размеры окна
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT) = (1000, 600)

# Определяем цвета в формате (R, G, B)
RED = (255, 0, 0)  
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0)  
BLUE = (0, 0, 255)  
BLACK = (0, 0, 0) 
RANDOM = (234, 0, 0)

# Создаём окно размером 1000x600 пикселей
screen = pygame.display.set_mode(WINDOW_SIZE)

# Устанавливаем начальные параметры рисования
color = BLACK  # Цвет по умолчанию — чёрный
shape = 'line'  # По умолчанию рисуем линии
width = 1  # Толщина линии по умолчанию

# Создаём объект для управления временем
clock = pygame.time.Clock()
fps = 60  # Устанавливаем частоту кадров в секунду

# Устанавливаем заголовок окна
pygame.display.set_caption('Давайте рисовать!')

# Заполняем фон белым цветом
screen.fill(WHITE)

# Переменные для хранения предыдущей и текущей точки при рисовании
prev, cur = None, None

# Создаём шрифт для отображения текста на экране
font = pygame.font.SysFont('Verdana', 15)

# Основной игровой цикл
while running:
    # Создаём белый прямоугольник сверху экрана, чтобы обновлять текст
    pygame.draw.rect(screen, WHITE, (0, 0, WINDOW_WIDTH, 30))

    # Выводим текущие параметры рисования
    screen.blit(font.render(f'Mode: {shape}', True, BLACK), (10, 10))
    screen.blit(font.render(f'Width: {width}', True, BLACK), (310, 10))
    screen.blit(font.render(f'Color: {color}', True, BLACK), (610, 10))
    
    # Обрабатываем события
    for event in pygame.event.get():
        # Проверяем, нажаты ли клавиши
        pressed = pygame.key.get_pressed()
        ctrl_pressed = pressed[pygame.K_RCTRL] or pressed[pygame.K_LCTRL]  # Контрольные клавиши
        alt_pressed = pressed[pygame.K_RALT] or pressed[pygame.K_LALT]  # Альтернативные клавиши

        # Закрытие окна при нажатии кнопки "Закрыть"
        if event.type == pygame.QUIT:
            running = False

        # Обрабатываем нажатия клавиш
        if event.type == pygame.KEYDOWN:
            if pressed[pygame.K_DOWN] and width > 1:  # Уменьшение толщины линии
                width -= 1
            if pressed[pygame.K_UP]:  # Увеличение толщины линии
                width += 1
            if alt_pressed and pressed[pygame.K_b]:  # Смена цвета на синий
                color = BLUE
            if alt_pressed and pressed[pygame.K_r]:  # Смена цвета на красный
                color = RED
            if alt_pressed and pressed[pygame.K_g]:  # Смена цвета на зелёный
                color = GREEN
            if alt_pressed and pressed[pygame.K_q]:  # Смена цвета на чёрный
                color = BLACK
            if alt_pressed and pressed[pygame.K_o]:  # Смена цвета на чёрный
                color = RANDOM
        

            # Смена режима рисования по комбинации Ctrl + клавиша
            if ctrl_pressed and pressed[pygame.K_c]:  # Рисование круга
                shape = 'circle'
            if ctrl_pressed and pressed[pygame.K_r]:  # Рисование прямоугольника
                shape = 'rectangle'
            if ctrl_pressed and pressed[pygame.K_l]:  # Рисование линии
                shape = 'line'
            if ctrl_pressed and pressed[pygame.K_e]:  # Ластик
                shape = 'eraser'
            if ctrl_pressed and pressed[pygame.K_t]:  # Прямоугольный треугольник
                shape = 'right_triangle'
            if ctrl_pressed and pressed[pygame.K_q]:  # Равносторонний треугольник
                shape = 'equilateral_triangle'
            if ctrl_pressed and pressed[pygame.K_h]:  # Ромб
                shape = 'rhombus'

        # Рисование линий и ластика
        if shape == 'line' or shape == 'eraser':
            if event.type == pygame.MOUSEBUTTONDOWN:  # При нажатии мыши фиксируем начальную точку
                prev = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:  # При движении мыши рисуем линии
                cur = pygame.mouse.get_pos()
                if prev:
                    if shape == 'line':
                        pygame.draw.line(screen, color, prev, cur, width)
                    if shape == 'eraser':
                        pygame.draw.line(screen, WHITE, prev, cur, width)
                    prev = cur  # Обновляем предыдущую точку
            if event.type == pygame.MOUSEBUTTONUP:  # Отпускаем кнопку мыши — прекращаем рисовать
                prev = None
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:  # Фиксируем первую точку для фигур
                prev = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:  # Фиксируем вторую точку и рисуем фигуру
                cur = pygame.mouse.get_pos()
                if shape == 'circle':  # Рисуем окружность
                    x = (prev[0] + cur[0]) / 2
                    y = (prev[1] + cur[1]) / 2
                    r = math.sqrt((cur[0] - prev[0])**2 + (cur[1] - prev[1])**2) / 2
                    pygame.draw.circle(screen, color, (int(x), int(y)), int(r), width)
                elif shape == 'rectangle':  # Рисуем прямоугольник
                    x = min(prev[0], cur[0])
                    y = min(prev[1], cur[1])
                    w = abs(cur[0] - prev[0])
                    h = abs(cur[1] - prev[1])
                    pygame.draw.rect(screen, color, (x, y, w, h), width)
                elif shape == 'right_triangle':  # Рисуем прямоугольный треугольник
                    pygame.draw.polygon(screen, color, [prev, (prev[0], cur[1]), cur], width)
                elif shape == 'equilateral_triangle':  # Рисуем равносторонний треугольник
                    side_length = math.sqrt((cur[0] - prev[0])**2 + (cur[1] - prev[1])**2)
                    height = side_length * math.sqrt(3) / 2
                    pygame.draw.polygon(screen, color, [
                        prev,
                        (prev[0] + side_length, prev[1]),
                        (prev[0] + side_length / 2, prev[1] - height)
                    ], width)
                elif shape == 'rhombus':  # Рисуем ромб
                    pygame.draw.polygon(screen, color, [
                        prev,
                        (2 * cur[0] - prev[0], cur[1]),
                        cur,
                        (2 * prev[0] - cur[0], prev[1])
                    ], width)

    # Обновляем экран
    pygame.display.flip()
    # Ограничиваем частоту кадров
    clock.tick(fps)

# Завершаем работу pygame
pygame.quit()