# Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет
# с шестизначным номером, где сумма первых трех цифр равна сумме
# последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

n = int(input("Введите 6 - ти значный номер билета"))
n1 = n // 1000
n2 = n % 1000 
summa1 = 0
summa2 = 0
while n1 > 0:
    summa1 += n1 % 10
    n1 = n1 // 10
while n2 > 0:
    summa2 += n2 % 10
    n2 = n2 // 10
if (summa1 == summa2):
    print("У вас счастливый билет")
else:
    print("Ваш билет не счастливый")