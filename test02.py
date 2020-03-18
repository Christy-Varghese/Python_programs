def isPerfect(n):
    # To store sum of divisors
    sum = 1

    # Find all divisors and add them
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n / i
        i += 1

    # If sum of divisors is equal to
    # n, then n is a perfect number

    return (True if sum == n and n != 1 else False)


# Driver program
t = int(input("Enter the number of test :"))
for i in range(t):
    n = int(input("Enter the Values: "))
    if isPerfect(n):
        print("YES")
    else:
        print("NO")