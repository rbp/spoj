#!/usr/bin/env python3
# http://www.spoj.com/problems/PALIN/

# TODO:
# - all in one function (including import)
# - switch from while to for?

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

    # FIXME: *strictly* larger than k! We need to start one above.#
    # -> we can do this by starting w/ carry=True (and have it as a function argument)
    
    len_digits = len(digits)
    # First pass goes up to midpoint, inclusive.
    midpoint = (len_digits // 2) - 1 if len_digits % 2 == 0 else len_digits // 2
    i = 0
    carry = False
    while i <= midpoint:
        i_front, i_back = i, -(i+1)
        if carry:
            digits[i_back] = plus_one[digits[i_back]]
            carry = False
            
        if digits[i_back] == "10":
            # TODO: Merge this and previous if
            digits[i_back] = digits[i_front][-1]
            carry = True

        front, back = digits[i_front], digits[i_back]

        if back == front:
            i += 1
            continue
        if back > front:
            # Comparing as strings (since by now both are 1-character strings).
            # Thanks, ascii :)
            carry = True
        back = digits[i_back] = front

        # This needs to be correctly updated for the below to work :)
        i += 1

    if not carry:
        # We've reached the midpoint and there's nothing to carry. Done!
        return "".join(digits)

    # Picking where we left off, carrying over while needed
    while carry and i < len_digits:
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
        len_digits += 1

    if carry:
        return "1{}1".format("0"*(len(digits)-1))

    # DEBUG
    assert is_palindrome(digits)

    return "".join(digits)

def main():    
    import sys
    t = sys.stdin.readline()
    for i in xrange(n):
        print(find_palindrome(sys.stdin.readline()))

if __name__ == '__main__':
    main()



# DEBUG

def is_palindrome(digits):
    # i is an iterable (string or list)
    for i in range(len(digits) // 2):
        if digits[i] != digits[-(i+1)]:
            return False
    return True

def test():
    for i in range(1000000):
        find_palindrome(str(i))


