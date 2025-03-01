import matplotlib.pyplot as plt
import numpy as np

v = 10
t1 = 5  # زمان توقف اول
t2 = 10  # زمان توقف دوم

time = np.linspace(0,20,num=200)  # زمان از ۰ تا ۲۰ ثانیه با گام‌های ۰٫۱ ثانیه
V = []
X = []
x = 0  # موقعیت اولیه

for t in time:
    if t < t1:
        v_current = v  # حرکت با سرعت ثابت
    elif t < t2:
        v_current = 0  # توقف
    else:
        v_current = v*2  # حرکت دوباره با سرعت ثابت
    V.append(v_current)
    x += v_current * 0.1  # محاسبه موقعیت
    X.append(x)


# رسم نمودار مکان-زمان
plt.plot(time, X, marker='o', linestyle='-', color='red')
plt.title('X_T')
plt.xlabel('T')
plt.ylabel('X')
plt.grid(True)

plt.tight_layout()
plt.show()