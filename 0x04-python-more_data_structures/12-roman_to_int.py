#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
    if not isinstance(roman_string, str) or roman_string == None:
        return None
    num_sum = 0
    for i in range(len(roman_string)-1, -1, -1):
        num = roman_numerals[roman_string[i]]
        if 3 * num < num_sum:
            num_sum -= num
        else:
            num_sum += num
    return num_sum
