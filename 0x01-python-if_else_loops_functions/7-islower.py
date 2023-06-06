#!/usr/bin/python3
def islower(c):
    num_ascii = ord(c)
    if num_ascii >= 97 and num_ascii <= 122:
        return True
    return False
