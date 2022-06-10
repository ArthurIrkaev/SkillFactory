import numpy as np


def guess(smallest=1, largest=101, number=1) -> int:
    """Функция угадывания заданного числа в заданном диапазоне.

    Args:
        smallest (int): Наименьшее значение диапазона поиска.
            По умолчанию 1.
        largest (int): Наибольшее значение диапазона поиска.
            По умолчанию 101.
        number (int): Число, которое необходимо угадать.
            По умолчанию 1.

    Returns:
        count (int): Количество попыток угадывания.
    """

    # Проверяем корректность передаваемых в функцию значений
    # аргументов smallest, largest и number
    if smallest > largest:
        raise ValueError('smallest не может быть больше largest')
    elif number < smallest or number > largest:
        raise ValueError('number не входит в заданный диапазон')

    # Задаем начальное значение счетчика попыток
    count = 0

    # Диапазон поиска можно представить,
    # как сортированный список чисел от smallest к largest
    # и применить бинарный поиск.
    # Переменной guessed_number присваиваем начальное значение,
    # равное середине диапазона поиска.
    guessed_number = int((largest+smallest) / 2)
    while True:
        # Если guessed_number равно заданному числу,
        # то увеличиваем счетчик попыток на 1,
        # и выходим из цикла while
        if guessed_number == number:
            count += 1
            break
        # Если guessed_number больше заданного числа,
        # то увеличиваем счетчик попыток на 1,
        # изменяем диапазон поиска, в котором наибольшим числом становится
        # текущее значение переменной guessed_number,
        # а переменной guessed_number присваиваем новое значение,
        # равное середине обновленного диапазона поиска.
        elif guessed_number > number:
            count += 1
            largest = guessed_number
            guessed_number = int(((largest+smallest) / 2))
        # Если guessed_number меньше заданного числа,
        # то увеличиваем счетчик попыток на 1,
        # изменяем диапазон поиска, в котором наименьшим числом становится
        # текущее значение переменной guessed_number,
        # а переменной guessed_number присваиваем новое значение,
        # равное середине обновленного диапазона поиска.
        elif guessed_number < number:
            count += 1
            smallest = guessed_number
            guessed_number = int(((largest+smallest) / 2))

    return count


def average_tries(smallest=1, largest=101, func=guess) -> int:
    """Функция расчета среднего значения попыток угадывания заданного числа
    при 1000 повторениях.

    Args:
        smallest (int): Наименьшее значение диапазона поиска.
            По умолчанию 1.
        largest (int): Наибольшее значение диапазона поиска.
            По умолчанию 101.
        func (function): Функция угадывания заданного числа.
            По умолчанию guess.

    Returns:
        score (int): Среднее значение попыток поиска
    """

    # Создаем список для хранения значений попыток поиска заданного числа
    count_list = []
    # Задаем условие для получения идентичных случайных последовательностей
    np.random.seed(1)
    # Создаем массив случайных чисел размером size
    random_array = np.random.randint(smallest, largest, size=(1000))

    for number in random_array:
        count_list.append(func(smallest, largest, number))

    # Находим среднее значение попыток поиска
    score = int(np.mean(count_list))

    return score


if __name__ == '__main__':
    # Задаем диапазон для случайного загадывания числа,
    # где smallest - начальное значение, а largest - конечное
    smallest, largest = 1, 101
    # Создаем случайное число для поиска
    number = np.random.randint(smallest, largest)

    print(f'Число {number} найдено', end=' ')
    print(f'за {guess(smallest, largest, number)} попыток(ки).')
    print(f'Алгоритм угадывает число в среднем', end=' ')
    print(f'за {average_tries(smallest, largest)} попыток.')
