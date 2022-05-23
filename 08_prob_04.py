from tkinter import N


def sum_r(n):
    if n == 1:
        return 1
    return sum_r(n-1) + n

s = sum_r(5)
print(s)
