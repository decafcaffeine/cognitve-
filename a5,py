import numpy as np

print("Q1")

arr = np.array([10, 20, 30, 40, 50])

print(arr + 2)
print(arr * 3)
print(arr / 2)


print("Q2")

arr = np.array([1, 2, 3, 6, 4, 5])

print(arr[::-1])

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

a = np.bincount(x)
b = np.argmax(a)

print(b)
print(np.where(x == b))

a = np.bincount(y)
b = np.argmax(a)

print(b)
print(np.where(y == b))


print("Q3")

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print(arr[0, 1])
print(arr[2, 0])


print("Q4")

Vishi = np.linspace(10, 100, 25)

print(Vishi)
print(Vishi.ndim)
print(Vishi.shape)
print(Vishi.size)
print(Vishi.dtype)
print(Vishi.nbytes)

Vishi = Vishi.reshape(25, 1)

print(Vishi)
print(Vishi.T)


print("Q5")

ucs420_Vishi = np.array([[10, 20, 30, 40],
                         [50, 60, 70, 80],
                         [90, 15, 20, 35]])

print(np.mean(ucs420_Vishi))
print(np.median(ucs420_Vishi))
print(np.max(ucs420_Vishi))
print(np.min(ucs420_Vishi))
print(np.unique(ucs420_Vishi))

reshaped_ucs420_Vishi = ucs420_Vishi.reshape(4, 3)

print(reshaped_ucs420_Vishi)

resized_ucs420_Vishi = np.resize(ucs420_Vishi, (2, 3))

print(resized_ucs420_Vishi)
