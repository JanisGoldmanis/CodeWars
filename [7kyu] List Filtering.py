#https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

def filter_list(l):
    result = []
    for value in l:
        if type(value)== int or type(value)==float:
            result.append(value)
    return result

# Should learn list comprehension
# Easier to compare, which values are not str