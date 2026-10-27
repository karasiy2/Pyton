A = ["яблоко", "груша", "слива", "киви", "банан"]

shortest = min(A, key=len)
longest = max(A, key=len)

print(f"Самая короткая строка: '{shortest}' (длина {len(shortest)})")
print(f"Самая длинная строка: '{longest}' (длина {len(longest)})")
