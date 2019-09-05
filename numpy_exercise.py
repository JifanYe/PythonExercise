import numpy as np

'''
persontype = np.dtype({'names':['name', 'age', 'chinese', 'math', 'english'], 'formats':['S32','i', 'i', 'i', 'f']})
peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5),("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],dtype=persontype)
ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
print(peoples)
# print(peoples.dtype)
print(peoples.size)
print(peoples.shape)


print(ages)
print(chineses)
print(maths)
print(englishs) 

d=np.arange(0,9)
e=d[::-1]

print(np.dot(d,e))

a = np.arange(1,5).reshape(2,2)
b = np.arange(5,9).reshape(2,2)
print(np.dot(a,b))
print(np.dot(b,a))

x = np.linspace(0,2*np.pi,21) 
y = np.sin(x)
print(x)
print(y)

print(type(peoples))
print(peoples.dtype)
print(peoples.itemsize)
print(peoples.nbytes)
print(peoples.ndim)
'''

a = np.arange(10)**3
b = a[ : :1]
print(b)

x = np.floor(10*np.random.random((3,4)))
print(x)

y = x.view()
y is x

# fix bug