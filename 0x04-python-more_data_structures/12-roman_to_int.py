#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string:
        return None

    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "l": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }

    for i in range(len(roman_string)):

        current = values[roman_string[i]]

        if i < len(roman_string) - 1:
            next = values[roman_string[i+1]]

            if current < next:
                result -= current

            else:
                result += current

    return result
