from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

#모델 가져오기
model_man = 'man.obj'
ground = 'ground.obj'
ceiling = 'ceiling.obj'
front_wall = 'front wall.obj'
door = 'door.obj'
left_wall = 'left wall.obj'
right_wall = 'right wall.obj'
central_wall = 'central wall.obj'
stairs = 'stairs.obj'
stair_wall1 = 'stair wall1.obj'
stair_wall2 = 'stair wall2.obj'
stair_wall3 = 'stair wall3.obj'
stair_wall4 = 'stair wall4.obj'
chair1 = 'chair1.obj'
chair2 = 'chair2.obj'
chair3 = 'chair3.obj'
chair4 = 'chair4.obj'
chair5 = 'chair5.obj'
chair6 = 'chair6.obj'
chair7 = 'chair7.obj'
chair8 = 'chair8.obj'

#왼쪽벽, 중앙벽 다시 만들기(빼먹은 블록이 있음)

#맵 생성
Model_ground = Entity(model = ground, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_ceiling = Entity(model = ceiling, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_front_wall = Entity(model = front_wall, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_door = Entity(model = door, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_left_wall = Entity(model = left_wall, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_right_wall = Entity(model = right_wall, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_central_wall = Entity(model = central_wall, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_stairs = Entity(model = stairs, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_stair_wall1 = Entity(model = stair_wall1, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_stair_wall2 = Entity(model = stair_wall2, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_stair_wall3 = Entity(model = stair_wall3, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_stair_wall4 = Entity(model = stair_wall4, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_chair1 = Entity(model = chair1, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_chair2 = Entity(model = chair2, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_chair3 = Entity(model = chair3, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_chair4 = Entity(model = chair4, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_chair5 = Entity(model = chair5, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_chair6 = Entity(model = chair6, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_chair7 = Entity(model = chair7, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')
Model_chair8 = Entity(model = chair8, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, -20), collider='box')

model_entity = Entity(model = model_man, scale = (0.4, 0.4, 0.4), color = color.orange, rotation = (-90, 0, 90), position = (0, 0, 0))#사람

#player settings
player = FirstPersonController()
crosshair = Entity(model = 'cube', color = color.red, scale = (0.003, 0.003), position = (10, 10, 10))
camera.fov = 100
player.jump_height = 1.5



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

    if key =='escape':
        quit_game()

def quit_game():
    application.quit()

app.run()
