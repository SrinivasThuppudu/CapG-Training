def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def primes(low, high):
    nums = []
    for i in range(low, high + 1):
        if is_prime(i):
            nums.append(i)
    return nums

def smallest_largest_prime(nums):
    smallest = nums[0]
    largest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
    return smallest, largest

def main():
    while True:
        low = int(input("Enter lower bound: "))
        high = int(input("Enter upper bound: "))
        if low >= 0 and high >= 0 and low < high:
            break

    prime_numbers = primes(low, high)
    if not prime_numbers:
        print("No prime numbers found in the range.")
    else:
        smallest, largest = smallest_largest_prime(prime_numbers)
        print(f"Prime numbers between {low} and {high} are:", prime_numbers)
        print(f"Smallest prime: {smallest}\nLargest prime: {largest}")

main()