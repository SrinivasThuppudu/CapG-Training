n = int(input("Enter the size of array:"))
nums = []
res = 0
for i in range(n):
    x = int(input(f"Enter the Integer {i + 1}:"))
    nums.append(x)
    res += x

print("Array Elements:", nums)
print("Sum of Integers in array:", res)
