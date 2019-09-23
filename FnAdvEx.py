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
f1, f2, f3 = count()
