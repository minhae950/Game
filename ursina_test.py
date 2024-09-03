from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

#모델 가져오기
model_path = 'man.obj'
model_m = 'model.obj'
#Grid_texture = load_texture('Texture.jpg')

#맵 생성
#ground = Entity(model = 'plane', scale = (50, 1, 50), texture = Grid_texture, collider = 'box')
Hospital_Models = Entity(model = model_m, scale = (0.37, 0.37, 0.37), position = (0, -0.8, 10), collider='box')
model_entity = Entity(model = model_path, scale = (0.4, 0.4, 0.4), color = color.orange, rotation = (-90, 0, 90), position = (0, 0, 0))

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
weapon_state = 'none'

def input(key):
    global hand_visable
    
    if key == 'left shift':
        player.speed = 10
    if key == 'left shift up': 
        player.speed = 5
    
    if key == '1':
        if hand_visable == False:
            hand.visible = True
            hand_visable = True
            weapon_state = 'hand'
        elif hand_visable == True:
            hand.visible = False
            hand_visable = not hand_visable
            
    if key =='escape':
        quit_game()

def quit_game():
    application.quit()


crosshair.parent = camera.ui

app.run()
