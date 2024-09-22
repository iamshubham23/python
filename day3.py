# print("welcome to the rollercoaster!")
# height=int(input("what is your height in cm"))
# if height>=120:
#    print("you can ride rollercoaster")
#    age=int(input("enter your age"))
#    if age <12 :
#     bill=5
#     print("your fair is $5")
#    elif age <=18:
#       bill=7
#       print("your fair is $7")
#    elif age>45 and age<55:
#         bill=0
#         print("your fair is 0")   
#    else:
#       bill=12
#       print("your fair is $12")
#    wants_photos=input("do you want photos ? y or n")
#    if wants_photos=="y":
#       bill +=3 
#       print(f"your final bill is {bill}")
# else:
#     print("you cannot ride rollercoaster")


# num=int(input("which number do you want to check"))
# if num%2==0:
#     print("number is prime")
# else:
#     print("number is not prime")


# #Body Mass Index(BMI)
# height=float(input("enter the height of person"))
# weight=int(input("enter the weight of person"))
# BMI=weight/(height*height)
# BMI_as_int=int(BMI)
# if BMI_as_int<18.5:
#    print(f"your bmi is {BMI_as_int},they are underweight")
# elif BMI_as_int<25:
#    print(f"your bmi is {BMI_as_int},they have normal weight")
# elif BMI_as_int<30:
#    print(f"your bmi is {BMI_as_int},they are overweight")
# else:
#  print(f"your bmi is {BMI_as_int},they are obese")

#Leap Year
# year=int(input("which year do you want to check"))   
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("leap year")
#         else:
#             print("not leap year")   
#     else:
#         print("leap year")    
# else:
#     print("not leap year")

#pizza Delivery
# print("welcome to python pizzas deliveries")
# size=input("what size do you want? s,m or l")
# add_pepperoni=input("do you want pepperoni ? y or n")
# extra_cheese=input("do you want extra cheese ? y or n")
# if size == "s":
#     cost=15
#     print("your bill for pizza is 15")
# elif size=="m":
#     cost=20
#     print("your bill is for pizza 20")
# else:
#    cost=25
#    print("your bill for pizza is 25")
# if add_pepperoni=="y":
#   if size=="s":
#       cost+=2
#   else:
#       cost+=3   
# else:
#     cost=cost
# if extra_cheese=="y":
#     cost+=1
# print(f"your final bill is {cost}")    


#LOVE CALCULATOR
# print("welcome to the Love calculator")
# name1=input("what is your name:")
# name2=input("what is her name:")
# combined_string=name1+name2
# lower_case_string=combined_string.lower()
# t=lower_case_string.count("t")
# r=lower_case_string.count("r")
# u=lower_case_string.count("u")
# e=lower_case_string.count("e")
# true=t+r+u+e
# l=lower_case_string.count("l")
# o=lower_case_string.count("o")
# v=lower_case_string.count("v")
# e=lower_case_string.count("e")
# love=l+o+v+e
# love_score=int(str(true)+str(love))
# if (love_score<10) or (love_score>90):
#     print(f"your love score is {love_score},you go together like coke and mentos")
# elif(love_score>=40) and (love_score<=50):
#     print(f"your score is{love_score},you are alright together")    
# else:
#     print(f"your score is{love_score}")    

#treasure island
# print("Welcome to Treasure island.your mission is to find treasure")
# direction=input('you\'re at a crossroad,choose the direction? "left" or "right".').lower()
# if direction=="left":
#     way=input("like to wait or swim").lower()
#     if way=="wait":
#         door=input("choose one gate ?blue,red or yellow").lower()
#         if door=="yellow":
#             print("you found treasure,you win")
#         else:
#             print("game over")   
#     else:
#         print("game over")
# else:
#     print("game over")                