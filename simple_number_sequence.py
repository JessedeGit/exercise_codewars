# In this Kata, you will be given a string of numbers in sequence and your task 
# will be to return the missing number. If there is no number missing or there is 
# an error in the sequence, return -1.

# For example:

# missing("123567") = 4 
# missing("899091939495") = 92
# missing("9899101102") = 100
# missing("599600601602") = -1 -- no number missing
# missing("8990919395") = -1 -- error in sequence. Both 92 and 94 missing.
# The sequence will always be in ascending order.

# More examples in the test cases.

# Good luck!

def divisor_generator(length):
    divisor = 1
    while divisor <= int(length / 2):
        # if not length % divisor:
        yield divisor
        divisor += 1


def missing(string):
    length = len(string)
    divisor = divisor_generator(length)

    for d in divisor:
        # print('d=', d)
        current_index = d * 2 - 1 # as 1 always the first divisor
        first2= True
        while current_index < length: # means not finish
            last = int(string[current_index - 2*d + 1:current_index - d + 1])
            if len(str(last + 1)) > d: # more digits required
                current_index = current_index + 1
                d = d + 1 
            this = int(string[current_index - d + 1:current_index + 1]) 
            diff = this - last
            # print('this', this, 'last', last, 'diff', diff)
            # at this time, if diff !=1 and diff !=2, then check if len(str(last + 1)) > d
            if diff != 1 and len(str(last + 2)) > d and len(str(last + 1)) == d:
                current_index = current_index + 1
                d = d + 1 
                this = int(string[current_index - d + 1:current_index + 1]) 
                diff = this - last
            current_index += d
            if diff == 1: continue
            if diff == 2 and first2:
                first2 = False
                res = last + 1
                continue
            else:
                break                
        else:
            # got it
            # print('when d =', d, 'I find it!')
            if not first2:
                return res 
            else:
                return -1
    return -1 # two or more missing



print(missing('810111213'))
# print(missing('99991000110002'))
# print(missing('899091939495'))
# print(missing('9899101102'))
# print(missing('599600601602'))
# print(missing('8990919395'))
