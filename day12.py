# game_level=3

# enemies=["skeleton","zombies","aliens"]
# if game_level<5:
#     new_enemy=enemies[0]
# print(new_enemy)    

#modifying global scope
# enemies=1 
# def increase_enemies():
#     print(f"enemies inside function:{enemies}")
#     return enemies+1
# enemies=increase_enemies()
# print(f"enemies outside function:{enemies}")    
       
#guessing the number
# from random import randint
# print("welcome to the gueesing number game!")
# print("I'm thiinking of a number between 1 to 100")
# level=input("choose a difficulty level.type hard or easy:")
# #answer=randint(1,100)
# if level=="easy":
#     attempts=10
#     def easy_level():
#         guessed_num=45
#         while attempts!=0:
#             print(f"you have {attempts} remaining guess the number")
#             guess_num=int(input("guess a number"))
#             if guess_num==guessed_num:
#                 print(f"you got it and number is {guess_num}")
#             elif guess_num>guessed_num:
#                 print("too high")    
#             else:
#                 print("too low")    
#             return attempts-1
#     attempts=easy_level()
