from ursina import *

app = Ursina()
cube = Entity(model='cube', color=color.orange, scale=(2, 2, 2), position=(0, 1, 0), collider='box')
cube.highlight_color = color.black  # 윤곽선 색상 설정


def update():
    cube.set_shader_input("highlight_color", color.black)  # 윤곽선 적용

app.run()
