import numpy as np
def f(x):
  return  0.5 * np.cos(2 * x) + np.sin(x)

a = 0 # کران پایین
b = 3 # کران بالا
n = 1000000 # تعداد مستطیل ها
total = 0

dx = (b - a) / n

for i in range(n):
  x = a + i * dx
  total += f(x) * dx

print(total)