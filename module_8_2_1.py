def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
    new_tuple = (result, incorrect_data)
    return new_tuple


if __name__ == "__main__":
    mix_list = [1, 2, 'a', 4, 5, None, 6]
    w = personal_sum(mix_list)