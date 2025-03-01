from tkinter import *
import pandas
import random
BACKGROUND_COLOR="#FFFFFF"
data=pandas.read_csv("Day31/french_words.csv")
to_learn=data.to_dict(orient="records")
current_card={}

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer=window.after(5000,func=flip_card)
def flip_card():
    canvas.itemconfig(card_title,text="English")
    canvas.itemconfig(card_word,text=current_card["English"],fill="red")
    canvas.itemconfig(card_background,image=card_back_img,fill="red")
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pandas.DataFrame(to_learn)
    data.to_csv("Day31/words_to_learn.csv")
    next_card()
window=Tk()
window.title("Flashy")
flip_timer=window.after(5000, func=flip_card)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas=Canvas(width=800,height=526)
card_front_img=PhotoImage(file="Day31/backgr.png")
card_back_img=PhotoImage(file="Day31/backsec.png")
card_background=canvas.create_image(400,263,image=card_front_img)
card_title=canvas.create_text(400,150,text="text",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
cross_image=PhotoImage(file="Day31/wrongone.png")
unknown_button=Button(image=cross_image,command=next_card)
unknown_button.grid(row=1,column=0)
check_image=PhotoImage(file="Day31/rightone.png")
known_button=Button(image=check_image,command=is_known)
known_button.grid(row=1,column=1)

next_card()
window.mainloop()