#Write a python code to print comma seperated fibinacci numbers(1,1,2,3,5,8,11)(Take limit from user)
nterms = int(input("How many terms you want? "))

n1 = 0
n2 = 1
count = 2

if nterms <= 0:
   print("Plese enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence:")
   print(n1)
else:
   print("Fibonacci sequence:")
   print(n1,",",n2,end=', ')
   while count < nterms:
       nth = n1 + n2
       print(nth,end=' , ')
       n1 = n2
       n2 = nth
       count += 1

