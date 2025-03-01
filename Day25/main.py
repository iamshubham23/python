# with open("Day25/weather_data.csv") as weather_data:
#     data=weather_data.readlines()
#     print(data)

# import csv
# with open("Day25/weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#        if row[1]!="temp":
#             temperatures.append(int (row[1]))
#     print(temperatures)    

# import pandas
# data=pandas.read_csv("Day25/weather_data.csv")
#print(type(data))
#print(type(data["temp"]))
#print(data["temp"])

# data_dict=data.to_dict()
# print(data_dict)
# temp_list=data["temp"].to_list()

# average=sum(temp_list)/len(temp_list)
# print(average)

#print(data["temp"].mean())
#print(data["temp"].max())

#Get Data in columns
# print(data["condition"])
# print(data.condition)


#Get Data in row
#print(data[data.day=="Monday"])
#print(data[data.temp==data.temp.max()])
# monday=data[data.day=="Monday"]
# # print(monday.condition)
# tempr=(monday.temp)
# print((tempr*9/5)+32)


#create a Dataframe from scratch
# data_dict={
#     "students":["Any","james","jarvis"],
#     "scores":[78,80,86]
# }
# data=pandas.DataFrame(data_dict)
# #print(data)
# data.to_csv("Day25/new_data.csv")

# import pandas
# data=pandas.read_csv("Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241021.csv")
# gray_squirrel_count=len(data[data["Primary Fur Color"]=="Gray"])
# red_squirrel_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
# black_squirrel_count=len(data[data["Primary Fur Color"]=="Black"])
# print(gray_squirrel_count)

# data_dict={
#     "Fur color":["Gray","Cinnamon","Black"],
#     "Count":[gray_squirrel_count,red_squirrel_count,black_squirrel_count]
# }
# df=pandas.DataFrame(data_dict)
# df.to_csv("Day25/squirrel_count.csv")