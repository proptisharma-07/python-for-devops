# #Write a program that takes input for the cost price and selling price of an item   

# cost_price = float(input("Enter the cost price: "))
# selling_price = float(input("Enter the selling price: "))

# if selling_price > cost_price:

#     profit = selling_price - cost_price 
#     profit_percentage = (profit/ cost_price)*100
#     print("profit percent =  ",profit_percentage)

# elif cost_price > selling_price:

#     loss = cost_price - selling_price
#     loss_percentage = (loss/ cost_price)*100
#     print("loss percentage = " ,loss_percentage )
   

# player1 = int(input("Enter the player 1 score "))
# player2= int(input ("enter the  player 2 score "))
# player3= int(input ("enter the  player  3 score "))
# player4= int(input ("enter the  player 4 score "))
# player5 = int(input ("enter the  player 5 score "))

# total = player1 + player2 + player3 + player4 + player5
# avrage = total/5
# print(f"total run = {total}  \naverage run = {avrage}")

# age = int(input("Enter your age"))
# retirement_age = 65
# if age < retirement_age:
#     years_left = retirement_age - age 
#     print("you have",years_left, "years left until retirement. ")
# else:
#     print("you have already reached retirement age.")



# a=int(input("Enter Applicant Age :"))
# b=int(input("Enter Applicant monthly income :"))
# c=int(input("Enter applicant credit score :"))
# d=int(input("Enter applicant outstanding debt :"))
# if a>=18 and a<=60:
#     print("cleared age criterion")
#     if b>=25000:
#         print("cleared income criterion")
#         if c>=700:
#             print("cleared credit score criterion")
#             if d<=10000:
#                 print("Congratulations You are Eligible for loan")

# else:
#     print("You are not eligible for loan hence loan rejected")


# 1. Task: Calculate Profit Percentage 
# ● Write a program that takes input for the cost price and selling price of an item. 
# ● Hints 
# ○ Prompt the user to input the cost price and selling price. 
# ○ Determine whether the transaction resulted in a profit or loss. 
# ○ If there is a profit calculate the profit percentage; if there is a loss calculate the loss percentage. 
# ○ Display the profit or loss and the respective percentage

# cost_price =int(input("Enter the Cost Price -"))
# selling_price=int(input("Enter the selling price -"))
# if cost_price>selling_price:
#     loss = cost_price - selling_price
#     loss_percentage = loss/cost_price*100
#     print(f" Loss - {loss}")
#     print(f" Loss Percentage - {loss_percentage}")
# elif cost_price<selling_price:
#     profit= selling_price - cost_price
#     profit_percentage = profit/cost_price*100
#     print(f" Profit - {profit}")
#     print(f" Profit Percentage - {profit_percentage}")
# else:
#     print("No profit No Loss")


# # 19.Calculate Class Attendance Percentage

# a=int(input("Percentage of class attended by student :"))

# if a<75:
#     print("Student is not allowed to sit in examination")
# else:
#     if a>=75:
#        print("student is allowed to sit in examination")


# 2. Task: Cricket Stats Analyzer 
# ● Objective: Write a script to analyze cricket stats for a team. 
# ● Hints: 
# ○ Prompt the user to input the runs scored by each of the five players in a cricket match. 
# ○ For each player (Player 1 to Player 5) ask the user to input the runs they scored. 
# ○ Calculate the total runs scored by all players and the average runs. 
# ○ Display the total runs and average runs to the user. 

# player1 = int(input("Player1 Run Score -"))
# player2 = int(input("Player2 Run Score -"))
# player3 = int(input("Player3 Run Score -"))
# player4 = int(input("Player4 Run Score -"))
# player5 = int(input("Player5 Run Score -"))

# total_runs = player1 + player2 + player3 + player4 + player5
# avg_score = player1 + player2 + player3 + player4 + player5 / 5
# print(f"Total Runs - {total_runs}")
# print(f"Average Score - {avg_score}")

# 17.Find the greatest number.

# 17.Find the greatest number.

# a=int(input("Enter your first number :"))
# b=int(input("Enter your second number :"))
# c=int(input("Enter your third number :"))

# if a>=b and a>=c:
#     print("The greatest number is",a)
# if b>=a and b>=c:
#     print("The greatest number is ",b)
# if c>=a and c>=b:
#     print("The greatest number is",c)        

# print("congratulation your greatest number is found")


# 16.Finding the Middle Number 

# a=int(input("Enter your first number :"))
# b=int(input("Enter your second number :"))
# c=int(input("Enter your Third number :"))
      
# print(f"The three numbers are {a} {b} {c}")

# if (a>=b and a<=c) or (a<=b and a>=c )  :
#     print("Middle number is",a)
# elif  (b>=a and b<=c) or (b<=a and b>=c) :
#     print("Middle number is",b)
# else:
#     print("Middle number is ",c)
 

# print("Congratulations You have found your middle number")  

# 13. Library Charge Calculation 

# a=int(input(" Enter the number of days the book has been borrowed :"))

# if a<=5:
#     print("The charges on the book is 2rupees per day")
# elif 6<=a<=10:
#     print("The charges on the book is 3rupees per day")  
# elif 11<=a<=15:
#     print("The charges on the book is 4rupees per day")      
# elif a>=15:
#     print("The charges on the book is 5rupees per day")    

# print("-------") 

# 22. Menu-Driven Login System 

# a=int(input("Ask the user to Enter their Phone number :"))
# b=int(input("Ask the user to Enter their OTP :"))

# if a==1234567890 and b==1234:
#     print("Login Successful with Phone ")
# else:    
#     print("OOPS, Invalid credentials")

# c=(input("Enter your Email :"))
# d=(input("Enter your Email password :"))

# if c=="user@example.com" and d=="password123":
#     print("Login Successful with Email ")

# else:    
#     print("OOPS, Invalid credentials")

# user=input("exit the program :")
# if user=="yes":
#       print("Existing the Program,Have a nice day") 

# 3. Task: Retirement Age Calculator 
# ● Objective: Write a program that prompts the user for their age and tells them how many years until they reach retirement age (65). 
# ● Hints: 
# ○ Ask the user to input their age. 
# ○ Calculate how many more years they have until they reach 65 years of age. 
# ○ Display the number of years left until retirement or a message if the user has already reached retirement age.

# age = int(input("Enter Your Age - "))
# if age < 65:
#     year_left = 65 - age
#     print(f" you have {year_left} years left until Retirement")
# else:
#     print("You has already reached retirement age"

# 5. Task: Salary Calculation 
# ● Objective: You have to calculate an employee's salary by computing the gross salary tax and net salary based on the given parameters. 
# ● Hints: 
# ○ Base Salary = ₹50000 
# ○ Bonus = ₹5000 
# ○ Tax Rate = 10%  
# ○ Other Charges = ₹2000 Display the Gross Salary Tax and Net Salary. 
#base_salary = 50000
# sal=int(input("Enter your salary: "))
# bonus=int(input("Enter your bonus: "))
# other_ch=int(input("Enter other charges: "))
# tax_r=10
# gross_sal=sal+bonus-other_ch
# income_tax=(gross_sal*tax_r)/100
# net_sal=gross_sal-income_tax
# print(f"""Gross Salary Tax = {income_tax}
# Net Salary = {net_sal}""")


# 15. Tax Calculation for Car Purchase 

# 15. Tax Calculation for Car Purchase 

# a=input("Enter the Brand of the Car :") 
# b=int(input("Enter the price of the car in lakhs :"))

# if b>=7 and b<10:
#     tax_percentage=5
#     tax=(b*tax_percentage)/100
#     print(f"The calculated tax on this {a} in lakhs is {tax}")

# if b>=10 and b<15:
#     tax_percentage=10
#     tax=(b*tax_percentage)/100
#     print(f"The calculated tax on this {a} in lakhs is {tax} ")

# if  b>=15 and b<20:
#     tax_percentage=25
#     tax=(b*tax_percentage)/100
#     print(f"The calculated tax on this {a} in lakhs is {tax}")

# if b>=20 and b<25:
#     tax_percentage= 30
#     tax=(b*tax_percentage)/100
#     print(f"The calculated tax on this {a} in lakhs is {tax}")   

# print("Congratulations for your new car")    

# print("🚗")


# # 7. Task: Students Interview Eligibility Checker 

# a=int(input("Enter The Academic score of a Student :"))
# b=int(input("Enter The Attendence percentage of a Student :"))
# c=input("Enter whether the student has participated in Extra Curriculam activities :")
# if a>=60 and b>=75:
#     print("cleared academic criterion")
#     if c=="yes":
#         print("You are Eligible for Interview")
# else:
#     print("You are not Eligible for Interview") 


# radius =int(input("Enter Radius of the Circle - "))
# area_circle = 3.14 * radius**2
# print(f" Area of Circle - {area_circle}")


# a=int(input("Enter your age in years :"))
# if a>=21 and a<=32:
#     print("you are eligible for upsc examination")
#     b=int(input("Enter your prelims score :"))
#     if b>=150:
#         print("You are eligible for mains exam :")

#         c=int(input("Enter your mains score :"))
#         if c>=1000:
#             print("You are eligible for Interview")

#             d=int(input("Enter your interview marks :"))
#             if d>=300:
#                 print("Congratulations, You have cleared the UPSC examination")
        
#             else:
#                 print("Sorry, you just missed the chance")

#         else:
#             print("You failed in your mains examination")    
#     else:
#         print("Sorry, you are failed in prelims")
# else:
#     print("You are not eligible for upsc exam")



# a=input("Enter Your Email :")
# find="gmail.com"
# if (find in a) :
#     print("Email is eligible for registration based on domain ")
# else:
#     print("Email is not eligible for Registration ")