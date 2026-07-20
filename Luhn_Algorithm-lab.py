def verify_card_number(card_number: str) -> str:
    numbers = list(card_number)
    length_numbers = len(numbers)
    k = 0
    while k < length_numbers:
        if not numbers[k] in [str(j) for j in range(10)]:
            if numbers[k] in ['-', ' ']:
                numbers.pop(k)
                length_numbers -= 1
            else:
                return 'INVALID!'
        else:
            k += 1
    total = 0
    for i in range(length_numbers):
        if (length_numbers - 1) % 2 == (length_numbers - 1 - i) % 2:
            total += int(numbers[-1 - i])
        else:
            number = 2 * int(numbers[-1 - i])
            if number <= 9:
                total += number
            else:
                number = list(str(number))
                for digit in number:
                    total += int(digit)
    if total % 10 != 0:
        return 'INVALID!'
    else:
        return 'VALID!' 