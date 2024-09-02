from ursina import *

app = Ursina()

# 텍스트와 버튼 생성
title = Text(text='Game Menu', position=(0, 0.3), scale=2, color=color.orange)
start_button = Button(text='Start', color=color.azure, scale=(0.3, 0.1), position=(0, 0.1))
exit_button = Button(text='Exit', color=color.red, scale=(0.3, 0.1), position=(0, -0.1))

# 버튼 클릭 시 동작 설정
def start_game():
    title.text = "Game Started!"

def exit_game():
    application.quit()

start_button.on_click = start_game
exit_button.on_click = exit_game

app.run()