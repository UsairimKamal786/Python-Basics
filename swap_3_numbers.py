a = int(input("Enter the first number to swap: "))
b = int(input("Enter the second number to swap: "))
c = int(input("Enter the third number to swap: "))
print("\nBefore swapping:")
print("a =", a, "b =", b, "c =", c)
temp = a
a = c
c = b
b = temp

print("\nAfter swapping:")
print("a =", a, "b =", b, "c =", c)
