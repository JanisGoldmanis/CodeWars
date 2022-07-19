import string
def alphabet_position(text):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    result = []
    for letter in text:
        if letter in lowercase:
            result.append(lowercase.index(letter)+1)
        if letter in uppercase:
            result.append(uppercase.index(letter)+1)
    return ' '.join(map(str, result))

print(alphabet_position("The sunset sets at twelve o' clock."))