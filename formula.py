def newton_method(number, n, epsilon=1e-10, max_iter=1000):
    x = number / 2  # Начальное приближение
    for _ in range(max_iter):
        x_next = (1/n) * ((n-1) * x + number / x**(n-1))
        if abs(x_next - x) < epsilon:
            return x_next
        x = x_next
    return x

# Исходное число и степень
number = 25
root_degree = 2

# Используем метод Ньютона
result = newton_method(number, root_degree)

print(f"Корень в третьей степени из {number} (метод Ньютона) равен {result}")