# Проект FitLife - MVP версия 1.0
# import time


def base_parameters():
    """Сбор параметров пользователя и расчет ИМТ и нормы воды."""
    print(
        "Здравствуйте! Добро пожаловать в Ваш личный фитнес-помощник.",
        flush=True
    )
    # time.sleep(1.3)

    user_name = input("\nКак я могу Вас называть? ").title()
    user_age = int(input(f"\n{user_name}, укажите Ваш возраст: "))

    weight_prompt = f"\n{user_name}, введите Ваш вес в кг (например, 75.5): "
    user_weight = float(input(weight_prompt))

    height_prompt = "\nИ Ваш рост в метрах (например, 1.67): "
    user_height = float(input(height_prompt))

    bmi = user_weight / (user_height ** 2)
    bmi_r = round(bmi, 1)

    water_1 = (user_weight * 30) / 1000
    water_r = round(water_1, 2)

    print("\n" + "=" * 50)

    print(
        f"Всё готово! {user_name} ({user_age} л.).\n"
        f"ИМТ: {bmi_r}\n"
        f"Норма воды: {water_r} литра в день."
    )
    print("-" * 50)
    # time.sleep(1.5)

    print("\nКонтролируйте водный баланс и будьте на высоте!")
    # time.sleep(0.75)
    print("\nХорошего Вам дня!\n")


base_parameters()
