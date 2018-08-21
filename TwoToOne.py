s1, s2 = 'xyaabbbccccdefww', 'xxxxyyyyabklmopq'

# def TwoToOne():
result = ''.join(sorted(set((list(s1 + s2)))))

print(result)