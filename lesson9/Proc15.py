def shift_left3(a, b, c):
    return b, c, a

set1 = (1, 2, 3)
set2 = (10, 20, 30)

print(f"Набор 1 {set1} - после сдвига:", shift_left3(*set1))
print(f"Набор 2 {set2} - после сдвига:", shift_left3(*set2))
