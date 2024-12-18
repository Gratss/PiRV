import concurrent.futures
import time
import random
import math
import os

def generate_numbers(n):
    """Генерация n случайных чисел."""
    return [random.randint(-100, 100) for _ in range(n)]

def direct_scheme(numbers):
    """Прямая схема: последовательное вычисление."""
    return sum(x for x in numbers if x > 0)

def cascade_scheme(numbers, num_threads):
    """Каскадная схема: разбиение задачи между потоками."""
    def partial_sum(nums):
        return sum(x for x in nums if x > 0)

    chunk_size = max(1, math.ceil(len(numbers) / num_threads))
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for chunk in chunks:
            results.append(executor.submit(partial_sum, chunk))

    return sum(f.result() for f in results)

def modified_cascade_scheme(numbers, num_threads):
    """Модифицированная каскадная схема: балансировка нагрузки."""
    def partial_sum(start, end):
        return sum(x for x in numbers[start:end] if x > 0)

    chunk_size = max(1, math.ceil(len(numbers) / num_threads))
    ranges = [(i, min(i + chunk_size, len(numbers))) for i in range(0, len(numbers), chunk_size)]

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for start, end in ranges:
            results.append(executor.submit(partial_sum, start, end))

    return sum(f.result() for f in results)

def shifted_cascade_scheme(numbers, num_threads):
    """Каскадная схема со сдвигом: смещение при разбиении на подзадачи."""
    def partial_sum(start, end):
        return sum(x for x in numbers[start:end] if x > 0)

    chunk_size = max(1, math.ceil(len(numbers) / num_threads))
    ranges = [(i, min(i + chunk_size + 1, len(numbers))) for i in range(0, len(numbers), chunk_size)]

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for start, end in ranges:
            results.append(executor.submit(partial_sum, start, end))

    return sum(f.result() for f in results)

def measure_performance(numbers, num_threads):
    """Измерение ускорения и эффективности различных схем."""
    results = {}

    # Прямая схема
    start_time = time.time()
    direct_result = direct_scheme(numbers)
    direct_time = time.time() - start_time
    results['direct'] = (direct_result, direct_time, 1.0, 1.0)

    # Каскадная схема
    start_time = time.time()
    cascade_result = cascade_scheme(numbers, num_threads)
    cascade_time = time.time() - start_time
    results['cascade'] = (cascade_result, cascade_time, direct_time / cascade_time if cascade_time > 0 else 0, (direct_time / cascade_time / num_threads if cascade_time > 0 else 0))

    # Модифицированная каскадная схема
    start_time = time.time()
    modified_result = modified_cascade_scheme(numbers, num_threads)
    modified_time = time.time() - start_time
    results['modified_cascade'] = (modified_result, modified_time, direct_time / modified_time if modified_time > 0 else 0, (direct_time / modified_time / num_threads if modified_time > 0 else 0))

    # Каскадная схема со сдвигом
    start_time = time.time()
    shifted_result = shifted_cascade_scheme(numbers, num_threads)
    shifted_time = time.time() - start_time
    results['shifted_cascade'] = (shifted_result, shifted_time, direct_time / shifted_time if shifted_time > 0 else 0, (direct_time / shifted_time / num_threads if shifted_time > 0 else 0))

    return results

if __name__ == "__main__":
    n = 10**6  # Размер массива
    max_threads = os.cpu_count() or 4
    num_threads = min(4, max_threads)  # Количество потоков, ограниченное ядрами процессора

    numbers = generate_numbers(n)

    try:
        performance = measure_performance(numbers, num_threads)

        print("Результаты производительности:")
        for scheme, (result, exec_time, speedup, efficiency) in performance.items():
            print(f"{scheme.capitalize()} схема: результат={result}, время={exec_time:.4f}с, ускорение={speedup:.2f}, эффективность={efficiency:.2f}")
    except RuntimeError as e:
        print(f"Ошибка выполнения: {e}. Попробуйте уменьшить количество потоков или размер задачи.")


