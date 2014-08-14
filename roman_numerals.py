import collections

# create a dictionary that relates arabic and roman numerals
# create a method that takes a number as an argument
# create an answer array
# iterate over the dictionary
# divide the number by the arabic number
# that number is how many times you push the corresponding roman numeral into the array
# update the number to the modulo of the arabic number
# repeat

arabic_to_roman = ((1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'))



def to_roman(num):
    answer = []
    ordered_arabic_to_roman = collections.OrderedDict(arabic_to_roman)
    for arabic, roman in ordered_arabic_to_roman.iteritems():
        for _ in range(num / arabic):
            answer.append(roman)
            num = num % arabic
    print ''.join(answer)


to_roman(545)
to_roman(9)
to_roman(808)











