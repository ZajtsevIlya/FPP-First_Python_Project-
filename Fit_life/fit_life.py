# Проект FitLife - MVP версия 1.0


def base_parametrs():
    """Функция для расчёта параметров."""
    print("\nДобро пожаловать в Ваш личный фитнес-помощник.")
    user_name = input("\nКак я могу Вас называть? ").title()
    user_age = int(input(f"\n{user_name}, укажите Ваш возраст: "))
    user_weight = float(input("\nВведите Ваш вес в кг (например, 75.5): "))
    user_height = float(input("\nИ Ваш рост в метрах (например, 1.67): "))
    bmi = user_weight / (user_height ** 2)
    bmi_r = round(bmi, 1)
    water_l = (user_weight * 30) / 1000
    water_r = round(water_l, 2)
    print("\n" + "=" * 50)
    print(f"Всё готово! {user_name} ({user_age} г.).\n")
    print(f"\nИМТ: {bmi_r}\n")
    print(f"\nНорма воды: {water_r} литра в день.")
    print("=" * 50)
    print("\nКонтролируйте водный баланс и будьте на высоте!")
    print("\nХорошего Вам дня!\n")


base_parametrs()
