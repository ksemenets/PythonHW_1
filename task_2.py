# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

n = int (input("Введите 3-х значное число"))
summa = 0
while n > 0:
    summa = summa + n % 10
    n = n // 10
print(summa)