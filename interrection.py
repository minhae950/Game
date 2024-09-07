from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

ground = Entity(model='plane', scale=(50, 1, 50), texture='white_cube', texture_scale=(20, 20), collider='box')

player = FirstPersonController()

texts = ["Hello, Doctor!", "Can you help me?"]

class InteractableCube(Entity):
    def __init__(self, name, position=(0, 0, 0), scale=(0, 0, 0), rotation=(0, 0, 0), **kwargs):
        super().__init__(
            model='man.obj',
            name=name,
            color=color.azure,
            collider='box',
            position=position,
            scale=scale,
            rotation=rotation,
            **kwargs
        )
        self.original_color = self.color
        
    def interact(self):
        print(f"Interacted with {self.name}")
        self.color = color.red

    def on_hover(self):
        self.color = color.green

    def on_unhover(self):
        self.color = self.original_color
        

def show_text(text, duration=2):
    message = Text(text, position=(0, -0.2), origin=(0, 0), scale=2)
    invoke(message.disable, delay=duration)
    return duration

def show_text_sequence(texts, interval=2):
    total_time = 0
    for text in texts:
        invoke(show_text, text, interval, delay=total_time)
        total_time += interval


cube1 = InteractableCube(name='man1', position=(3, 0, 3), scale=(0.4, 0.4, 0.4), rotation=(-90, 0, 90))
cube2 = InteractableCube(name='man2', position=(-3, 0, -3), scale=(0.4, 0.4, 0.4), rotation=(-90, 0, 90))

previous_hovered_entity = None

def update():
    global previous_hovered_entity
    hit_info = raycast(camera.world_position, camera.forward, distance=3)
    
    if hit_info.hit and isinstance(hit_info.entity, InteractableCube):
        hovered_entity = hit_info.entity
        
        hovered_entity.on_hover()
        
        if held_keys['e']:
            hovered_entity.interact()
            if hovered_entity.name == 'man1':
                show_text("hello, I'm 1", 2)
            if hovered_entity.name == 'man2':
                show_text("hello, I'm 2", 2)

        if previous_hovered_entity and previous_hovered_entity != hovered_entity:
            previous_hovered_entity.on_unhover()

        previous_hovered_entity = hovered_entity

    else:
        if previous_hovered_entity:
            previous_hovered_entity.on_unhover()
            previous_hovered_entity = None

app.run()
