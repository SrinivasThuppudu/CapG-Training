def is_palindrome(lst):
    n = len(lst)
    start, end = 0, n - 1
    while start < end:
        if lst[start] != lst[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

def main():
    print("Enter the list:", end='')
    lst = list(map(int, input().split()))
    print(is_palindrome(lst))

main()