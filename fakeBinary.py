# Given a string of digits, you should replace any digit below 5 with '0' 
# and any digit 5 and above with '1'. Return the resulting string.


def fake_binary(s):
    return ''.join(['0' if (int(v) < 5) else '1' for v in s])


print(fake_binary('81926054'))
