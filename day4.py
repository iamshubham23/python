# import random
# random_integer=random.randint(1,10)
# print(random_integer)
# random_float=random.random()*5
# print(random_float)

# import random
# test_seed=int(input("create a seed number"))
# random.seed(test_seed)
# random_side=random.randint(0,1)
# if random_side==1:
#     print("Heads")
# else:
#     print("Tails")    


#List
# states_of_india=["Bihar","uttrakhend","delhi","jharkhand"]
# #print(states_of_india[-1])
# states_of_india[1]="uttrakhand"
# #print(states_of_india[1])
# states_of_india.append("jammu")
# print(states_of_india)


#you are going to write a program which will select a random name from a list of names.the person selected will have to pay everybody's bill
import random
test_seed=int(input("create a seed number:"))
random.seed(test_seed)
namesAsCSV=input("give me everybodys name,separated by comma")
names=namesAsCSV.split(", ")
num_items=len(names)
random_choice=random.randint(0,num_items - 1)
person_who_will_pay=names[random_choice]
print(person_who_will_pay+" is going to buy the meal")


#WAP for selection of random food out of some food
# import random
# test_seed=int(input("give seed number"))
# random.seed(test_seed)
# menu_item=input("give the option of food separated by commas:")
# menu=menu_item.split(", ")
# menus_items=len(menu)
# random_choice=random.randint(0,menus_items -1)
# food_selected=menu[random_choice]
# print("the food selected is "+food_selected)


#treasure
# row1=[" "," "," "]
# row2=[" "," "," "]
# row3=[" "," "," "]
# map=[row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position=input("where do you want to put treasure")#first number for column and second for row
# horizontal=int(position[0])
# vertical=int(position[1])
# map[vertical-1][horizontal-1] = "x"
# print(f"{row1}\n{row2}\n{row3}")



#Rock,Paper,Scissor Game
# import random
# user_choice=int(input("what do you choose? Type 0 for rock,1 for paper,2 for scissors:"))
# computer_choice=random.randint(0,2)
# print(f"computer choice{computer_choice}")
# if user_choice>2 or user_choice<0:
#     print("you typed invalid you loose")   
# elif user_choice==0 and computer_choice==2:
#     print("you win")
# elif computer_choice==0 and user_choice==2:
#     print("you loose")
# elif computer_choice >user_choice:
#     print("you loose")
# elif user_choice > computer_choice:
#     print("you win")
# elif computer_choice==user_choice:
#    print("draw")