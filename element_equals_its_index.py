# Element equals its index
# Given a sorted array arr of distinct integers, 
# write a function index_equals_value that returns the lowest index i 
# for which arr[i] == i. Return -1 if there is no such index.

# Your algorithm should be very performant.

# [input] array of integers

# [output] integer

# Examples:
# input: arr = [-8,0,2,5]
# output: 2 # since arr[2] == 2

# input: arr = [-1,0,3,6]
# output: -1 # since no index in arr satisfies arr[i] == i.
# Random Tests Constraints:
# Array length: 200000 Ammount of tests: 1000

# Time limit: 1.5 s

def index_equals_value(arr):
    start, end = 0, len(arr) - 1
    while start <= end:
        if  arr[start] == start: return start
        elif arr[start] > start or arr[end] < end: return -1
        else: 
            mid = (start + end) // 2
            if arr[mid] >= mid: 
                end = mid
                continue
            elif arr[mid] < mid:
                start = mid + 1
                continue
        
    

print(index_equals_value([-3,0,1,3,10,11,12,13,15,16]))