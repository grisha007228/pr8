import time
# Запрашиваем у пользователя ввод двух чисел
a = int(input("Введите первое число (a): "))
b = int(input("Введите второе число (b): "))

# Определяем меньшее и большее число
start = min(a, b)
end = max(a, b)

# Выводим целые числа между a и b
print(f"Целые числа между {start} и {end}:")
for num in range(start + 1, end):
    print(num)
time.sleep(5)	
