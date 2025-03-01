# import requests
# response=requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data=response.json()["iss_position"]["longitude"]
# print(data)


# from tkinter import *
# import requests
# def get_quote():
#     response=requests.get("https://api.kanye.rest")
#     response.raise_for_status()
#     data=response.json()
#     quote=data["quote"]
#     canvas.itemconfig(quote_text,text=quote)
# window=Tk()    
# window.title("Kanye Says...")
# window.config(padx=50,pady=50)
# canvas=Canvas(width=300,height=414)
# background_img=PhotoImage(file="Day33/quotes.png")
# canvas.create_image(150,207,image=background_img)
# quote_text=canvas.create_text(150,207,text="Kanye Quote goes here",width=250,font=("Arial",24,"bold"))
# canvas.grid(row=0,column=0)
# kanye_img=PhotoImage(file="Day33/kanye.png")
# kanye_button=Button(image=kanye_img,highlightthickness=0,command=get_quote)
# kanye_button.grid(row=1,column=0)

# get_quote()

# window.mainloop()



import requests
from datetime import datetime
MY_LAT=26.

MY_LONG=78.962883
parameters={
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted":0
}
response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
sunrise=data["results"]["sunrise"]
sunset=data["results"]["sunset"]
print(f"sunrise :{sunrise.split("T")[1].split(":")[0]}")
print(f"sunset:{sunset.split("T")[1].split(":")[0]}")
time_now=datetime.now()
print(time_now.hour)