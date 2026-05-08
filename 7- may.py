#
#
#  num1=20 
# if num1%2==0:
#     print("EVEN")
#     mob=input("Enter your number :")
#     if len(mob)=10 :
#         print("valid number")
#     else:
#         print("invalid number")
# else:
#     print("ODD")

pre=int(input("enter your pre marks "))
if pre >= 400:
    print("you are pass in pre and aligble for mains ")
    mains=int(input("enter your mains marks : "))
    if mains >= 600:
        print("you are pass in mains and eligble for interview")
    else:
        print("fail in mains ")
else:
    print("better luck next time ,pre failed ☠️  ")




