import multiprocessing
import math

# Функция для вычисления значения y[i] с использованием ряда Тейлора
def taylor_series(i, N, n):
    result = 0
    for k in range(n):
        result += (-1)**k * (2 * math.pi * i / N) ** (2 * k) / math.factorial(2 * k)
    return result

# Функция для вычисления и вывода значения
def calculate_y_process(i, N, n, queue):
    y_i = taylor_series(i, N, n)
    print(f"Process {multiprocessing.current_process().pid}: y[{i}] = {y_i}")
    queue.put(y_i)

# Главная функция для создания процессов
def main_multiprocessing(K, N, n):
    queue = multiprocessing.Queue()
    processes = []
    for i in range(K):
        process = multiprocessing.Process(target=calculate_y_process, args=(i, N, n, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_sum = 0
    while not queue.empty():
        total_sum += queue.get()

    with open('result_multiprocessing.txt', 'w') as file:
        file.write(str(total_sum))

# Ввод данных от пользователя
K = int(input("Введите K: "))
N = int(input("Введите N: "))
n = int(input("Введите количество членов ряда Тейлора: "))

main_multiprocessing(K, N, n)
