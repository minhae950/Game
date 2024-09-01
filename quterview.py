from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()

# 3D 모델 엔티티 생성
model_path = 'man.obj'  # 모델 파일의 경로를 지정합니다.
model_entity = Entity(model=model_path, scale=(1, 1, 1), color=color.orange)
model_entity.rotation = ()

# 모델의 가시성을 제어할 변수
model_visible = True

def update():
    global model_visible

    # 스페이스 키를 눌러서 모델 숨기기 또는 보이기
    if held_keys['space']:
        if model_visible:
            model_entity.visible = False
        else:
            model_entity.visible = True
        model_visible = not model_visible  # 상태 반전

app.run()
