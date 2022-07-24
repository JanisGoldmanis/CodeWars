#https://www.codewars.com/kata/54edbc7200b811e956000556/




def count_sheeps(sheep):
    """Counts how many "True" there are in an array

    :param sheep: array containing True/False
    :return: int
    """
    result = 0
    for value in sheep:
        if value == True:
            result +=1
    return result
