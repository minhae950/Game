from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

#model import
model_path = 'man.obj'
Grid_texture = load_texture('Texture.jpg')

#map
ground = Entity(model='plane', scale=(50, 1, 50), texture='white_cube', texture_scale=(20, 20), collider='box')

model_entity = Entity(model=model_path, scale=(0.4, 0.4, 0.4), color=color.orange, rotation=(-90, 0, 90), position=(0, 0, 0))



card = Entity(model='quad', color=color.gray, scale=(1, 0.6), position=(0, 0, -0), parent=camera.ui)
card.visible = False

#fucking player settings
player = FirstPersonController()
crosshair = Entity(model='circle', color=color.red, scale=(0.003, 0.003), position=(0, 0, 0))
camera.fov = 100

# cube = Entity(model='cube', color=color.white, scale=(2, 2, 2), position=(0, 1, 5), collider='box')

#UI
hand = Entity(parent=camera, model='cube', scale=(0.13, 0.15, 0.13), color=color.rgb(150, 75, 0))
hand.position = Vec3(0.5, -0.3, 0.5)
hand.rotation = Vec3(0, 90, 0)

#blogal variables
hand_visable = False
hand.visible = False
cursur_lock = False
card_visible = False


def input(key):
    global hand_visable
    global cursur_lock
    #print(key) #for check
    
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
        if cursur_lock == False:
            mouse.locked = True
            cursur_lock = True
            card.visible = False
        elif cursur_lock == True:
            mouse.locked = False
            cursur_lock = not cursur_lock
            card.visible = True
            
    if key =='escape':
        quit_game()

def quit_game():
    application.quit()


crosshair.parent = camera.ui

app.run()