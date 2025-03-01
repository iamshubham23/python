
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("Day30/a_file.txt", "w")
#     file.write("xyro")
# except KeyError as error_message:
#     print("that key does not exist")

# else:
#     content=file.read()
#     print(content)


# try:
#     # Attempt to open and read the file
#     with open('example.txt', 'r') as file:
#         content = file.read()
#         print("File content:")
#         print(content)
# except FileNotFoundError:
#     # If the file does not exist, create it and write some content
#     print("File not found. Creating a new file.")
#     with open('Day30/example.txt', 'w') as file:
#         file.write("xarvish.")
# else:
#     # This block executes if no exceptions were raised in the try block
#     print("File read successfully.")


# height=float(input("height: "))
# weight=float(input("weight:"))
# if height > 3:
#     raise ValueError("human height should not be over 3 meter")
# BMI=weight/height**2
# print(BMI)

# fruits=["Apple","Pear","Orange"]
# def make_pie(index):
#     try:
#         fruit=fruits[index]
#     except IndexError:
#         print("fruit pie")
#     else:
#         print(fruit + "pie") 

# make_pie(4)    


facebook_post=[
    {'Likes':21,'comments':2},
    {'Likes':11,'comments':2,'shares':21},
    {'Likes':31,'comments':2,'shares':12},
    {'comments':5,'shares':6},
    {'comments':2,'shares':7},
    {'Likes':21,'comments':2}

]
total_likes=0
for post in facebook_post:
    try:
        total_likes=total_likes +post['Likes']
    except KeyError:
       pass
print(total_likes)    