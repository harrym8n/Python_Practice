from random import randint


def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers


def draw_winning_numbers():
    winning_num = generate_numbers(6)
    winning_num.sort()
    winning_num.append(randint(1, 45))

    return winning_num


def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for number in numbers:
        if number in winning_numbers:
            count += 1

    return count


def check(numbers, winning_numbers):
    bonus_num = winning_numbers[6]
    count_common = count_matching_numbers(numbers, winning_numbers[:6])

    if count_common == 6:
        return 100000000
    elif count_common == 5 and bonus_num in numbers:
        return 50000000
    elif count_common == 5:
        return 50000000
    elif count_common == 5:
        return 1000000
    elif count_common == 4:
        return 50000
    elif count_common == 3:
        return 5000
    else :
        return 0