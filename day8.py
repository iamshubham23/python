# def greet():
#     print("hello")
#     print("namaste")
#     print("good morning")
# greet()

#function that alllows  for input
# def greet_with_name(name):
#     print(f"hello {name}")
#     print(f"how do you do {name}")

# greet_with_name("shubham")    

#functions with more than one input
# def greet_with(name,location):
#     print(f"my name is {name}")
#     print(f"i am from {location}")

# #greet_with("shubham","begusari")    

# #function with keyword arguments
# greet_with(location="begusari",name="shubham")

#can required for painting of walls
# import math
# def paint_calc(height,width,cover):
#     area=height*width
#     num_of_cans=math.ceil(area / cover)
#     print(f"required number of cans is {num_of_cans}")
# test_height=int(input("enter the height of the wall"))
# t_width=int(input("enter the width of wall"))
# coverage=5
# paint_calc(height=test_height,width=t_width,cover=coverage)

#prime number checker
# def prime_num(number):
#    is_prime=True
#    for i in range(2,number-1):
#      if number%i==0:
#       is_prime=False
#      if is_prime:
#        print("its a prime number")
#      else:
#        print("its not a prime number")   
      
# test_num=int(input("enter a number"))
# prime_num(number=test_num)            


#caesar cipher
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction=input("type 'encode' to encrypt,type 'decode' to decrypt:\n")
# text=input("type your message:\n").lower()
# shift=int(input("type the shift number:\n"))
#todo-1:create a function called 'encrypt' that takes the text and shift as input
#def encrpyt(plain_text,shift_amount): 
#     cipher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         new_position=position+shift_amount
#         new_letter=alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"the encoded text is {cipher_text}")
    
# #todo-2:inside the 'encrypt' function,shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted text
# encrpyt(plain_text=text,shift_amount=shift)
# def decrypt(plain_text,shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         new_position=position-shift_amount
#         new_letter=alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"the new text is:{cipher_text}")

# decrypt(plain_text=text,shift_amount=shift)    

#combine the encrypt and decrypt function into a single function into a single function callled caesar
# def caesar(start_text,shift_amount,cipher_direction):
#     end_text=" "
#     for letter in start_text:
#         postion=alphabet.index(letter)
#         if cipher_direction=="encode":
#             new_position=postion+shift_amount
#         if cipher_direction=="decode":
#             new_position=postion-shift_amount
#         new_letter=alphabet[new_position]
#         end_text+=new_letter
#     print(f"end text is:{end_text}")    
# caesar(start_text=text,shift_amount=shift,cipher_direction=direction)    

#to-do1:import and print the logo from art.py when the program starts
# from art import logo
# print(logo)
#to-do2:what happens if user enter a number space or symbol
def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
        shift_amount*=-1
    for char in start_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position+shift_amount
            end_text+=alphabet[new_position]   
        else:
            end_text+=char     
    print(f"here is the{cipher_direction}d result:{end_text}")    
#caesar(start_text=text,shift_amount=shift,cipher_direction=direction)   

#to-do4:can you figure out a way to ask the user if they want to restart the cipher program
should_continue=True
while should_continue:
    direction=input("type 'encode' to encrypt,type 'decode' to decrypt:\n")
    text=input("type your message:\n").lower()
    shift=int(input("type the shift number:\n"))
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)   
    result=input("type 'yes' if we want to continue otherwise type no to exit")
    if result=="no":
        should_continue=False
        print("good bye")