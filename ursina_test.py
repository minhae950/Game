from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

#model import
man = 'man.obj'

#class
class InteractableCube(Entity):
    def __init__(self, name, model, position=(0, 0, 0), scale=(0, 0, 0), rotation=(0, 0, 0), **kwargs):
        super().__init__(
            model=model,
            name=name,
            color=color.azure,
            collider='box',
            position=position,
            scale=scale,
            rotation=rotation,
            **kwargs
        )
        self.original_color = self.color
        
    #interact #define
    def interact(self):
        print(f"Interacted with {self.name}")
        self.color = color.red
    def on_hover(self):
        self.color = color.green
        show_text(self.name, 0.01, (0, -0.1))
    def on_unhover(self):
        self.color = self.original_color
        

#map
ground = Entity(model='plane', scale=(50, 1, 50), texture='white_cube', texture_scale=(20, 20), collider='box')


Humman1 = InteractableCube(name='man1', model='man', position=(3, 0, 3), scale=(0.4, 0.4, 0.4), rotation=(-90, 0, 90))
Humman2 = InteractableCube(name='man2', model='man', position=(-3, 0, -3), scale=(0.4, 0.4, 0.4), rotation=(-90, 90, 90))

#Tab UI
card = Entity(model='quad', color=color.gray, scale=(1, 0.6), position=(0, 0), parent=camera.ui)
card.visible = False

#fucking player settings
player = FirstPersonController()
camera.fov = 100

#UI
hand = Entity(parent=camera, model='cube', scale=(0.13, 0.15, 0.13))
hand.position = Vec3(0.5, -0.3, 0.5)
hand.rotation = Vec3(0, 90, 0)

#blogal variables
hand_visable = False
hand.visible = False
cursur_lock = False
card_visible = False
previous_hovered_entity = None

#dialog
texts = ["Hello Doctor,", "Can you help me?"]

def input(key):
    global hand_visable
    global cursur_lock
    
    #run key
    if key == 'left shift':
        player.speed = 10
    if key == 'left shift up': 
        player.speed = 5
    
    #item uses
    if key == '1':
        hand.color = color.white
        if hand_visable == False:
            hand.visible = True
            hand_visable = True
        elif hand_visable == True:
            hand.visible = False
            hand_visable = not hand_visable
    if key == '2':
        hand.color = color.yellow
        if hand_visable == False:
            hand.visible = True
            hand_visable = True
        elif hand_visable == True:
            hand.visible = False
            hand_visable = not hand_visable
    if key == '3':
        hand.color = color.orange
        if hand_visable == False:
            hand.visible = True
            hand_visable = True
        elif hand_visable == True:
            hand.visible = False
            hand_visable = not hand_visable        

    #ID card check
    if key == 'tab':
        if cursur_lock == False:
            mouse.locked = False
            cursur_lock = True
            card.visible = True
            player.cursor.enabled = False
        elif cursur_lock == True:
            mouse.locked = True
            cursur_lock = False
            card.visible = False 
            player.cursor.enabled = True
            
    if key =='escape':
        quit_game()

def show_text(text, duration=2, position=(0, -0.2)):
    message = Text(text, position=position, origin=(0, 0), scale=2, color=color.black)
    invoke(message.disable, delay=duration)
    return duration

def show_text_sequence(texts, interval=2):
    total_time = 0
    for text in texts:
        invoke(show_text, text, interval, delay=total_time)
        total_time += interval

def update():
    global previous_hovered_entity
    hit_info = raycast(camera.world_position, camera.forward, distance=3)
    
    if hit_info.hit and isinstance(hit_info.entity, InteractableCube):
        hovered_entity = hit_info.entity
        
        hovered_entity.on_hover()
        
        if held_keys['e']:
            hovered_entity.interact()
            if hovered_entity.name == 'man1':
                show_text_sequence(texts, interval=2)
                
            if hovered_entity.name == 'man2':
                show_text_sequence(texts, interval=2)

        if previous_hovered_entity and previous_hovered_entity != hovered_entity:
            previous_hovered_entity.on_unhover()

        previous_hovered_entity = hovered_entity

    else:
        if previous_hovered_entity:
            previous_hovered_entity.on_unhover()
            previous_hovered_entity = None


def quit_game():
    application.quit()

app.run()