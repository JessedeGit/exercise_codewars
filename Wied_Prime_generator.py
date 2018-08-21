# Consider the sequence a(1) = 7, a(n) = a(n-1) + gcd(n, a(n-1)) for n >= 2:

# 7, 8, 9, 10, 15, 18, 19, 20, 21, 22, 33, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 69, 72, 73....

# Let us take the differences between successive elements of the sequence and get a second sequence 
# g: 1, 1, 1, 5, 3, 1, 1, 1, 1, 11, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 23, 3, 1....

# For the sake of uniformity of the lengths of sequences we add a 1 at the head of g:

# g: 1, 1, 1, 1, 5, 3, 1, 1, 1, 1, 11, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 23, 3, 1...

# Removing the 1s gives a third sequence: p: 5, 3, 11, 3, 23, 3... where you can see prime numbers.

# #Task: Write functions:

# 1: an(n) with parameter n: returns the first n terms of the series a(n) (not tested)

# 2: gn(n) with parameter n: returns the first n terms of the series g(n) (not tested)

# 3: countOnes(n) with parameter n: returns the number of 1 in g(n) 
#     (don't forget to add a `1` at the head) # (tested)

# 4: p(n) with parameter n: returns an array of n unique prime numbers (not tested)

# 5: maxp(n) with parameter n: returns the biggest prime number of the sequence pn(n) # (tested)

# 6: anOver(n) with parameter 
# n: returns an array (n terms) of the a(i)/i for every i such g(i) != 1 (not tested but interesting result)

# 7: anOverAverage(n) with parameter n: returns as an *integer* the average of anOver(n)  (tested)
# #Note: You can write directly functions 3:, 5: and 7:. There is no need to write functions 1:, 2:, 4: 6: except out of pure curiosity.

def gcd(a, b):
    small = min(a, b)
    large = max(a, b)
    if large % small == 0:
        return small
    i = int(small / 2)

    i = int(small / 2)



            return i
        else: 
            i = int(i / 2)

def an(n):
    yield 7
    i = 2
    last = 7
    while i <= n:
        curr = last + gcd(i, last)
        yield curr
        last = curr
        i += 1

def gn(n):
    firstOne = False
    # yield 1
    for v in an(n):
        if not firstOne:
            last = v
            firstOne = True
            continue
        yield v - last
        last = v

def count_ones(n):
    return sum(1 for v in gn(n) if v == 1)

def p_generator(n):
    last_value = 7
    curr_index = 2
    curr_prime_array = []
    num = 0

    while num < n:
        curr_gcd = gcd(curr_index, last_value)
        if curr_gcd != 1 and curr_gcd not in curr_prime_array:
            curr_prime_array.append(curr_gcd)
            yield curr_gcd
            num = num + 1
        last_value = curr_gcd + last_value
        curr_index = curr_index + 1
def p(n):
    return [v for v in p_generator(n)]
def max_pn(n):
    return max(p(n))

def anOver_generator(n):
    last_value = 7
    curr_index = 2
    num = 0

    while num < n:
        curr_gcd = gcd(curr_index, last_value)
        ai = curr_gcd + last_value
        if curr_gcd != 1:
            yield ai/curr_index
            num = num + 1
        last_value = curr_gcd + last_value
        curr_index = curr_index + 1

def anOver(n):
    return [v for v in anOver_generator(n)]

def an_over_average(n):
    return int(sum(anOver(n))/n)
# test
# print(list(an(100)))
# print(list(gn(100)))
# print(count_ones(100))
print(list(p_generator(5)))
print(list(p_generator(7)))
print(max_pn(5))
print(max_pn(7))
# print(anOver(5))
# print(an_over_average(11))