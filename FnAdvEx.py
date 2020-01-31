array1 = [1, 2, 3]
a1, a2, a3 = array1
print(a1, a2, a3)

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    
    return fs

#f1 = count()

def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count1()
print(f1())