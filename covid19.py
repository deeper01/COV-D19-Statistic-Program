import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from matplotlib import style
import requests
import tkinter as tk
from tkinter import ttk
import urllib.request
import json

import pandas as pd
import numpy as np

global my_selected_country
global my_seleceted_category

LARGE_FONT = ("ComicSansMs", 25, "bold")

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)
url = "https://api.covid19api.com/total/dayone/country/"
response = requests.get(url)
json_data = pd.read_json('https://api.covid19api.com/total/dayone/country/turkey')



def onlbclick(evt):
    w=evt.widget
    index = int(w.curselection()[0])
    value= w.get(index)
    my_selected_country = ''.join(value)

    json_data = pd.read_json("https://api.covid19api.com/total/dayone/country/" + my_selected_country)
    Y = json_data.iloc[:, 8].values
   
    X = json_data.iloc[:, 11].values
    plt.bar(X, Y)
    plt.show()




def onlbclick2(evt2):
    w=evt2.widget
    index = int(w.curselection()[0])
    value= w.get(index)
    my_selected_category = ''.join(value)

    json_data = pd.read_json("https://api.covid19api.com/total/dayone/country/" + my_selected_category)
    Y = json_data.iloc[:, 9].values
   
    X = json_data.iloc[:, 11].values
    plt.bar(X, Y)
    plt.show()

class Corona(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self)
        tk.Tk.wm_title(self, "Covid19")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="***COVID19 ??STAT??ST??K UYGULAMAMIZA HO??GELD??N??Z***", fg="purple", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="GRAF??KLER", width=100,
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="TABLOLAR", width=100,
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="PASTA G??R??N??M??", width=100,
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):
    def print_me(self):
        clicked_items = lstb.curselection()
        print(clicked_items)
        for item in clicked_items:
            print(lstb.get(item))

    def print_me2(self):
        clicked_items = lstb2.curselection()
        print(clicked_items)
        for item in clicked_items:
            print(lstb2.get(item))
    
        

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="HAD?? B??R ??LKE SE?? SONRADA NE ????RENMEK ??STED??????N??!", fg="green",
                         font=("ComicSansMs", 15, "bold"))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="ANA SAYFA", width=15,
                             command=lambda: controller.show_frame(StartPage))
        button1.place(x=5, y=10)

        button2 = ttk.Button(self, text="SONRAK?? SAYFA",
                             command=lambda: controller.show_frame(PageTwo))
        button2.place(x=50, y=550)

        yaz?? = tk.Label(self, text="??lke Se??imi")
        yaz??.place(x=10, y=50)

        lstb = tk.Listbox(self, font="Calibri", selectmode="single")
        lstb.place(x=10, y=80)

        yaz??2 = tk.Label(self, text="Veri Se??imi")
        yaz??2.place(x=10, y=310)

        lstb2 = tk.Listbox(self, font="Calibri", selectmode="single")
        lstb2.place(x=10, y=330)
        lstb2.insert(0, 'Onaylanm????lar')
        lstb2.insert(1, '??l??mler')
        lstb2.insert(2, '??yile??enler')
        lstb2.insert(3, 'Aktif')
        lstb2.insert(4, 'Onaylanm????-G??nl??k')
        lstb2.insert(5, '??l??mler-G??nl??k')
        lstb2.insert(6, '??yile??en-G??nl??k')
        lstb2.insert(7, 'Aktif-G??nl??k')
      
        btnDraw = tk.Button(self, text="??iz")
        btnDraw.place(x=20, y=550)


        with open("world.json") as dosya:
            data = json.load(dosya)
        for countries in data['countries']:
            liste = ()
            liste = list(countries['Slug'])
            lstb.insert(0, liste)

        lstb.bind('<<ListboxSelect>>', onlbclick)
       
       
 
        
       
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="COVID19 UYGULAMASINA HO??GELD??N??Z", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="T??RK??YE COVID19 ??L??MLER??N??N YA??LARA G??RE DA??ILIMI", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label2 = tk.Label(self, text="Ya??lara g??re da????l??m s??rekli a????klanmad??????ndan dolay?? grafik g??ncel de??ildir.")
        label2.pack()
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        
        f=Figure(figsize=(5,5),dpi=100)
        
        
        a = f.add_axes([0,0,1,1])
        a.axis('equal')
        yas = ['10-19 Ya??', '20-29 Ya??', '50-59 Ya??', '70-79 Ya??', '80 Ya?? ve ??zeri']
        semboliksay?? = [11,22,71,440,814]
        a.pie(semboliksay??, labels = yas,autopct='%1.2f%%')
       

        

        canvas =FigureCanvasTkAgg(f,self)
       
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
       


     


app = Corona()

app.mainloop()
