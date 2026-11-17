from microbit import *

display.show(Image.HAPPY)
pin2.write_digital(0)
state = 0

while True:
    # 假设按下时读取为1（根据你的硬件接线确认，如果是下拉电阻按键按下为1）
    if pin0.read_digital() == 1:
        sleep(50)  # 消抖
        if pin0.read_digital() == 1:  # 确认真的按下了
            # 翻转状态
            if state == 0:
                pin2.write_digital(1)
                state = 1
            else:
                pin2.write_digital(0)
                state = 0
            
            # 关键：等待按键松开，防止按住时状态一直翻转
            while pin0.read_digital() == 1:
                sleep(10)