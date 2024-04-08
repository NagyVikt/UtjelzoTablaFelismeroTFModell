import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy as np

#load the trained model to classify sign
from keras.models import load_model
model = load_model('traffic_signs_v6.h5')
#dictionary to label all traffic signs class.
classes = { 1:'Sebességkorlátozás (20km/h)',
           2:'Sebességkorlátozás (30km/h)',
           3:'Sebességkorlátozás (50km/h)',
           4:'Sebességkorlátozás (60km/h)',
           5:'Sebességkorlátozás (70km/h)',
           6:'Sebességkorlátozás (80km/h)',
           7:'Sebességkorlátozás Vége (80km/h)',
           8:'Sebességkorlátozás (100km/h)',
           9:'Sebességkorlátozás (120km/h)',
           10: 'Előzni tilos',
           11: '3,5 tonnánál nehezebb járművek előzése tilos',
           12: 'Elsőbbségadás kötelező kereszteződésben',
           13: 'Főútvonal',
           14: 'Adjon elsőbbséget',
           15: 'Állj, minden járműnek meg kell állnia',
           16: 'Járművek behajtása tilos',
           17: '3,5 tonnánál nehezebb járművek behajtása tilos',
           18: 'Behajtani tilos',
           19: 'Fokozott óvatosság',
           20: 'Veszélyes bal kanyar',
           21: 'Veszélyes jobb kanyar',
           22: 'Kettős kanyar',
           23: 'Buckás út',
           24: 'Csúszós út',
           25: 'Út szűkület jobbról',
           26: 'Útépítési munkálatok',
           27: 'Közlekedési lámpa',
           28: 'Gyalogosok',
           29: 'Gyermekátkelő',
           30: 'Kerékpár átkelő',
           31: 'Jeges/ havas út',
           32: 'Vadállat-átkelő',
           33: 'Sebesség- és előzési korlátozás vége',
           34: 'Jobbra kanyarodj',
           35: 'Balra kanyarodj',
           36: 'Csak egyenesen',
           37: 'Egyenesen vagy jobbra',
           38: 'Egyenesen vagy balra',
           39: 'Tarts jobbra',
           40: 'Tarts balra',
           41: 'Körforgalom',
           42: 'Előzési tilalom vége',
           43: '3,5 tonnánál nehezebb járművek előzési tilalmának vége',
           44:'Sebességkorlátozás (90km/h)'  }
#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Traffic sign classification')
top.configure(background='#CDCDCD')
label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)
def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.convert('RGB')  # Convert the image to RGB
    image = image.resize((30,30))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    prediction = model.predict([image])
    pred = np.argmax(prediction, axis=1)[0]  # Get the index of the max value
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#011638', text=sign)

def show_classify_button(file_path):
   classify_b=Button(top,text="Kép szkennelése",command=lambda: classify(file_path),padx=10,pady=5)
   classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
   classify_b.place(relx=0.79,rely=0.46)
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
       pass
upload=Button(top,text="Tölts fel egy képet",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="check traffic sign",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()