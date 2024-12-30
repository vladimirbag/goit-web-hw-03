import time

def factorize_sync(*numbers):
    """
    Функція знаходить усі дільники для переданих чисел.
    """
    def find_factors(n):
        return [i for i in range(1, n + 1) if n % i == 0]

    return [find_factors(number) for number in numbers]

# Тест синхронної версії
start_time = time.time()
a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
end_time = time.time()

print(f"Синхронна версія виконана за {end_time - start_time:.2f} секунд")
print(a)
print(b)
print(c)
print(d)