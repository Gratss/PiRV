import threading
import math

# Функция для вычисления значения y[i] с использованием ряда Тейлора
def taylor_series(i, N, n):
    result = 0
    for k in range(n):
        result += (-1)**k * (2 * math.pi * i / N) ** (2 * k) / math.factorial(2 * k)
    return result

# Функция для вычисления и вывода значения
def calculate_y_thread(i, N, n):
    y_i = taylor_series(i, N, n)
    print(f"Thread {threading.get_ident()}: y[{i}] = {y_i}")
    return y_i

# Главная функция для создания потоков
def main_threaded(K, N, n):
    threads = []
    results = []
    for i in range(K):
        thread = threading.Thread(target=lambda i=i: results.append(calculate_y_thread(i, N, n)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_sum = sum(results)
    with open('result_threaded.txt', 'w') as file:
        file.write(str(total_sum))

# Ввод данных от пользователя
K = int(input("Введите K: "))
N = int(input("Введите N: "))
n = int(input("Введите количество членов ряда Тейлора: "))

main_threaded(K, N, n)
