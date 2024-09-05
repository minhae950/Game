from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

#모델 가져오기
model_path = 'man.obj'
model_door = 'door.obj'
model_ground = 'ground.obj'
model_Front_Wall = 'Front_Wall.obj'
model_Left_Wall = 'Left_Wall.obj'
model_Right_Wall = 'Right_Wall.obj'
model_Central_Desk = 'Central_Desk.obj'
model_Inner_left_wall = 'Inner_left_wall.obj'
model_Inner_Right_Wall = 'Inner_Right_Wall.obj'
model_Inside_front_Wall = 'Inside_front_Wall.obj'
model_Interior_Facde_Wall_parts1 = 'Interior_Facde_Wall_parts1.obj'
model_Interior_Facde_Wall_parts2 = 'Interior_Facde_Wall_parts2.obj'
model_Diagonal_wall1= 'Diagonal_wall1.obj'
model_Diagonal_wall2 = 'Diagonal_wall2.obj'

#맵 생성
Model_door = Entity(model = model_door, scale = (0.37, 0.37, 0.37), position = (0, -0.8, 10), collider='box')#문
Model_ground = Entity(model = model_ground, scale = (0.37, 0.37, 0.37), position = (0, -0.8, 10), collider='box')#땅
Model_Left_Wall = Entity(model = model_Left_Wall, scale = (0.37, 0.37, 0.37), position = (0, -0.8, 10), collider='box')#왼쪽 벽
Model_Right_Wall = Entity(model = model_Right_Wall, scale = (0.37, 0.37, 0.37), position = (0, -0.8, 10), collider='box')#오른쪽 벽
Model_Front_Wall = Entity(model = model_Front_Wall, scale = (0.37, 0.37, 0.37), position = (0, -0.8, 10), collider='box')#정면 벽
Model_Central_Desk = Entity(model = model_Central_Desk, scale = (0.37, 0.37, 0.37), position = (0, -0.8, 10), collider='box')#중앙 테이블
Model_Diagonal_wall1 = Entity(model = model_Diagonal_wall1, scale = (0.37, 0.37, 0.37), position = (0, -0.8, 10), collider='box')#대각선 벽1
Model_Diagonal_wall2 = Entity(model = model_Diagonal_wall2, scale = (0.37, 0.37, 0.37), position = (0, -0.8, 10), collider='box')#대각선 벽2
Model_Inner_left_wall = Entity(model = model_Inner_left_wall, scale = (0.37, 0.37, 0.37), position = (0, -0.8, 10), collider='box')#안쪽 왼쪽 벽
Model_Inner_Right_Wall = Entity(model = model_Inner_Right_Wall, scale = (0.37, 0.37, 0.37), position = (0, -0.8, 10), collider='box')#안쪽 오른쪽 벽
Model_Inside_front_Wall = Entity(model = model_Inside_front_Wall, scale = (0.37, 0.37, 0.37), position = (0, -0.8, 10), collider='box')#안쪽 정면 벽
Model_Facde_Wall_parts1 = Entity(model = model_Interior_Facde_Wall_parts1, scale = (0.37, 0.37, 0.37), position = (0, -0.8, 10), collider='box')#안쪽 정멱 부품1안된;;;;
Model_Facde_Wall_parts2 = Entity(model = model_Interior_Facde_Wall_parts2, scale = (0.37, 0.37, 0.37), position = (0, -0.8, 10), collider='box')#안쪽 정멱 부품2안됨;;;;

model_entity = Entity(model = model_path, scale = (0.4, 0.4, 0.4), color = color.orange, rotation = (-90, 0, 90), position = (0, 0, 0))#사람

#player settings
player = FirstPersonController()
crosshair = Entity(model = 'cube', color = color.red, scale = (0.003, 0.003), position = (10, 10, 10))
camera.fov = 100

#cube = Entity(model='cube', color=color.white, scale=(2, 2, 2), position=(0, 1, 5), collider='box')

#UI손모양
hand = Entity(parent=camera, model='cube', scale=(0.13, 0.15, 0.13), color=color.rgb(150, 75, 0))
hand.position = Vec3(0.5, -0.3, 0.5)  # 화면 우측 하단에 위치시키기
hand.rotation = Vec3(0, 90, 0)  # 손 모양을 약간 회전

#blogal variables
hand_visable = False
hand.visible = False
cursor_visable = False


def input(key):
    global hand_visable
    global cursor_visable

    if key == 'left shift':
        player.speed = 10
    if key == 'left shift up': 
        player.speed = 5
    
    if key == '1':
        if hand_visable == False:
            hand.visible = True
            hand_visable = True
        elif hand_visable == True:
            hand.visible = False
            hand_visable = not hand_visable
            
    if key == 'tab':
        if cursor_visable == False:
            mouse.locked = False
            cursor_visable == True
        elif cursor_visable == True:
            mouse.locked = True
            cursor_visable = False


    if key =='escape':
        quit_game()

def quit_game():
    application.quit()


crosshair.parent = camera.ui

app.run()
