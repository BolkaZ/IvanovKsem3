import math


def get_coefficient(prompt):
    while True:
        try:
            coefficient = float(input(prompt))
            return coefficient
        except ValueError:
            print("Ошибка: Введите корректное значение для коэффициента.")


def solve_biquadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant >= 0:
        sqrt_discriminant = math.sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)
        if root1 > 0:
            root3 = math.sqrt(root1)
            print(root3, -root3)
        if root2 > 0:
            root4 = math.sqrt(root2)
            print(root4, -root4)
    else:
        # Нет действительных корней
        return None


def main():
    try:
        # Вводим коэфициенты уравнения
        a = get_coefficient("Введите коэффициент A: ")
        b = get_coefficient("Введите коэффициент B: ")
        c = get_coefficient("Введите коэффициент C: ")

        # Вызов решения уравнения
        roots = solve_biquadratic(a, b, c)
        if roots:
            print("Корни биквадратного уравнения:", roots)
        else:
            print("Биквадратное уравнение не имеет действительных корней.")
    except KeyboardInterrupt:
        print("\nПрограмма завершена.")


if __name__ == "__main__":
    main()
