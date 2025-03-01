# تعریف ثوابت معادله درجه دو
a = 1
b = -3
c = 2

# محاسبه دلتا
delta = b**2 - 4 * a * c

# بررسی شرایط دلتا
if delta > 0:
    # دو ریشه حقیقی متفاوت
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)
    print(f"معادله دو ریشه حقیقی دارد: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    # یک ریشه حقیقی (دو ریشه مساوی)
    x = (-b) / (2 * a)
    print(f"معادله یک ریشه حقیقی دارد: x = {x}")
else:
    # دو ریشه مختلط
    real_part = -b / (2 * a)
    imaginary_part = (-delta)**0.5 / (2 * a)
    print(f"معادله دو ریشه مختلط دارد: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i")