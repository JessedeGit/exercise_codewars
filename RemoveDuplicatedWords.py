s = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

list = s.split()
i = 0
output = []
while len(list):
    output.insert(i, list[0])
    while output[i] in list:
        list.remove(output[i])
    i += 1
    
print(' '.join(output))
