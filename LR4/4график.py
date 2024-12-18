import time
import matplotlib.pyplot as plt

# Placeholder for your functions
def main_threaded(K, N, n):
    # Replace with your threaded implementation
    print("main_threaded is running with K=", K, ", N=", N, ", n=", n)
    # Placeholder for your calculations
    time.sleep(0.1) # simulate some work

def main_multiprocessing(K, N, n):
    # Replace with your multiprocessing implementation
    print("main_multiprocessing is running with K=", K, ", N=", N, ", n=", n)
    # Placeholder for your calculations
    time.sleep(0.2)  # simulate some work

def main_sequential(K, N, n):
    # Replace with your sequential implementation
    print("main_sequential is running with K=", K, ", N=", N, ", n=", n)
    # Placeholder for your calculations
    time.sleep(0.3)  # simulate some work

# Ввод данных
K = int(input("Введите K: "))
N = int(input("Введите N: "))
n = int(input("Введите количество членов ряда Тейлора: "))

# Замер времени для потоков
start_time = time.time()
main_threaded(K, N, n)
time_threaded = time.time() - start_time

# Замер времени для процессов
start_time = time.time()
main_multiprocessing(K, N, n)
time_multiprocessing = time.time() - start_time

# Замер времени для последовательного вычисления
start_time = time.time()
main_sequential(K, N, n)
time_sequential = time.time() - start_time

# График сравнения
labels = ['Threads', 'Multiprocessing', 'Sequential']
times = [time_threaded, time_multiprocessing, time_sequential]

plt.bar(labels, times, color=['blue', 'green', 'red'])
plt.ylabel('Time (seconds)')
plt.title('Comparison of Execution Times')
plt.show()