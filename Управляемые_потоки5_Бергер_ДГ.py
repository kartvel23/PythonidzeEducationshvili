print((2+2+2 >= 6) and (-1* -1 <0))
#False
print((4*2 <= 8) and (7-1 == 6))
#True
print((2-1 > 3) or (-5*2 == -10))
#True
print((9+5 <= 15) or (7 != 4+3))
#True

#Another task
name = input("Введите имя пользователя: ")
ARM = int(input("Введите номер АРМ: "))

if (name=='Дмитрий' and ARM==1) or (name=='Ангелина' and ARM==2) or (name=='Василий' and ARM==3) or (name=='Екатерина' and ARM==4):
    print('Добро пожаловать!')
elif name=='Дмитрий' and ARM!=1:
    print('Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!')
else:
    print('Логин или пароль не верный, попробуйте еще раз')

#Another task
print((2-1 > 3) or (-5*2 == -10))
#True
print((9+5 <= 15) or (7 != 4+3))
#True

#Another task
grade=float(input('Введите ср. балл'))
if grade>=4:
  print('A')
elif grade>=3:
  print('B')
elif grade>=2:
  print('C')
elif grade>=1:
  print('D')
else:
  print('F')
