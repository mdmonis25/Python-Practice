#palindrome Number
p = int(input("Enter Number: "))
d = p
rev = 0
while p>0:
    rev = rev*10 + p%10
    p //=10

if d == rev:
    print(f'{d} is a paindrome number.')
else :
    print(f'{d} is not a paindrome number.')
               