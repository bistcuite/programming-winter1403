import matplotlib.pyplot as plt
import numpy as np

# اطلاعات حرکت
x0 = 400  # موقعیت اولیه
v0 = 5  # سرعت اولیه
a = -0.01  # شتاب
total_time = 10  # مدت زمان حرکت

# محاسبه موقعیت و سرعت در هر لحظه

t = np.linspace(0,15,num=100)  # زمان از ۰ تا ۱۰ ثانیه با گام‌های ۰٫۱ ثانیه
x = []
v = []

for i in t:
    x.append(x0 + v0 * i + 0.5 * a * i**2)

for i in t:
    v.append(v0 + a * i)

# رسم نمودار مکان-زمان
plt.plot(t, x, marker='o', linestyle='-', color='blue')
plt.title('X_T')
plt.xlabel('T')
plt.ylabel('X')
plt.show()

# نمودار سرعت-زمان
plt.plot(t, v, marker='o', linestyle='-', color='red')
plt.title('V_T')
plt.xlabel('T')
plt.ylabel('V')
plt.show()

