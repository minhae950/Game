from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

ground = Entity(model='plane', scale=(50, 1, 50), texture='white_cube', texture_scale=(20, 20), collider='box')

# InteractableCube 클래스 정의
class InteractableCube(Entity):
    def __init__(self, name, color=color.azure, position=(0, 0, 0), **kwargs):
        super().__init__(
            model='cube',
            color=color,
            collider='box',
            position=position,
            name=name,
            **kwargs
        )
        self.original_color = self.color

    def interact(self):
        print(f"Interacted with {self.name}")
        self.color = color.red  # 상호작용 시 색상 변경

    def on_hover(self):
        self.color = color.green  # 마우스 커서를 올리면 색상을 초록색으로 변경

    def on_unhover(self):
        self.color = self.original_color  # 마우스 커서가 벗어나면 원래 색상으로

# 플레이어 초기화
player = FirstPersonController()

# 상호작용할 수 있는 큐브 생성
cube1 = InteractableCube(name='Cube 1', color=color.azure, position=(3, 1, 3))
cube2 = InteractableCube(name='Cube 2', color=color.orange, position=(-3, 1, -3))

# 이전에 마우스 커서를 올렸던 오브젝트를 추적하기 위한 변수
previous_hovered_entity = None

def update():
    global previous_hovered_entity

    hit_info = raycast(camera.world_position, camera.forward, distance=3)
    
    if hit_info.hit and isinstance(hit_info.entity, InteractableCube):
        hovered_entity = hit_info.entity
        # 마우스 커서를 올린 오브젝트에서 on_hover 메서드 호출
        hovered_entity.on_hover()

        if held_keys['e']:  # 'E' 키를 눌러 상호작용
            hovered_entity.interact()

        # 이전에 다른 오브젝트를 가리키고 있었을 경우, on_unhover 메서드 호출
        if previous_hovered_entity and previous_hovered_entity != hovered_entity:
            previous_hovered_entity.on_unhover()

        previous_hovered_entity = hovered_entity

    else:
        # 어떤 `InteractableCube`도 가리키지 않을 경우 이전 오브젝트의 색상 초기화
        if previous_hovered_entity:
            previous_hovered_entity.on_unhover()
            previous_hovered_entity = None

app.run()
