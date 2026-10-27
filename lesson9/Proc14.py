def shift_right3(a, b, c):
    return c, a, b

set1 = (1, 2, 3)
set2 = (10, 20, 30)

print(f"Набор 1 {set1} - после сдвига:", shift_right3(*set1))
print(f"Набор 2 {set2} - после сдвига:", shift_right3(*set2))
