# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5

def parse_int(input):
    single_digit = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                    'nine': 9}

    double_digit = {'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
                    'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40,
                    'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
    result = 0

    if len(input) == 0:
        return 0

    input = input.replace('-', ' ')
    input = input.replace(' and', '')

    list = input.split(' ')

    if 'million' in list:
        return 10 ** 6 * parse_int(' '.join(list[0:list.index('million')])) + parse_int(
            ' '.join(list[list.index('million') + 1:]))

    elif 'thousand' in list:
        return 10 ** 3 * parse_int(' '.join(list[0:list.index('thousand')])) + parse_int(
            ' '.join(list[list.index('thousand') + 1:]))

    elif 'hundred' in list:
        return 10 ** 2 * parse_int(' '.join(list[0:list.index('hundred')])) + parse_int(
            ' '.join(list[list.index('hundred') + 1:]))

    else:
        for number in list:
            if number in single_digit:
                result += single_digit[number]
            elif number in double_digit:
                result += double_digit[number]
    return result

