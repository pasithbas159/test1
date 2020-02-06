#ep2copybot.py
import pyautogui as pg
import time
# 1 บรรทัด = 30 pixels
def CopyText(nextline=0):
    
    #############################Line1####################
    #ใช้เมาส์คลิกไผยังตำแหน่งที่ต้องการก๊อปปี้ (ด้านหน้า)
    time.sleep(1) #รอ1วินาที
    start_point = (1050, 254 + nextline)
    pg.click(start_point)

    #ลากไปให้สุดบรรทัด
    time.sleep(1)
    end_point = (1400, 254 + nextline)
    pg.dragTo(end_point, duration = 1)

    #กดปุ่ม Ctrl+C
    pg.hotkey('ctrl', 'c')

    #ขยับเมาส์ไปทางด้านซ้าย
    left_box2 = (650, 254 + nextline)
    pg.click(left_box2)

    #กดปุ่ม Ctrl+V เพื่อวาง แล้วกด Enter
    pg.hotkey('ctrl', 'v')
    pg.press('enter')

for i in range(5):
    CopyText(30*i)
