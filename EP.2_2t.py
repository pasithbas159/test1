from openpyxl import Workbook

excelfile = Workbook()
sheet = excelfile.active

allname = ['Prayut',
           'Taksin',
           'Parina',
           'Mongkolrit',
           'Prawit',
           'Thanatorn',
           'Chatchat',
           'Sudarat',
           'Anuthin',
           'Somchai']

#print(allname[0][0]) [0] -> index [0] -> ตัวอักษร

'''
---for loop---
for i in range(3):
    print(i)
------OR------
range(3)
list(range(3))
for i in [0,1,2]:
    print(i) #เหมือนกัน
'''

'''
checkname = {}
if 'A' in checkname.keys():
    print('OK')

checkname = {}
'''

checkname = {}

for nm in allname:
    #print(nm[0])

    if nm[0] not in checkname.keys():
        checkname[nm[0]] = 1
        sheet[nm[0]+'1'] = nm
    else:
        checkname[nm[0]] = checkname[nm[0]] + 1
        sheet[nm[0] + str(checkname[nm[0]])] = nm

print(checkname)

excelfile.save('Allname.xlsx')

'''
---Manual---
sheet['P1'] = allname[0]
sheet['T1'] = allname[1]
sheet['P1'] = allname[2]
sheet['M1'] = allname[3]
sheet['P3'] = allname[4]
sheet['T2'] = allname[5]
---Dictionary---
count = {'A':1, 'p':2}
print(count['A'])

count['A'] = count['A'] + 1
print(count['A'])

count.keys()
list(count.keys())
'A' in ['A', 'p']
if 'A' in ['A', 'p']:
    print('มีเออยู่ด้านใน')
'''

