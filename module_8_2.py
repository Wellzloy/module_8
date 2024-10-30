def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы: {i}")
    new_tuple = (result, incorrect_data)
    return new_tuple


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple, str)):
            raise TypeError("В numbers записан некорректный тип данных")

        if not numbers:
            return 0

        sum_of_numbers, incorrect_data = personal_sum(numbers)

        if sum_of_numbers is None or len(numbers) - incorrect_data == 0:
            return 0

        average = sum_of_numbers / (len(numbers) - incorrect_data)

        return average
    except ZeroDivisionError as exc:
        print(exc)
        return 0
    except TypeError as exc:
        print(exc)
        return None


if __name__ == "__main__":
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
