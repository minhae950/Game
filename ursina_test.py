from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

#model import
man = 'man.obj'

#class
class Human(Entity):
    def __init__(self, name, model, position=(0, 0, 0), scale=(0, 0, 0), rotation=(0, 0, 0), texture='', **kwargs):
        super().__init__(
            model=model,
            name=name,
            color=color.azure,
            collider='box',
            position=position,
            scale=scale,
            rotation=rotation,
            texture=texture,
            **kwargs
        )
        self.original_color = self.color
        
    #interact #define
    def interact(self):
        print(f"Interacted with {self.name}")
        self.color = color.red
    def on_hover(self):
        self.color = color.green
        show_text(self.name, 0.1, (0, -0.1))
    def on_unhover(self):
        self.color = self.original_color
        

#map
ground = Entity(model='plane', scale=(50, 1, 50), texture='white_cube', texture_scale=(20, 20), collider='box')


James = Human(name='James', model='man', position=(2, 0, 0), scale=(0.4, 0.4, 0.4), rotation=(-90, 0, 90))
Jhon = Human(name='Jhon', model='man', position=(2, 0, 2), scale=(0.4, 0.4, 0.4), rotation=(-90, 0, 90))
Robert = Human(name='Robert', model='man', position=(2, 0, 4), scale=(0.4, 0.4, 0.4), rotation=(-90, 0, 90))
David = Human(name='David', model='man', position=(2, 0, 6), scale=(0.4, 0.4, 0.4), rotation=(-90, 0, 90))

#dialog
"""
X-ray: James, Jessica, Dorothy
Stethoscope: Robert, Jhon, Elizabeth
Ringer: David, Margaret
"""
#Man
text_James = ["I feel like I have parasites in my body." "Please take out parasites."]
text_Robert = ["I've been running too much,", "my heart has gotten faster.", "Please help."]
text_Jhon = ["I broke up with my girlfriend. It's so sad.", "Please check what's wrong with my body."]
text_David = ["I lost too much blood in the accident.", "I need to get a blood transfusion pack, please help."]
#Woman
text_Jessica = ["My son swallowed the toy." "He can't breathe. Please help."]
text_Dorothy = ["My.. body.... wrong..", "ghost.... hel..p"]
text_Elizabeth = ["I am an office worker who usually drinks coffee and cigarettes.", "My heart is beating fast these days.", "Is there something wrong with me?"]
text_Margaret = ["I'm on an IV because I caught a cold. But I feel dizzy and weird.", "I heard you need to get an A-pack, is everything going well?"]

#Tab UI
card = Entity(model='quad', color=color.gray, scale=(1, 0.6), position=(0, 0), parent=camera.ui)
card.visible = False

#fucking player settings
player = FirstPersonController()
player.jump_height = 0.8
player.jump_up_duration = 0.2
camera.fov = 100

#UI
hand = Entity(parent=camera, model='cube', scale=(0.13, 0.15, 0.13))
hand.position = Vec3(0.5, -0.3, 0.5)
hand.rotation = Vec3(0, 90, 0)

#blogal variables
hand_visible = False
hand.visible = False
cursur_lock = False
card_visible = False
previous_hovered_entity = None

def input(key):
    global hand_visible
    global cursur_lock
    
    #run key
    if key == 'left shift':
        player.speed = 10
    if key == 'left shift up': 
        player.speed = 5
    
    #item uses
    if key == '1':
        hand.color = color.white
        if hand_visible == False:
            hand.visible = True
            hand_visible = True
        elif hand_visible == True:
            hand.visible = False
            hand_visible = not hand_visible      

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
    
    if hit_info.hit and isinstance(hit_info.entity, Human):
        hovered_entity = hit_info.entity
        
        hovered_entity.on_hover()
        
        if held_keys['e']:
            hovered_entity.interact()
            if hovered_entity == James:
                show_text_sequence(text_James, interval=2)
            if hovered_entity == Jhon:
                show_text_sequence(text_Jhon, interval=2)
            if hovered_entity == Robert:
                show_text_sequence(text_Robert, interval=2)
            if hovered_entity == David:
                show_text_sequence(text_David, interval=2)

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