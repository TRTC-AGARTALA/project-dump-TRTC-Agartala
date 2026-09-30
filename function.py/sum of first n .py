def sum_n(n):
    if n == 1 or n == 0:
        return n
    return n + sum_n(n-1)
n = int(input("enter n:"))
print(f"sum of first {n} natural number is {sum_n(n)}")