# def my_function():
#     print("Hello")
#     print("by")
# my_function()    

year=int(input("enter the year"))
if(year%400==0):
    print(f"year {year} is leap year")
elif (year%4==0 and year%100!=0):
    print(f"year {year} is leap year")
else:
    print(f"year {year} is not leap year")        