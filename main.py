# coding for bonus calaculation
a = int(input("enter you salary "))
b = int(input(" enter your service period "))
if (b>= 5 and b<=20):
 print(a*b*5/100)
else:
 print("your are not eligible for bonus ")

a = int(input("enter you age "))

#voting eligibility
if (a>=17  and a<=100):
  print("your are eligiable for votingour are e")
else:
 print("your are not eligible for voting ")

# even odd number
even =int(input("enter your even number"))
if even%2 == 0:
  print("your number is even")
else:
  print("your number is odd")

# divisible by 7
divisible =int(input("enter your number"))
if divisible%7 == 0:
  print("your number is divisible by 7")
else:
  print("your number is not divisible by 7")

hello = "hello"
print(hello*5,sep="\n")

num=45465656
num1=num%10
print(num1)


tax = 0
pr= int(input("enter your bike price"))
if pr>= 150000:
  print(20/100*pr)
elif pr>=100000 and pr<=150000:
  print(15/100*pr)
elif pr>=50000 and pr<=100000:
  print(10/100*pr)