from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

#모델 가져오기
model_man = 'man.obj'
model_door = 'door.obj'
model_ground = 'ground.obj'
model_stairs = 'stairs.obj'
model_chair0 = 'chair0.obj'
model_chair1 = 'chair1.obj'
model_chair2 = 'chair2.obj'
model_chair3 = 'chair3.obj'
model_chair4 = 'chair4.obj'
model_chair5 = 'chair5.obj'
model_chair6 = 'chair6.obj'
model_chair7 = 'chair7.obj'
model_ceiling = 'ceiling.obj'
model_Left_Wall = 'Left Wall.obj'
model_Right_Wall = 'Right Wall.obj'
model_Front_Wall = 'Front Wall.obj'
model_Central_Wall = 'Central Wall.obj'
model_Dressing_room_door = 'Dressing room door.obj'


#맵 생성
Model_door = Entity(model = model_door, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#문
Model_ground = Entity(model = model_ground, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#땅
Model_stairs = Entity(model = model_stairs, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#의자
Model_chair0 = Entity(model = model_chair0, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#의자
Model_chair1 = Entity(model = model_chair1, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#의자
Model_chair2 = Entity(model = model_chair2, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#의자
Model_chair3 = Entity(model = model_chair3, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#의자
Model_chair4 = Entity(model = model_chair4, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#의자
Model_chair5 = Entity(model = model_chair5, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#의자
Model_chair6 = Entity(model = model_chair6, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#의자
Model_chair7 = Entity(model = model_chair7, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#의자
#천장을 쓰면 어두워짐#Model_ceiling = Entity(model = model_ceiling, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#천장
Model_Left_Wall = Entity(model = model_Left_Wall, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#왼쪽벽
Model_Front_Wall = Entity(model = model_Front_Wall, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#정멱벽
Model_Right_Wall = Entity(model = model_Right_Wall, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#오른쪽벽
Model_Central_Wall = Entity(model = model_Central_Wall, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#중앙벽
Model_Dressing_room_door = Entity(model = model_Dressing_room_door, scale = (0.37, 0.37, 0.37), position = (-10, -0.8, 10), collider='box')#탈의실 문

model_entity = Entity(model = model_man, scale = (0.4, 0.4, 0.4), color = color.orange, rotation = (-90, 0, 90), position = (0, 0, 0))#사람

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
