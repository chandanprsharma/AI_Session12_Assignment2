# Fibonacci Series
def getFibonacci(limit):
    result = []
    i = 0
    j = 1
    result.append(i)
    result.append(j)
    while True:
        t = i + j
        if t > limit:
            break
        result.append(t)
        i = j
        j = t
    
    print(f'Fibonacci Series upto {limit}:\n', result)

