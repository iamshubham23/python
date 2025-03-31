# import pyqrcode
# import png
# from pyqrcode import QRCode
# from tkinter import *
# def create_qrcode():
#     s1=s.get()
#     qr=pyqrcode.create(s1)
#     qr.png("myqr.png",scale=6)
#     Label(window,text="QR code is created succesfully").pack()

# window=Tk()
# window.config(width=400,height=400)

# window.title("QRCode generator")
# window.config(padx=50,pady=50)
# my_label=Label(text="Enter text to generate QR code",font=("Arial",15)).pack()
# # my_label.pack(expand=True)
# # my_label["text"]="I am RAVI from cse(AI)"
# # my_label.config(text="I am RAVI from cse(Ai) branch")
# # canvas=Canvas(width=300,height=414)
# s=Entry(window,width=50)
# s.pack(pady=10)
# Button(window,text="generate QR Code",command=create_qrcode).pack(pady=10)




# window.mainloop()




# import qrcode as qr
# img=qr.make("Hii i am Ravi Raushan i need urgent money,"
# "my father is bihar Daroga")
# img.save("RAVI")



# import qrcode
# from PIL import Image

# qr=qrcode.QRCode(version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_H,
#                 box_size=10,border=4,)
# qr.add_data("Hii i am Ravi")
# qr.make(fit=True)




from flask import Flask,render_template, request
import qrcode
from io import BytesIO
from base64 import b64encode

import qrcode.constants
qr=qrcode.QRCode(
    version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/' ,methods=['POST'])
def generateQR():
    memory=BytesIO()
    data=request.form.get('link')
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill='black',back_color='white')
    img.save(memory)
    memory.seek(0)


    base64_img="data:image/png;base64," + b64encode(memory.getvalue()).decode('ascii')
    
    return render_template('index.html',data=base64_img)
if __name__=='__main__':
    app.run(debug=True)

