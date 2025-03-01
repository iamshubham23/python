# import smtplib

# my_email="adhira720@gmail.com"
# password="qmyvtwzvefgayuyd"
# connection=smtplib.SMTP("smtp.gmail.com",587)
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,
# to_addrs="shubham880999@gmail.com",
# msg="subject:Hello\n\nThis is the body of the email"
# )
# connection.close()


# import datetime as dt
# now= dt.datetime.now()
# year=now.year
# month=now.month
# day_of_week=now.weekday()
# print(day_of_week)

# date_of_birth=dt.datetime(year=2005,month=1,day=23)
# print(date_of_birth)


# import smtplib
# import datetime as dt
# import random
# my_email="adhira720@gmail.com"
# password="qmyvtwzvefgayuyd"
# now= dt.datetime.now()
# weekday=now.weekday()
# name="shubham kumar"
# if weekday == 1:
#     with open("Day32/quotes.txt","r",encoding='utf-8') as quote_file:
#         all_quotes=quote_file.readlines()
#         quote=random.choice(all_quotes)


#     with smtplib.SMTP("smtp.gmail.com",587) as connection:
#         connection.starttls()
#         connection.login(my_email,password)
#         connection.sendmail(
#             from_addr=my_email,to_addrs="shubham880999@gmail.com",msg=f"subject:Hii i am {quote}"
#         )
        


import pandas
from datetime import datetime
import random
import smtplib
import os
my_email="adhira720@gmail.com"
password="qmyvtwzvefgayuyd"
current_datetime=datetime.now()
current_date=current_datetime.day
current_month=current_datetime.month
today=(current_month,current_date)
data=pandas.read_csv("Day32/birthdays.csv")
birthdays_dict={(data_row["month"],data_row["day"]):data_row for(index,data_row) in data.iterrows()}
if today in birthdays_dict:
    birthday_person=birthdays_dict[today]
    file_path="Day32/birthday-wisher2.txt"
    if os.path.exists(file_path):
        with open(file_path) as letter_file:
            contents=letter_file.read()
            contents=contents.replace("[NAME]",birthday_person["name"])
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )
    else:
        print(f"file {file_path} does not exist")
else:
    print("No birthdays today")        