import pygame
import sys

# 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rush Hour')

# 색상 설정
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# 차량 크기와 설정
GRID_SIZE = 100
CARS = [
    {"rect": pygame.Rect(300, 300, GRID_SIZE, GRID_SIZE * 2), "color": BLUE, "vertical": True},
    {"rect": pygame.Rect(100, 100, GRID_SIZE * 2, GRID_SIZE), "color": RED, "vertical": False},
    {"rect": pygame.Rect(300, 100, GRID_SIZE * 2, GRID_SIZE), "color": GREEN, "vertical": False},
    {"rect": pygame.Rect(500, 100, GRID_SIZE, GRID_SIZE * 2), "color": (255, 255, 0), "vertical": True},
]

# 게임 루프
running = True
selected_car_index = 0  # 키보드로 선택할 차량
MOVE_SPEED = GRID_SIZE  # 차량을 한 번에 이동시키는 단위

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        for y in range(0, HEIGHT, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

def check_collision(car, dx, dy):
    """차량이 다른 차량 또는 화면 경계와 충돌하는지 확인."""
    new_rect = car["rect"].move(dx, dy)

    # 화면 경계 충돌 확인
    if new_rect.left < 0 or new_rect.right > WIDTH or new_rect.top < 0 or new_rect.bottom > HEIGHT:
        return True

    # 다른 차량과 충돌 확인
    for other_car in CARS:
        if other_car != car and new_rect.colliderect(other_car["rect"]):
            return True

    return False

while running:
    screen.fill(WHITE)
    draw_grid()

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            car = CARS[selected_car_index]

            if event.key == pygame.K_TAB:  # Tab 키로 차량 전환
                selected_car_index = (selected_car_index + 1) % len(CARS)

            dx, dy = 0, 0
            if event.key == pygame.K_UP and car["vertical"]:
                dy = -MOVE_SPEED
            elif event.key == pygame.K_DOWN and car["vertical"]:
                dy = MOVE_SPEED
            elif event.key == pygame.K_LEFT and not car["vertical"]:
                dx = -MOVE_SPEED
            elif event.key == pygame.K_RIGHT and not car["vertical"]:
                dx = MOVE_SPEED

            # 충돌하지 않으면 이동
            if not check_collision(car, dx, dy):
                car["rect"].move_ip(dx, dy)

    # 차량 그리기
    for car in CARS:
        pygame.draw.rect(screen, car["color"], car["rect"])
    pygame.draw.rect(screen, "gray", (300, 0, 100, 100), width=0)


    pygame.display.flip()
