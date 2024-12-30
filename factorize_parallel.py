from multiprocessing import Pool, cpu_count
import time

def find_factors(n):
    """
    Знаходить усі дільники числа n.
    """
    return [i for i in range(1, n + 1) if n % i == 0]

def factorize_parallel(*numbers):
    """
    Функція знаходить дільники для чисел паралельно.
    """
    with Pool(cpu_count()) as pool:
        results = pool.map(find_factors, numbers)
    return results

# Тест паралельної версії
start_time = time.time()
a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)
end_time = time.time()

print(f"Паралельна версія виконана за {end_time - start_time:.2f} секунд")
print(a)
print(b)
print(c)
print(d)
