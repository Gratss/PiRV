import random
import time
import concurrent.futures

# Функция для последовательного поиска минимального значения
def find_min_sequential(arr):
    return min(arr)

# Функция для параллельного поиска минимального значения
def find_min_parallel(arr):
    def worker(sublist):
        return min(sublist)
    
    # Разделим данные на несколько частей
    num_workers = 4
    chunk_size = len(arr) // num_workers
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        results = list(executor.map(worker, chunks))
    
    return min(results)

# Генерация случайных данных
N = 1000000
arr = [random.randint(0, 1000) for _ in range(N)]

# Последовательное выполнение
start_time = time.time()
find_min_sequential(arr)
seq_time = time.time() - start_time

# Параллельное выполнение
start_time = time.time()
find_min_parallel(arr)
par_time = time.time() - start_time

# Вычисление ускорения
speedup = seq_time / par_time

# Вывод результатов
print(f"Последовательное время: {seq_time:.4f} секунд")
print(f"Параллельное время: {par_time:.4f} секунд")
print(f"Ускорение: {speedup:.2f}")
