import math

# Функция для вычисления значения y[i] с использованием ряда Тейлора
def taylor_series(i, N, n):
    result = 0
    for k in range(n):
        result += (-1)**k * (2 * math.pi * i / N) ** (2 * k) / math.factorial(2 * k)
    return result

# Главная функция для последовательного вычисления
def main_sequential(K, N, n):
    total_sum = 0
    for i in range(K):
        y_i = taylor_series(i, N, n)
        print(f"y[{i}] = {y_i}")
        total_sum += y_i

    with open('result_sequential.txt', 'w') as file:
        file.write(str(total_sum))

# Ввод данных от пользователя
K = int(input("Введите K: "))
N = int(input("Введите N: "))
n = int(input("Введите количество членов ряда Тейлора: "))

main_sequential(K, N, n)
