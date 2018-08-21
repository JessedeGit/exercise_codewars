# Welcome to the Challenge Edition of Upside-Down Numbers
# In the original kata by @KenKamau you were limited to integers below 2^17. Here, you will be given strings of digits of up to 42 characters in length (upper bound is 10^42 - 1).

# Your task is essentially the same, but an additional challenge is creating a fast, efficient solution.

# Input:
# Your function will receive two strings, each comprised of digits representing a positive integer.

# Output:
# Your function must return the number of valid upside down numbers within the range between the two numbers, inclusive.

# What is an Upside-Down Number?
# An upside down number is an integer that appears the same when rotated 180 degrees, as illustrated below.

# 1961 - OK, 88 - OK, 101 - OK, 25 - No

# Example:

# x = '0'
# y = '25'
# upsidedown(x,y) #4
# # the valid numbers in the range are 0, 1, 8, and 11
# Additional Notes:
# All inputs will be valid.
# The first argument will always be less than the second argument (ie. the range will always be valid).
# If you enjoyed this kata, be sure to check out my other katas.
import pdb

def upsidedown(x, y):
    min = get_min(x)
    return min

def mirro_all_from_i(res, i, lx):
    while i < lx:
        res[i] = res[lx - 1 - i]
        if res[i] == 9: res[i] = 6
        elif res[i] == 6: res[i] = 9
        i += 1
def backupdigit(i, res, lx):
    i = i - 1
    if i == lx - 1 - i:
        if res[i] == 0: res[i] = 1; i += 1; mirro_all_from_i(res, i, lx); return
        elif res[i] == 1: res[i] = 8; i += 1; mirro_all_from_i(res, i, lx); return
        elif res[i] == 8: res[i] = 0; i -= 1;
    cp = lx - 1 - i
    while i > -1:
        # pdb.set_trace()
        if   res[i] == 9: res[i] = 0; res[cp] = 0; i -= 1; cp = lx - 1 - i; continue
        elif res[i] == 8: res[i] = 9; res[cp] = 6; break
        elif res[i] >= 6: res[i] = 8; res[cp] = 8; break
        elif res[i] >= 1: res[i] = 6; res[cp] = 9; break
        elif res[i] >= 0: res[i] = 1; res[cp] = 1; break
    else:
        return [1] + [0] * (lx - 1) + [1]
def lowupdigit(res, i, lx, x):
    cp = lx - 1 - i
    while i > (lx - 1)//2: 
        if res[i] > int(x[i]) : break
        else: i = i - 1
    else:
        return backupdigit(i+1, res, lx)

def copy_to_right_end(res, i, lx):
    cp = lx - i - 1
    while i < lx:
        if res[cp] in (0, 1, 8): res[i] = res[cp]
        elif res[cp] == 9: res[i] = 6
        elif res[cp] == 6: res[i] = 9
        i += 1; cp = lx - i - 1
def get_min(x):
    lx = len(x)
    if x == '0'            : return '0'
    if x == '1'            : return '1'
    if lx == 1 and x <= '8': return '8'
    if lx == 1             : return '11'
    #===================================
    res = list(map(int, x))
    # step 1
    i = 0
    s1_status = 'ok'; 
    while i <= (lx - 1)//2:
        cv = res[i]
        if i == lx//2 and lx % 2:# middle digit
            if cv in (0, 1, 8)    :             s1_status = 'ok'           ; break
            if cv in (2,3,4,5,6,7): res[i] = 8; i += 1; s1_status = 'mirro_all_from_i'; break
            else                  : res[i] = 0; s1_status = 'up_digit_back'; break                 

        if cv in (2,3,4,5,7):
            res[i] = 8 if cv == 7 else 6
            i += 1
            j = i
            while i < lx - j: res[i] = 0; i += 1
            s1_status = 'mirro_all_from_i'; break

        if i == (lx - 1)//2: break # cv must in (1,6,8,9,0)
        i += 1
    # step 2
    # import pdb; pdb.set_trace()
    if s1_status == 'mirro_all_from_i': mirro_all_from_i(res, i, lx)
    elif s1_status == 'ok': 
        i = (lx - 1)//2 + 1
        while i < lx:
            cp = lx - i - 1
            if res[cp]  in (0, 1, 8) and res[i] < res[cp]:
                res[i] = res[cp]
                i = i + 1; cp = lx - i - 1
                mirro_all_from_i(res, i, lx)
                break
            elif res[cp] in (0, 1, 8) and res[i] == res[cp]:
                i = i + 1; cp = lx - i - 1
                continue
            elif res[cp] in (0, 1, 8) and res[i] > res[cp]:
                res[i] = res[cp]
                back = lowupdigit(res, i - 1, lx, x)
                if back: res = back 
                else: copy_to_right_end(res, i, lx)
                # i = cp + 1
                # j = i
                # while i < lx - j: 
                #     res[i] = 0; i += 1
                break
            elif res[cp] == 6 and res[i] < 9:
                res[i] = 9
                i = i + 1
                copy_to_right_end(res, i, lx)
                break
            elif res[cp] == 6 and res[i] == 9: 
                i = i + 1; continue
            elif res[cp] == 9 and res[i] < 6:
                # pdb.set_trace()
                res[i] = 6; i = i + 1
                copy_to_right_end(res, i, lx)
                break
            elif res[cp] == 9 and res[i] == 6: 
                i = i + 1; cp = lx - i - 1
                continue
            elif res[cp] == 9 and res[i] > 6:
                res[i] = 6
                back = lowupdigit(res, i - 1, lx, x)
                if back: res = back 
                # back = backupdigit(cp, res, lx)
                else: copy_to_right_end(res, i, lx)
                # i = cp
                # j = i
                # while i < lx - j: 
                #     res[i] = 0; i += 1
                break
    elif s1_status == 'up_digit_back':
        # pdb.set_trace()
        back = backupdigit(i, res, lx)
        if back: res = back
        else: copy_to_right_end(res, i, lx)
    return ''.join(list(map(str, res)))

# test 
lastv = -1
count = 0
for i in range(100000000,1000000000):
    cv = upsidedown(str(i), '100')
    if lastv != cv: 
        print(i,':', cv)
        count = count + 1
    # print(cv)
    lastv = cv
print(count)