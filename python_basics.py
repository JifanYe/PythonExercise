'''
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
'''

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    
    return fs
temp = 0
#f1 = count()
f1, f2, f3 = count()
a1, a2, a3 = [1, 3, 5]

print(f1)
print(f2)
print(f3)
