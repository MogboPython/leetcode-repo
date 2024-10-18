numerals ={
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}


def intToRoman(number):
    roman_dict = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_numeral = ''

    for key in roman_dict.keys():
        while number >= key:
            roman_numeral += roman_dict[key]
            number -= key

    return roman_numeral
    # return len(str(number))
    # if number > 10:


    # rem = number % 10
    # if rem == 5:
    #     return "V"
    # else:
    #     return "I" * rem
    # total = 0
    # length = len(number)
    # for i in range(length-1):
    #     if (numerals[number[i]] < numerals[number[i+1]]):
    #         total -= numerals[number[i]]
    #     else:
    #         total += numerals[number[i]]
    #     i += 1
    # return total + numerals[number[-1]]

print(intToRoman(58))