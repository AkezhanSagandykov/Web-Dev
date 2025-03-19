def power(a, n):
    if n == 0:  # Любое число в степени 0 равно 1
        return 1.0
    if a == 0 and n > 0:  # 0^n = 0
        return 0.0
    if a < 0 and n % 2 == 0:  # Отрицательное число в четной степени становится положительным
        return power(-a, n)
    
    result = 1.0
    base = a
    while n > 0:
        if n % 2 == 1:  # Если степень нечетная, умножаем результат на текущее основание
            result *= base
        base *= base  # Возводим основание в квадрат
        n //= 2  # Делим степень на 2

    return result

# Ввод данных
float_num, int_num = input().split()
a = float(float_num)
n = int(int_num)

# Вывод результата
print(power(a, n))