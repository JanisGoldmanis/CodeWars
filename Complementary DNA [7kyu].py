def DNA_strand(dna):
    # https://www.codewars.com/kata/554e4a2f232cdd87d9000038/
    '''
    input - string containing chars A,T,C,G
    output - chars replaced with their pair character
    A-T,C-G
    '''
    dictionary = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    result = ''
    for letter in dna:
        result+=dictionary[letter]
    return result

print(DNA_strand('ATTGC'))
