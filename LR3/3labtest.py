import random
import time
import threading

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

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

# Пример использования
if __name__ == "__main__":
    # Генерация случайного массива
    arr = [random.randint(1, 100) for _ in range(100)]
    print("Исходный массив:", arr)

    # Измерение времени
    start_time = time.time()
    sorted_arr = parallel_quick_sort(arr, 4)  # Использование 4 потоков
    end_time = time.time()

    print("Отсортированный массив:", sorted_arr)
    print("Время выполнения:", end_time - start_time)
