from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# 플레이어 설정
player = FirstPersonController()

# 바닥 생성
floor = Entity(model='plane', scale=(10, 1, 10), texture='white_cube', texture_scale=(10, 10), collider='box')

health_bar_background = Entity(model='quad', color=color.gray, scale=(0.4, 0.05), position=(-0.5, 0.4, -0.1), parent=camera.ui)
health_bar = Entity(model='quad', color=color.green, scale=(0.38, 0.04), position=(-0.5, 0.4, -0.2), parent=camera.ui)
health_text = Text(text="Health", position=(-0.85, 0.42), scale=1.5, parent=camera.ui)

ammo_count = Text(text='Ammo: 30', position=(0.7, -0.45), scale=2, parent=camera.ui)

hp=8

def reduce_health():
    global hp
    if health_bar.scale_x > 0:
        health_bar.scale_x -= 0.05
        health_bar.x -= 0.025
        hp -= 1
    if hp <= 0:
        gameover_text = Text(text='Game Over', position=(-0.1, 0.015), scale=1.5, parent=camera.ui)

def reduce_ammo():
    current_ammo = int(ammo_count.text.split(': ')[1])
    if current_ammo > 0:
        current_ammo -= 1
        ammo_count.text = f'Ammo: {current_ammo}'

def input(key):
    if key == 'space':
        reduce_health()
        reduce_ammo()
    if key == 'escape':
        application.quit()

app.run()
