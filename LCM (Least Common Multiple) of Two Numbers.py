def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(n, m):
    return abs(n * m) // gcd(n, m)
N = int(input("Enter first integer (N): "))
M = int(input("Enter second integer (M): "))
result = lcm(N, M)
print("LCM of", N, "and", M, "is:", result)
