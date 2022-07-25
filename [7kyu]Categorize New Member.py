#https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/

def open_or_senior(data):
    result = []
    for pair in data:
        if pair[0]>=55 and pair[1]>7:
            result.append("Senior")
        else:
            result.append("Open")
    return result