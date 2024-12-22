# 1) Даны два целых числа A и B (A < B). 
# Вывести в порядке убывания все целые числа, 
# расположенные между A и B (не включая числа A и B), 
# а также количество N этих чисел.
a = 5 
b = 14

n = 0
for i in range(b - 1,a,-1):
    print(i)
    n += 1 
print("Количество чисел: ",n)

# 2) Дано целое число N (> 0). Найти сумму
# 1 + 1/2 + 1/3 + ... + 1/N
# (вещественное число).
n = 7 
s = 0

for i in range(1,n+1):
    s += 1 / i

print(s)
# 3) Дано целое число N (> 0). Найти произведение
# 1.1⋅1.2⋅1.3⋅...
# (N сомножителей).
n = 15
s = 1 

for i in range(1,n):
    s *= 1 + i / 10

print(s)
# 4) Дано целое число A и целое число N (> 0). Найти A в степени N :
# AN=A⋅A⋅...⋅A
# (числа A перемножаются N раз).
n = 5 
a = 4 
r = 1

for _ in range(1,5+1):
    r *= a

print(r) 

# 5) Дано вещественное число A и целое число N (> 0). Используя один цикл, найти значение выражения
# 1−A+A^2−A^3+...+(−1)^N⋅A^N.
# Условный оператор не использовать.