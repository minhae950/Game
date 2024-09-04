from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()
crosshair = Entity(model = 'cube', color = color.red, scale = (0.003, 0.003), position = (0, 0, 0))
camera.fov = 100

model = Entity(model='./model.obj', scale = (0.37, 0.37, 0.37), position = (0, -0.8, 10))

# 메쉬의 크기를 확인하기 위해 모델의 bounding_box를 사용
#print('Bounding box size:', model.model.bounds)

# BoxCollider를 사용해 모델 크기에 맞는 콜라이더 설정
model.collider = BoxCollider(model, center=(0, 0, 0), size=model.scale)

app.run()
