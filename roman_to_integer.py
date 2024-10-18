numerals ={
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

def romanToInt(number):
    total = 0
    length = len(number)
    for i in range(length-1):
        if (numerals[number[i]] < numerals[number[i+1]]):
            total -= numerals[number[i]]
        else:
            total += numerals[number[i]]
        i += 1
    return total + numerals[number[-1]]

# def romanToInt(number):
#     total = 0
#     length = len(number)
#     for i, numeral in enumerate(number):
#         if i+1 < length and numerals[numeral] < numerals[number[i+1]]:
#             total -= numerals[numeral]
#         else:
#             total += numerals[numeral]
#     return total

print(romanToInt("MCMXCIV"))