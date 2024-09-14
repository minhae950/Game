from ursina import *

app = Ursina()

def show_temporary_text(text, duration=2):
    # 텍스트 생성
    message = Text(text, position=(0, 0.4), origin=(0, 0), scale=2)
    
    # 일정 시간 후에 텍스트 제거
    invoke(message.disable, delay=duration)
    return duration  # 다음 텍스트를 표시할 시간을 위해 duration 반환

def show_text_sequence(texts, interval=2):
    total_time = 0
    
    for text in texts:
        # 각 텍스트를 표시하는 함수를 invoke로 예약
        invoke(show_temporary_text, text, interval, delay=total_time)
        total_time += interval  # 각 텍스트가 표시되는 시간을 누적

# 텍스트 시퀀스 예제
texts = ["Hello, World!", "Welcome to Ursina!", "This is a sequence of messages."]

# 텍스트를 순차적으로 2초 간격으로 표시
show_text_sequence(texts, interval=2)

app.run()
