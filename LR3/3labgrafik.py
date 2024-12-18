import random
import time
import threading
import matplotlib.pyplot as plt

# Функция быстрой сортировки
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

# Параллельная быстрая сортировка
def parallel_quick_sort(arr, max_threads):
    if len(arr) <= 1:
        return arr
    
    # Создаем потоки до максимального количества
    if max_threads > 1:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        
        # Разделяем задачу на два потока
        thread1 = threading.Thread(target=parallel_quick_sort, args=(less, max_threads // 2))
        thread2 = threading.Thread(target=parallel_quick_sort, args=(greater, max_threads // 2))
        
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()

        return parallel_quick_sort(less, max_threads // 2) + [pivot] + parallel_quick_sort(greater, max_threads // 2)
    else:
        return quick_sort(arr)

# Функция для измерения времени выполнения
def measure_time(arr, max_threads):
    start_time = time.time()
    parallel_quick_sort(arr, max_threads)
    return time.time() - start_time

# Генерация случайного массива
arr = [random.randint(1, 1000) for _ in range(1000)]

# Число потоков для тестирования
threads_list = [1, 2, 4, 8, 16]
times = []

# Измеряем время для каждого числа потоков
for threads in threads_list:
    time_taken = measure_time(arr, threads)
    times.append(time_taken)

# Построение графика зависимости ускорения и коэффициента эффективности
serial_time = times[0]
speedup = [serial_time / t for t in times]  # Ускорение
efficiency = [s / t for s, t in zip(speedup, threads_list)]  # Коэффициент эффективности

# График ускорения
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(threads_list, speedup, marker='o')
plt.title("Зависимость ускорения от числа потоков")
plt.xlabel("Число потоков")
plt.ylabel("Ускорение")

# График коэффициента эффективности
plt.subplot(1, 2, 2)
plt.plot(threads_list, efficiency, marker='o', color='r')
plt.title("Зависимость коэффициента эффективности от числа потоков")
plt.xlabel("Число потоков")
plt.ylabel("Коэффициент эффективности")

plt.tight_layout()
plt.show()

# Оценка ускорения по закону Амдала
# Предполагаемая доля распараллеливаемой части программы (P)
P = 0.9  # Например, 90% программы можно распараллелить

# Теоретическое ускорение по закону Амдала
theoretical_speedup = [1 / ((1 - P) + P / p) for p in threads_list]

# График теоретического ускорения
plt.plot(threads_list, theoretical_speedup, marker='x', label="Амдал")
plt.plot(threads_list, speedup, marker='o', label="Реальное ускорение")
plt.title("Сравнение теоретического и реального ускорения")
plt.xlabel("Число потоков")
plt.ylabel("Ускорение")
plt.legend()
plt.show()
