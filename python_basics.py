# 1️⃣ Checking if a number is even or odd
num = int(input("Enter a number: "))
if num == 0:
    print(num,"is neither even nor Odd")
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# 2️⃣ Finding the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c : 
    print(a,"is largest number")
elif b > a and b > c :
    print(b,"is largest number")
else : 
    print(c,"is largest number")

# 3️⃣ Checking if a year is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

# 4️⃣ Checking if a number is positive, negative or zero
num = float(input("Enter a number: "))
if num > 0:
    print(num, "is Positive")
elif num < 0:
    print(num, "is Negative")
else:
    print(num, "is Zero")

# 5️⃣ Checking if the number is divisible by 2 
A = int(input("Enter a number :"))
if A % 2 == 0 and A % 5 ==0 :  
    print( A ,"is divisible by 2 and 5")
else : 
    print( A ,"is not divisible by 2 and 5")
