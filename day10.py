#def format_name(f_name,l_name):
#     print(f_name.title())
#     print(l_name.title())
#     formated_f_name=f_name.title()
#     formated_l_name=l_name.title()
#     print(f"{formated_f_name} {formated_l_name}")
# format_name("shubham","kumar")
# def format_name(f_name,l_name):
#    """Take a first and last name and last name and format 
#    it to return the title case veresion of the name."""
#    if f_name == "" or l_name == "":
#       return "you did not provide valid inputs"
#    formated_f_name=f_name.title()
#    formated_l_name=l_name.title()
#    return f"{formated_f_name} {formated_l_name}"
# print(format_name(input("what is your first name?"),
# input("what is your last name?")))

#days in month
# def is_leap(year):
#     if year%4==0:
#         if year%100==0:
#             if year%400==0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# def days_in_month(year,month):
#     month_days=[31,28,31,30,31,30,31,31,30,31,30,31] 
#     if is_leap(year) and month==2:
#         return 29
#     return month_days[month-1]   

# year=int(input("enter a year:"))
# month=int(input("enter a month"))
# days=days_in_month(year,month)    
# print(days)

#Calculator
def add(n1,n2):
    return n1+n2
#subtract
def subtract(n1,n2):
    return n1-n2

#multiply
def multiply(n1,n2):
    return n1*n2
#divide
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():
    num1=float(input("enter n1:"))
    for symbol in operations:
        print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol=input("pick an operation from above")
        num2=float(input("enter n2:"))
        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input("type 'y' to continue calculating with {answer},or n to start a new calculator:")=="y":
            num1=answer
        else:
            should_continue=False    
            calculator()
            
calculator()