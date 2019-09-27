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

def count1():
    def f(j):
        return j*j
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

#f1 = count()
f1, f2, f3 = count1()

print(f1)
print(f2)
print(f3)

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
	
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
	
test_calc_sum = calc_sum(1, 3, 5, 7, 9)
test_lazy_sum = lazy_sum(1, 3, 5, 7, 9)

print(test_calc_sum, test_lazy_sum())


