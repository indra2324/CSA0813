#string to integer
a=str(input("enter a string:\n"))
result=int(a)
print("result:",result)

#remove duplicate elements
a=eval(input("enter the list:\n"))
result=set(a)
print(list(result))

#average of list of integers
a=eval(input("enter the list:\n"))
sum=0
length=len(a)
for i in a:
    sum=sum+i
average=sum/length
print("average list of integers:\n",average)

#perfect square(or)not
import math
a=int(input("enter the square of a number:\n"))
result1=math.sqrt(a)
result2=result1**2
if result2==a:
    print("perfect square")
else:
    print("not a perfect square")

#sum of all even numbers in a list
a=eval(input("enter the list:\n"))
sum=0
for i in a:
    if i%2==0:
        sum=sum+i
print(sum)


#number id divisible by 3&5
n=int(input("enter the number:\n"))
if n%3==0 or n%5==0:
    print("divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")

#vowel or consonant
a=str(input("enter the string:\n"))
vowels="aeiouAEIOU"
consonants="bcdfghjklmnprstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
if a in vowels:
    print("entered alphabet a vowel")
elif a in consonants:
    print("entered alphabet is a consonats")
else:
    print("enterd is not vowel or consonants")

import array
a=array.array('i',[1,2,3,4,5,5])
a.append(7)
print("After append:", a)
a.insert(2,6)
print("After insert:", a)
a.pop(1)
print("After pop:", a)
b=a.index(4)
print("Index of 4:",b)
a.reverse()
print("After reverse:", a)
c=a.count(5)
print(c)


