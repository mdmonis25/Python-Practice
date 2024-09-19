# factors of a number
a = int(input("Enter your number: "))
print("Factors of these numbers are")
for i in range(1,a+1):
    if(a%i==0):
        print(i,end=" ")