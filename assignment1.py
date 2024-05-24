# Write a program that swaps the values of two variables.

x = 40 
y = 10

x,y = y,x
print(x,y)

# Write a program that calculates the area of a rectangle given its length and width.
length = 10
width = 20 

area = (20*10)/2
print(area)

# Write a program that converts temperature from Fahrenheit to Celsius.

Farenheit = 98.6
celsius = ((Farenheit-32)*5)/9
print(celsius)

# Write a program that calculates the volume of a sphere given its radius.
import math
r = 5
r_cubed = r**3
volume = round((4*(math.pi)*r_cubed),2)/3
print(volume)

# Write a program that finds the average of three numbers.

a= 10
b= 15
c = 20
total = a+b+c
avg = total/3
print(avg)

# Write a program that determines if a number is even or odd.
num = int(input("Enter any number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

a =10
b=15
c = 20
#Write a program that finds the maximum of three numbers.
if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
else:
    print("c is largest")# Write a program that finds the maximum of three numbers.

#Write a program that determines if a year is a leap year or not.

year = int(input("enter any value "))

if (year % 400 == 0) or (year % 4 == 0) and (year %100 !=0):
    print("leap year")
else:
    print("not a leap year")
    
#Write a program that determines if a number is positive, negative, or zero.
num = float(input("Enter a number: "))
if num > 0 :
    print("positive")
elif num < 0 :
    print("negative")
else:
    print("Zero")
    
#Write a program that calculates the grade based on a given percentage.

marks = int(input("enter your marks here! "))

if marks >= 80:
    print("A+")
elif 70 < marks <= 79:
    print("A")
elif marks >=65:
    print("A-")
elif marks >=50:
    print("B")
else:
    print("F")
    
#Write a program that prints the first `n` natural numbers.
n = 10
for i in range(1,n):
    print(i)

#Write a program that calculates the factorial of a number.

n = int(input("write a number: "))
facto = 1

while n > 1:
    facto *= n
    n -= 1
print(facto)

# 13. Write a program that generates a Fibonacci sequence of length `n`.
 
term = int(input("Enter number "))

n1 = 0
n2 = 1
cnt = 0

if term<=0:
    print("invalid input")
elif term == 1:
    print(n1)
else:
    while cnt<term:
        print(n1)
        nxt=n1+n2
        n1 = n2
        n2=nxt
        cnt+=1

#14. Write a program that checks if a given number is prime or not.

num = int(input("enter a number "))

if num % 2 ==0:
    print("prime") 
else:
    print("not prime")
    
#15. Write a program that prints the multiplication table of a given number.

num = int(input("write a number: "))

for i in range(1,11):
    total = num*i
    print(f"{num}x{i}={total}")

#16 Write a program that finds the sum of all even numbers between 1 and `n`.

n = int(input("enter a number: "))

total = 0

for i in range(1,n):
    if i % 2 == 0:
        total += i
print(total)

#Write a program that reverses a given number.
    
n = int(input("enter a number: "))

rev = 0

while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10
print(rev)

# 18. Write a program that checks if a given string, is a palindrome.

word = input("Enter any string: ")
word_rev = word[::-1]
#print(word_rev)
if word == word_rev:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
    
# 19. Write a program that generates a random number and allows the user to guess it.

import random

num = random.randint(1,10)
#print(num)

guess = int(input("Enter a number of you choice between 1 to 10: "))

if num == guess:
    print("you guessed right")
else:
    print("you guessed it wrong")
     
# 20. Write a program that finds the greatest common divisor (GCD) of two numbers.
import math
a = 20
b = 8
print(math.gcd(a,b))