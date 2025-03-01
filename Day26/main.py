# numbers=[1,2,3]
# new_numbers=[n+1 for n in numbers]
# print(new_numbers)

# range_list=[num*2 for num in range(1,5)]
# print(range_list)

# names=['vivek','ishu','saurabh','dheeraj','annand']
# #short_names=[name for name in names if len(name)<5]
# #print(short_names)
# cap_name=[name.upper() for name in names if len(name)>5]
# print(cap_name)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers=[n**2 for n in numbers]
# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result=[n for n in numbers if n%2==0]
# print(result)

# with open("Day26/file1.txt")as file1:
#     file_1_data=file1.readlines()
# with open("Day26/file2.txt")as file2:
#     file_2_data=file2.readlines() 

# result=[int(num) for num in file_1_data if num in file_2_data]
# print(result)


# import random
# names=['vivek','ishu','saurabh','dheeraj','annand']
# student_score={student:random.randint(1,100) for student in names }
# print(student_score)

# passed_student={student:score for (student,score) in student_score.items() if score >=50 }
# print(passed_student)



# sentence="what is airspeed velocity of an unladen swallon"
# result={word:len(word) for word in sentence.split()}
# print(result)

# weather_c={
# 'Monday': 53.6,
# 'Tuesday': 57.2,
# 'Wednesday': 59.0,
# 'Thursday': 57.2,
# 'Friday': 69.8,
# 'Saturday': 71.6,
# 'Sunday': 75.2,
# }
# weather_f={temp:int((temp*9/5)+32) for (day,temp) in weather_c.items()}
# print(weather_f)

# student_dict={
#     "student":["Angela","James","Lily"],
#     "score":[60,70,80]

# }
# import pandas
# student_data_frame=pandas.DataFrame(student_dict)
# print(student_data_frame)

# #Loop through a data frame
# # for (key,value) in student_data_frame.items():
# #     print(value)

# #loop through rows of a data frame
# for(index,row) in student_data_frame.iterrows():
#     print(row.score)


# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
#for (key, value) in student_dict.items():
    #Access key and value
#   pass

# import pandas
# data=pandas.read_csv("Day26/nato-phonetic-alphabet.csv")
# print(data.to_dict())
# #student_data_frame = pandas.DataFrame(student_dict)

#phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}
#print(phonetic_dict)
#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
#    pass




import pandas
data = pandas.read_csv("Day26/nato-phonetic-alphabet.csv")
phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}
print(phonetic_dict)
word=input("enter a word ").upper()
def generate_phonetic():
    try:
        output_list=[phonetic_dict[letter] for letter in word]
       
    except KeyError:
        print("sorry! enter the string")
    else:
        print(phonetic_dict)    

generate_phonetic()        
