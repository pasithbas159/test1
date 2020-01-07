#writeexcel.py
from openpyxl import Workbook
#จาก library ที่ชื่อว่า openpyxl ดึงคลาส Workbook
# Python > Library > Python File > Class > Function > Variables > Values

excelfile = Workbook() #สร้างไฟล์ excel ใน python

sheet = excelfile.active #เลือกWorksheetที่กำลังเปิดอยู่

sheet['C3'] = 'Hello' #จะทับข้อมูลเก่า

sheet.cell(row=3, column=4).value = 'world'

#data = ['Uncle', 100, '100']
#sheet.append(data)

excelfile.save('Result.xlsx')
print('Done!')
