#Debugging
#decribe the problem
# def my_function():
#     for i in range(1,20):
#         if i==18:
#             print("you got it")
# my_function()

#reproduce the bugs
# from random import randint
# dice_imgs=["1a","2a","3a","4a","5a","6a"]
# dice_num=randint(0,5)
# print(dice_imgs[dice_num])

#play the computer
# year=int(input("what's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("you are a millenal")
# elif year >=1994:
#     print("you are a Gen Z")

#Fix  the errors
# age=int(input("how old are you"))
# if age >18:
#     print(f"you can drive at {age}")

#print is your friend
# pages=0
# word_per_page=0
# pages=int(input("number of pages:"))
# word_per_page=int(input("number of words per page:"))
# total_words=pages*word_per_page
# print(f"pages={pages}")
# print(f"word per pages={word_per_page}")
# print(total_words)

#use a debugger
# def mutate(a_list):
#     b_list=[]
#     for item in a_list:
#         new_item=item*2
#         b_list.append(new_item)
#     print(b_list)
# mutate([1,2,3,5,8,13])

# number=int(input("which number do you want to check"))
# if number % 2==0:
#     print("this is an even number")
# else:
#     print("this is an odd number")    /

for number in range(1,101):
    if number%3==0 and number %5==0:
        print("FizzBuzz")
    elif number % 3==0:
        print("Fizz") 
    elif number %5==0:
        print("Buzz")
    else:
        print([number]  )         
