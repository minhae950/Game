from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import sys
import time

app = Ursina()

# if __name__ == "__main__":
#     print("Arguments Are: " + sys.argv[1] + " / " + sys.argv[2] + " / " + sys.argv[3])
#     time.sleep(3)

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

cube = Entity(model='cube', scale=(1, 1, 1), position=(0, 0.5, 5), color=color.red, collider='box')

James = Human(name='James', model='man', position=(2, 0, 0), scale=(0.4, 0.4, 0.4), rotation=(-90, 0, 90))
Doyun = Human(name='도윤', model='man', position=(2, 0, 2), scale=(0.4, 0.4, 0.4), rotation=(-90, 0, 90))
Jhon = Human(name='Jhon', model='man', position=(2, 0, 4), scale=(0.4, 0.4, 0.4), rotation=(-90, 0, 90))
David = Human(name='David', model='man', position=(2, 0, 6), scale=(0.4, 0.4, 0.4), rotation=(-90, 0, 90))

Jessica = Human(name='David', model='man', position=(2, 0, 6), scale=(0.4, 0.4, 0.4), rotation=(-90, 0, 90))
Dorothy = Human(name='David', model='man', position=(2, 0, 6), scale=(0.4, 0.4, 0.4), rotation=(-90, 0, 90))
Elizabeth = Human(name='David', model='man', position=(2, 0, 6), scale=(0.4, 0.4, 0.4), rotation=(-90, 0, 90))
Margaret = Human(name='David', model='man', position=(2, 0, 6), scale=(0.4, 0.4, 0.4), rotation=(-90, 0, 90))

#dialog
"""
X-ray: James, Jessica, Dorothy
Stethoscope: Robert, Jhon, Elizabeth
Ringer: David, Margaret
"""
#Man
text_James = ["제 몸에 기생충이 있는것 같아요.", "위를 갉아먹는 느낌이에요.", "기생충 좀 빼주세요."]
text_Doyun = ["너무 많이 뛰었더니,", "심장이 빨라져서 돌아오지 않아요.", "도와주세요."]
text_Jhon = ["제가 아끼는 여자친구와 헤어졌어요.", "너무 슬퍼서 힘들어요.", "몸에 무슨 문제가 있는지 확인해주세요."]
text_David = ["사고로 피를 너무 많이 흘렸어요.", "수혈팩을 맞아야하는데, 도와주세요."]
#Woman
text_Jessica = ["아들이 장난감을 삼켰어요.", "숨을 못쉬고 있어요.", "제발 도와주세요."]
text_Dorothy = ["저.. 몸.. 귀신..", "도와주세..요"]
text_Elizabeth = ["평소에 커피와 담배를 가까이 하는 직장인이에요.", "요즘들어 심장이 빨리뛰는 것 같아요.", "제게 문제가 있는걸까요?"]
text_Margaret = ["감기에 걸려서 링거를 맞고있어요.", "근데 어지럽고 이상한 느낌이 들어요.", "듣기로는 A팩을 받아야한다는데, 잘 진행되고 있는건가요?"]

#Sounds
main_theme = Audio(sound_file_name='assets/music/night-in-kyoto.mp3', volume=0.1, autoplay=False)

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
    message = Text(text, position=position, origin=(0, 0), scale=2, color=color.black, font='assets/fonts/neodgm.ttf')
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
                main_theme.play()
            if hovered_entity == Jhon:
                show_text_sequence(text_Jhon, interval=2)
            if hovered_entity == Doyun:
                show_text_sequence(text_Doyun, interval=2)
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