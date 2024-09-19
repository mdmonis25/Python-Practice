# Factorial of a number
fact = 1
n = int(input("Enter your number: "))
if n == 0:
    fact = 1
else:
    for i in range(1,n+1):
        fact = fact*i
print(fact)        