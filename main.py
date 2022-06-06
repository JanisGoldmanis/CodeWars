def parseInt(input):
    single_digit = {'one': 1, 'two': 2, 'three': 3, ' four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    double_digit = {'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
                    'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40,
                    'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
    result = 0

    #Searching for keywords - million, thousand or hundred, order is important

    list = input.split(' ')
    if 'million' in list:
        print(list.index('million'))
        print(list)

    #sum from dictionary everything before keyword

    #everything before the keyword is multiplied by keyword multiplier

    #recursive function return result + parInt everything after keyword






parseInt('one million three hundred')
