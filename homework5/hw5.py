import time
# Инициализация суммы
total_sum = 0

print("Введите числа для подсчета суммы. Введите 'stop' или 'end' для завершения ввода.")

while True:
    user_input = input("Введите число: ")
    
    # Проверка на завершение ввода
    if user_input.lower() in ['stop', 'end']:
        break
    
    try:
        # Преобразование ввода в число и добавление к общей сумме
        number = float(user_input)  #для поддержки дробных чисел
        total_sum += number
    except ValueError:
        print("Пожалуйста, введите действительное число или 'stop'/'end' для завершения.")

# Вывод суммы
print(f"Сумма введённых чисел: {total_sum}")
time.sleep(5)
