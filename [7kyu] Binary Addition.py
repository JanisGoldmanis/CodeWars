# https://www.codewars.com/kata/551f37452ff852b7bd000139

def add_binary(a,b):
    return bin(a+b).replace('0b','')





print(add_binary(1,1))
print('Has to be 10')
print(add_binary(5,9))
print('Has to be 1110')
print(add_binary(0,1))
print('Has to be 1')