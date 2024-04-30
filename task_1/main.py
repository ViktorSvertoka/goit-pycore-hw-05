def caching_fibonacci() -> callable:
    cache = {}  # словник для зберігання результатів обчислень

    def fibonacci(n: int) -> int:
        # Якщо n <= 0, повертаємо 0
        if n <= 0:
            return 0
        # Якщо n == 1, повертаємо 1
        elif n == 1:
            return 1
        # Якщо n вже є у кеші, повертаємо його значення
        elif n in cache:
            return cache[n]
        # Якщо число не знаходиться у кеші, обчислюємо його рекурсивно
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci


# Приклад використання:
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
