#ep2copybot.py
import pyautogui as pg
import time

#############################Line1####################
#ใช้เมาส์คลิกไผยังตำแหน่งที่ต้องการก๊อปปี้ (ด้านหน้า)
time.sleep(1) #รอ1วินาที
start_point = (1050, 254)
pg.click(start_point)

#ลากไปให้สุดบรรทัด
time.sleep(1)
end_point = (1400, 254)
pg.dragTo(end_point, duration = 1)

#กดปุ่ม Ctrl+C
pg.hotkey('ctrl', 'c')

#ขยับเมาส์ไปทางด้านซ้าย
left_box2 = (650, 254)
pg.click(left_box2)

#กดปุ่ม Ctrl+V เพื่อวาง แล้วกด Enter
pg.hotkey('ctrl', 'v')
pg.press('enter')


#############################Line2####################
#ใช้เมาส์คลิกไผยังตำแหน่งที่ต้องการก๊อปปี้ (ด้านหน้า)
time.sleep(1) #รอ1วินาที
start_point = (1050, 296)
pg.click(start_point)

#ลากไปให้สุดบรรทัด
time.sleep(1)
end_point = (1400, 296) #254+42 = 296
pg.dragTo(end_point, duration = 1)

#กดปุ่ม Ctrl+C
pg.hotkey('ctrl', 'c')

#ขยับเมาส์ไปทางด้านซ้าย
left_box2 = (650, 254)
pg.click(left_box2)
#กดลูกศรลง
pg.press('down')

#กดปุ่ม Ctrl+V เพื่อวาง แล้วกด Enter
pg.hotkey('ctrl', 'v')
pg.press('enter')

#############################Line3####################
#ใช้เมาส์คลิกไผยังตำแหน่งที่ต้องการก๊อปปี้ (ด้านหน้า)
time.sleep(1) #รอ1วินาที
start_point = (1050, 336)
pg.click(start_point)

#ลากไปให้สุดบรรทัด
time.sleep(1)
end_point = (1400, 336)
pg.dragTo(end_point, duration = 1)

#กดปุ่ม Ctrl+C
pg.hotkey('ctrl', 'c')

#ขยับเมาส์ไปทางด้านซ้าย
left_box2 = (650, 254)
pg.click(left_box2)
#กดลูกศรลง
pg.press('down')
pg.press('down')

#กดปุ่ม Ctrl+V เพื่อวาง แล้วกด Enter
pg.hotkey('ctrl', 'v')
pg.press('enter')



