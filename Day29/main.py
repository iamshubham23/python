# from tkinter import *
# window=Tk()
# window.title("passsword manager")
# window.config(padx=20,pady=20)
# canvas=Canvas(height=200,width=200)
# logo_img=PhotoImage(file="Day29/lock.png")
# canvas.create_image(100,100,image=logo_img)
# canvas.pack()

# window.mainloop()


# #for try 
# from tkinter import *
# window=Tk()
# r=Label(bg="red",width=20,height=5)
# r.grid(row=0,column=0)
# g=Label(bg="green",width=20,height=5)
# g.grid(row=1,column=1)
# b=Label(bg="blue",width=40,height=5)
# b.grid(row=2,column=0,columnspan=2)
# window.mainloop()


from tkinter import * 
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

#password generator project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(7,8))]
    password_symbols=[choice(symbols) for _ in range(randint(2,3))]
    password_numbers=[choice(numbers) for _ in range(randint(2,4))]
    password_list=password_letters+password_numbers+password_symbols
    shuffle(password_list)
    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
#save password
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        website:{
            "email":email,
            "password":password,
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="oops",message="something is missing")
    else:
        try:
            with open("Day29/data.json","r") as data_file:
                #Reading old data
                data=json.load(data_file)
        except FileNotFoundError:
                with open("Day29/data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)      
                #Updating old data with new data
        else:        
            data.update(new_data)    
            with open("Day29/data.json","w") as data_file:
                 #saving updated data
                json.dump(data, data_file, indent=4)
        finally:        
            website_entry.delete(0,END)
            password_entry.delete(0,END)

def find_password():
    website=website_entry.get()
    try:
        with open("Day29/data.json")as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="error",message="no data file found")
    else:           
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"email:{email}\npassword:{password}")
        else:
            messagebox.showinfo(title="Error",message=f"no details for {website} exits")    
window=Tk()
window.title("password manager")
window.config(padx=50,pady=50)
canvas=Canvas(height=300,width=200)
logo_img=PhotoImage(file="Day29/lock.png")
canvas.create_image(90,90,image=logo_img)
canvas.grid(row=0,column=1)

#Labels
website_label=Label(text="Website")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/user")
email_label.grid(row=2,column=0)
password_label=Label(text="Password")
password_label.grid(row=3,column=0)

#Entries

website_entry=Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"shubham880999@gmail.com")
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)


#Buttons
generate_search_button=Button(text="Search",width=13,command=find_password)
generate_search_button.grid(row=1,column=2)
generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=35,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()


