def rot13(message):
    input = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    result = ''
    for char in message:
        if char in input:
            result+=output[input.index(char)]
        else:
            result+=char
    return result


print(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"))