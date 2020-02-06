def Sawatdee(name='สมปอง'):
    print('สวัสดี', name)
    print('How are you?')
    print('------')

Sawatdee('robert')

#for - วนลูปสิ่งที่อยู่ใน list
for i in range(5):
    print('hello world', i)

for krang in range(3):
    print('Hello', krang)

for i in range(0, 20, 5): #0-19 -> 4รอบ
    print('Hello', i)

for i in range(0, 21, 5): #0-20 -> 5 รอบ
    print('Hello', i)

print(list(range(3)))

for i in [10, 20, 30]:
    print(i)

for i in [10, 20, '1st', '2nd']:
    print(i)

friend = ['A', 'B', 'C']
for f in friend:
    print(f)