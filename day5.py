# fruits=["Apple", "Banana", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit+" pie")
# print(fruits)

#Average height
# students_height=input("give evrybody height").split()
# for n in range(0,len(students_height)):
#     students_height[n]=int(students_height[n])

# total_height=0
# for height in students_height:
#     total_height+=height
# print(total_height)   

# number_of_student=0
# for student in students_height:
#     number_of_student+=1

# average_height=total_height/number_of_student
# print(average_height)


#maximum scores
# student_scores=input("give the score obtanied by student").split()
# for n in range(0,len(student_scores)):
#     student_scores[n]=int(student_scores[n])
# highest_score=0
# for score in student_scores:
#     if score >highest_score:
#         highest_score=score
# print(f"the highest score among the score is{highest_score}")

#sum of 1 to 100
# total=0
# for number in range(1,101):
#     total+=number
# print(f"{total}")


#sum of even number between 1 to 100
# total=0
# #for number in range(1,101):
# for number in range(2,101,2):  #use any one for loop
#     if(number%2==0):
#        total+=number
# print(f"{total}")        

#fizzBuzz problem
# for number in range(1,101):
#     if(number%3==0 and number%5==0):
#         print("fizzbuzz")
#     elif(number %3 ==0):
#         print("Fizz")   
#     elif(number%5==0 ) :
#         print("buzz")
#     else:
#         print(f"{number}")    


#password generator
import random
letters=['a', 'b', 'c', 'd' ,'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']    
symbols=['!', '#', '$', '%', '&']

print("welcome to the password generator")
nr_letters=int(input("how many letters would you like in ur password:"))
nr_symbols=int(input(f"how many symbols would you like in ur password:"))
nr_numbers=int(input(f"how many numbers would you like:"))
#easy level
# password=""
# for char in range(0,nr_letters):
#     random_char=random.choice(letters)
#     password+=random_char
# for num in range(0,nr_numbers):
#     random_num=random.choice(numbers)
#     password+=random_num
# for symb in range(0,nr_symbols):
#     random_symb=random.choice(symbols)
#     password+=random_symb

#hard level
password_list=[]
for char in range(0,nr_letters):
    random_char=random.choice(letters)
    password_list+=random_char
for num in range(0,nr_numbers):
    random_num=random.choice(numbers)
    password_list+=random_num
for symb in range(0,nr_symbols):
    random_symb=random.choice(symbols)
    password_list+=random_symb
print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
    password+=char
print(password)