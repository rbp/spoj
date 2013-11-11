#!/usr/bin/env python3
# http://www.spoj.com/problems/PALIN/

def find_palindrome(k):
    # Returns the next palindrome strictly larger than k
    # k and return value are string representations
    digits = list(k)
    plus_one = {
        "0": "1",
        "1": "2",
        "2": "3",
        "3": "4",
        "4": "5",
        "5": "6",
        "6": "7",
        "7": "8",
        "8": "9",
        "9": "10"
        }

    # *strictly* larger than k
    digits[-1] = plus_one[digits[-1]]
    
    len_digits = len(digits)
    # First pass goes up to midpoint, inclusive.
    midpoint = (len_digits + 1) // 2
    carry = False
    for i in range(midpoint+1):
        i_front, i_back = i, -(i+1)
        if carry:
            digits[i_back] = plus_one[digits[i_back]]
            carry = False
            
        if digits[i_back] == "10":
            digits[i_back] = digits[i_front][-1]
            carry = True

        front, back = digits[i_front], digits[i_back]

        if back == front:
            continue
        if back > front:
            # Comparing as strings (since by now both are 1-character strings).
            # Thanks, ascii :)
            carry = True
        back = digits[i_back] = front

    if not carry:
        # We've reached the midpoint and there's nothing to carry. Done!
        return "".join(digits)

    # Picking where we left off, carrying over while needed
    for i in range(i+1, len_digits):
        # Slightly different logic from the above: We're moving from the centre backwards
        i_front, i_back = i, -(i+1)
        d = plus_one[digits[i_back]]
        if d == "10":
            # Do I need to carry from the end of the list again?
            # I don't think so! I'm already going "up" by carrying here.
            digits[i_back] = digits[i_front] = "0"
            carry = True
        else:
            digits[i_back] = digits[i_front] = d
            carry = False
        if not carry:
            break

    if carry:
        return "1{}1".format("0"*(len(digits)-1))

    return "".join(digits)

def main():    
    import sys
    from itertools import islice
    all_input = sys.stdin.readlines()
    # t = int(all_input[0])
    all_output = [find_palindrome(k.rstrip()) for k in islice(all_input, 1, None)]
    print("\n".join(all_output))

if __name__ == '__main__':
    main()



# DEBUG
def is_next_palindrome(k, digits):
    int_k = int(k)
    str_digits = "".join(digits)

    i = int_k+1
    str_i = str(i)
    while not is_palindrome(str_i):
        i += 1
        str_i = str(i)
    return str_i == str_digits

def is_palindrome(digits):
    # i is an iterable (string or list)
    for i in range(len(digits) // 2):
        if digits[i] != digits[-(i+1)]:
            return False
    return True

def test():
    for i in range(100000000000000000000000000):
        find_palindrome(str(i))


