import numpy
n, m = map(int, input().split())
a = numpy.array((list(map(int, input().split())))).reshape(n, m)
b = numpy.array((list(map(int, input().split())))).reshape(n, m)
print(numpy.round(a + b).astype(int))
print(numpy.round(a - b).astype(int))
print(numpy.round(a * b).astype(int))
print(numpy.round(a / b).astype(int))
print(numpy.round(a % b).astype(int))
print(numpy.round(a ** b).astype(int))