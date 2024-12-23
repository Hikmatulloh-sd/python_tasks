# 1) Дано трехзначное число. Проверить истинность высказывания: 
# «Все цифры данного числа различны».
# # 5 6 7 => True 
# 5 5 5 => False 

number = 554

check_num = set(str(number))

if len(check_num) == 3:
    print(True)
else:
    print(False)

# 2) Даны числа x, y. Проверить истинность высказывания: 
# «Точка с координатами (x, y) лежит во второй координатной четверти».
#         y
#     1   |   2
#         |
#         |  
#   --------------
#         | x
#     3   |   4
#         |

x = 4 
y = -2


if x > 0 and y > 0:
    print(True)
else:
    print(False )

# 3) Дано целое число N (> 0). 
# Используя операции деления нацело и взятия остатка от деления, 
# вывести все его цифры, начиная с самой правой (разряда единиц).
n = 945


while True:
    print(n % 10)
    n = n // 10

    if n == 0 :
        break

# 4) Дано целое число N (> 0). 
# С помощью операций деления нацело и взятия остатка от деления определить, 
# имеется ли в записи числа N цифра «2». Если имеется, то вывести TRUE, 
# если нет — вывести FALSE.
n = 5 
n = 942

flag = 0
while True:
    r = n % 10
    n = n // 10

    if r == 2:
        flag = True
        break
    else:
        flag = False

    if n == 0 :
        break
print(flag)

# 5) Дано целое число N (> 0). Используя один цикл, найти сумму
# 1+1/(1!)+1/(2!)+1/(3!)+...+1/(N!)
import math

n = 7 
s = 1

for i in range(1,7+1):
    s += 1 / (math.factorial(i))

print(s)

# 6) Дан номер года (положительное целое число). 
# Определить количество дней в этом году, учитывая, 
# что обычный год насчитывает 365 дней, а високосный — 366 дней. 
# Високосным считается год, делящийся на 4, за исключением тех годов, 
# которые делятся на 100 и не делятся на 400 (например, годы 300, 1300 и 1900 
# не являются високосными, а 1200 и 2000 — являются).
year = 2024
day = 0

if year % 2 == 0:
    if year % 100 == 0 and year % 400:
        day = 355
    else:
        day = 366
print(day)

3