#вправа 1
a=60
b=60
a=a*b
print(a)
#вправа2
seconds_per_hour = a
#вправа3
c=24
c=seconds_per_hour*c
print(c)
#вправа4
c=24
c=seconds_per_hour*c
seconds_per_day = c
print(seconds_per_day)
#вправа5
d = seconds_per_day/seconds_per_hour
print(d)
#вправа6
d = seconds_per_day//seconds_per_hour
print(d)
#якщо не враховувати .0 вкінці, то значення збігаються з попередньою вправою
#вправа7
print(6+6)
print(24-12)
print(36//3)
print(3*4)
#задача8
number='17'
print('my favorite number is - ' + number)
#задача9
name = 'Nastia'
print(str.lower(name))
print(str.upper(name))
print(str.swapcase(name))
#задача10
poem = '''Yes, I will smile, indeed, through tears and weeping
... Sing my songs where evil holds its sway,
... Hopeless, a steadfast hope forever keeping,
... I shall live! You thoughts of grief, away!'''

print(poem)

t=poem.startswith('Yes')
print(t)

p=poem.endswith('I shall live!')
print(p)

j=poem.find(',')
print(j)

w=poem.rfind(',')
print(w)

x=poem.count(',')
print(x)

h=poem.isalnum()
print(h)






#Задачі
#задача1
a = 'hello'
print(a)
a = 'hi'
print(a)

#задача2
name = input("Enter your name:")
print("Hello," +name+ "would you like to learn some Python today?")

#задача3
famous_person = 'Уолт Дісней'
message='Кращий спосіб почати робити – перестати говорити і почати робити.'
print(famous_person + 'одного разу сказав' + message)

#задача5
print("Дамян Анастасія \n Україна \n 5008 \n м. Чернівці \n бульвар героїв Крут 4\n")
#задача6
me=15
i=590.55
f=49.21
m=0.009321
y=16.40
print("{0:f} {1:f} {2:f} {3:f} {4:f}" .format(me, i, f, m, y ))
#задача7
days_holiday = 14
hours_holiday = 24*days_holiday
minutes_holiday=60*hours_holiday
seconds_haliday=60*minutes_holiday
print("{:<10} {:<10} {:<10} ".format(hours_holiday,minutes_holiday,seconds_haliday))
#задача8
c=13
f = 32 + 9/5 * c
k = c + 273,15
print(f"{k}")
print(f"{f}")
