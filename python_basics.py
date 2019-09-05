def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
 
f = fib(3)

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)


e = [x * x for x in range(1, 11)]
for i in e:
    print(i)