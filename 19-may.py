# what is function in python. 
# 1. every function has their own purpose.
# 2. function is block of instruction(code) which execute inside its own block.
# 3 . function is reusable means define one time use manytime(dry).
# 4 . function has two main part first functions defination second function calling.\
# 5 . in python by default none.

# how define function in python.
# def add():
#     add()
#     a = 20 
#     b=10 
#     c=a+b
#     print(c)

# function divide into 4 category.
# 1. take nothing return nothing.
# 2. take nothing return something.
# 3. take something return nothing.
# 4. take something return something.

# parameters(para) and arguments(args).
# posinal parameter/argument.
# default parameter.

# def add(a=0,b=0):
#     print(a+b)
# add(11,22)

#def table_print(n):
#   for i in range (1,11):
#       print(f"{n} x {i} = {n*i}")
#m=2
#table_print(m)

# def sub(a,b):
#     c=a-b
#     print(c)
# sub(50,20)


#waf to check number pass by argument is odd or even.

# def odd_even (a):
#     if a % 2==0:
#         print("Even")
#     else:
#         print("odd")
# odd_even(4)

#waf to check which number is greater and two number by user.

# def check_greater (n1,n2)
#     if n1 > n2 :
#         print(n1 ,"is greter")
#     else:
#      print(n2 ,"is greter")
#     n1=11
#     n2=22
# check_greater(n1,n2)

#Waf to check the character pass by user is vowel or consonant.

# def check_character(char):
#     if  char in "aeiou" :
#         print ("vowel")
#     else:
#         print ("consonents")
# check_character("b")        


#waf to check in number completly divide by 2 and 3 and return
#"yes number is completely devide"
#"n
# not completely divide"

# def check_divide(num):
#     if num%2==0 and num%3==0:
#         return "yes number is completely devide"
#     else:
#         return "no completely divide"
# res =check_divide(6)
# print(res)

# waf to return length of a string pass by user without using len().
# def len_string(s):
#     c=0
#     for i in s:
#         c=c+1
#         return c
# print(len_string("python"))



#waf to check number pass by argument is odd or even.

def odd_even(a):
    if a %