from tkinter import*
from tkinter.ttk import*
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from collections import Counter
from random import choices,randint
import random
import numpy as np
import matplotlib.pyplot as plt
from time import time,sleep


Breakfast = {'Whole grain bread':69,
             'Tumeric Milk':157,
              'Soy Milk':54,
              'Honey':304,
              'Dairy Products':50,
              'Cereal':360,
              'Oat meal':150,
              'Soft Boiled Egg':72,
              'Egg white':52,
              'Yoghurt':59,
              'Sprouts':256,
              'Nuts':607,
              'Detox tea':2,
              'Coffee':1,
              'Omelette':188,
              'Pohe':250,
              'Upma':192,
              'Biscuit digestives':140,
              'Muesli':195,
              'Bacon fried':150,
              'Banana shake':190,
              'Avacodo':250
              }
Lunch = {'Rice':111,
          'Chappati':300,
          'Pulse':81,
          'Pasta':131,
          'Fish':206,
          'Meat':170,
          'Paneer':220,
          'Salad':235,
          'broccoli':31,
          'Vegetables':65,
          'Curd':98,
          'Cheese':402,
          'Soy bean':446,
          'Egg curry':156,
          'Prawns':180,
          }


Dinner = {'Curd Rice':350,
           'Fruit':75,
           'Yoghurt':59,
           'Granola':471,
           'Peanut butter':588,
           'vegetable':65,
           'Pasta':131,
           'Fish':206,
           'Meat':170,
           'Egg curry':156,
           'Prawns':180,
           'Cold Milk':150,
           'Fruit Salad':123,
           }

Snacks = {'Granola bar':471,
          'Greek Yoghurt':59,
           'Bhel':289,
          'Cottage Cheese':98,
          'Dark Chocolate':150,
          'hummus':166,
          'Hard Boiled egg':80,
          'Fruit Salad':50,
          'Pistachio bar':500,
          'Jam':38,
          'Mars bar':240,
          'Avacado':150}

x_input=[]          #x input for nn
y_input = []        #y input for nn
cal_hist =[]        #cal cache for cal calcualted by nn
cal_ga = []         #cal cache for cal calcualted by ga
np.random.seed(1)
class AIdiet:
    def __init__(self,master):
           master.geometry('450x350')
           master.title('who are you?')
           p2 = PhotoImage(file='diet.png')
           master.configure(bg='light yellow')
           master.iconphoto(False,p2)
           theme = ThemedStyle(master)
           theme.set_theme('radiance')
           name = Label(master,text='Name',borderwidth=5,relief='groove')
           email = Label(master,text='email',borderwidth=5,relief='groove')
           number = Label(master,text='Phone no.',borderwidth=5,relief='groove')
           self.n = StringVar()
           self.e = StringVar()
           self.z = StringVar()
           y_main=100
           for _ in (name,email,number):
                 _.place(x=100,y=y_main)
                 y_main+=50
           name_entry = Entry(master,textvariable=self.n)
           email_entry = Entry(master,textvariable=self.e)
           number_entry = Entry(master,textvariable=self.z)

           y_main=100
           for _ in (name_entry,email_entry,number_entry):
                     _.place(x=200,y=y_main)
                     y_main+=50
           b1 = Button(master,text='register',command=self.credentials)
           b2 = Button(master,text='proceed',command=self.go)
           y_main=250
           for _ in (b1,b2):
                _.place(x=150,y = y_main)
                y_main+=40
    def credentials(self):
           self.name = (self.n).get()
           self.email = (self.e).get()
           self.phone =(self.z).get()

    def go(self):
        if (self.n).get()=='':
                        root = tk.Toplevel(root_orig)
                        root.geometry('500x500')
                        root.title('are you dumb?')
                        root.configure(bg='light yellow')
                        p2 = PhotoImage(file='diet.png')
                        root.iconphoto(True,p2)
                        theme = ThemedStyle(root)
                        theme.set_theme("radiance")
                        Label(root,text='please fill in your credentials \n\n     at least your name!',font=('Helvetica',16)).place(x=100,y=100)
                        Button(root,text ='Go back',command = root.destroy).place(x=175,y=250)
        else:
                        root = tk.Toplevel(root_orig)
                        root.configure(bg='light yellow')
                        p2 = PhotoImage(file='diet.png')
                        root.iconphoto(True,p2)
                        root.title("what's your diet?")
                        root.geometry('1000x600')
                        theme = ThemedStyle(root)
                        #theme.set_theme("radiance")
                        Label(root,text ="Welcome {}!".format(self.name),font=('Helvetica',16)).place(x=150,y=10)


                        #ttk.Style().theme_use('clam')
                        style = Style()

                        #Style
                        style.configure('C.TButton',font=('calibri',10,'bold'),foreground='blue')
                        style.configure('J.TButton',font=('calibri',10,'bold'),foreground='green')
                        style.configure('Q.TButton',font=('calibri',10,'bold'),foreground='red')
                        style.configure('S.TButton',font=('calibri',10,'bold'),foreground='black')

                        

                        
                        #labels
                        age_label = Label(root,text='Age')
                        gender_label = Label(root,text='Gender')
                        height_label = Label(root,text='Height(m)')
                        weight_label = Label(root,text ='Weight(kg)')
                        disorder_label = Label(root,text = 'Disorder')
                        diet_label = Label(root,text = 'Diet type')
                        work_label = Label(root,text = 'Workout')

                        Breakfast_label = Label(root,text = 'Breakfast',font=('calibri',14,'bold'))
                        Lunch_label = Label(root,text = 'Lunch',font=('calibri',14,'bold'))
                        Snacks_label = Label(root,text = 'Snacks',font=('calibri',14,'bold'))
                        Dinner_label = Label(root,text = 'Dinner',font=('calibri',14,'bold'))

                        notify_label = Label(root,text = 'calculated by AI diet bot',font=('Helvetica',12,'italic'))
                        notify_label1 = Label(root,text='Drink a lot of water:6-8 glasses of water per day',font =('Helvetica',16,'bold'))
                        notify_label2 = Label(root,text='Do not drink too much of coffee or tea!',font =('Helvetica',16,'bold'))
                        notify_label3 = Label(root,text='Avoid eating too fast!',font =('Helvetica',16,'bold'))
                        notify_label4 = Label(root,text='Do not consume too much sweets!',font =('Helvetica',16,'bold'))
                        notify_label5 = Label(root,text='Reduce Smoking and alcohol intake! ',font =('Helvetica',16,'bold'))
                        notify_label6 = Label(root,text='Excercise daily!',font =('Helvetica',16,'bold'))
                        notify_label7 = Label(root,text='Have an early Dinner! 8-9 PM would do!',font =('Helvetica',16,'bold'))

                        #label_placer
                        y_label_len = 60
                        for i in (age_label,gender_label,height_label,weight_label,disorder_label,diet_label,work_label):
                              i.place(x=100,y=y_label_len)
                              y_label_len+=30

                        #food_label
                        x_food_lab=330
                        for _ in (Breakfast_label,Lunch_label,Snacks_label,Dinner_label):
                                    _.place(x=x_food_lab,y=70,width=600,height=20)
                                    x_food_lab+=150

                        #str to strvar
                        a = StringVar()#age
                        g = StringVar()#gender
                        h = StringVar()#height strvar
                        w = StringVar()#weight strvar
                        d = StringVar()#disorder strvar
                        y = StringVar()#diet strvar
                        o = StringVar()#work strvar


                        gender = ttk.Combobox(root,textvariable=g)
                        gender['values'] = ('Male','Female')

                        disorder = ttk.Combobox(root,textvariable=d)
                        disorder['values'] = ('Diabetes','Cardio-vascular','liver','kidney')


                        diet = ttk.Combobox(root,textvariable=y)
                        diet['values'] = ('Veg','Non-Veg','Vegan')

                        work = ttk.Combobox(root,textvariable=o)
                        work['values'] = ('low','medium','high')


                        #entries
                        age_entry = Entry(root,textvariable=a)
                        height_entry = Entry(root,textvariable = h)
                        weight_entry = Entry(root,textvariable = w)



                        #label_ans

                        Breakfast_Label_ans=Label(root)
                        Lunch_Label_ans = Label(root)
                        Snacks_label_ans = Label(root)
                        Dinner_Label_ans = Label(root)

                        #food_entry
                        x_food_en = 330
                        for j in (Breakfast_Label_ans,Lunch_Label_ans,Snacks_label_ans,Dinner_Label_ans):
                                    j.place(x=x_food_en,y=90,width=600,height=300)
                                    x_food_en+=140
                        #entry_placer
                        y_entry_len=60
                        for m in (age_entry,gender,height_entry,weight_entry,disorder,diet,work):
                                   m.place(x=180,y=y_entry_len,width=120,height=20)
                                   y_entry_len+=30



                        #cmds
                        find = ttk.Button(root,text = 'Find',command = Ga().find,style = 'C.TButton')
                        like = ttk.Button(root,text='Like it?',command= Nn().cache,style = 'J.TButton')
                        progress = ttk.Button(root,text='progress',command=Ga().progress,style='Q.TButton')
                        quit = ttk.Button(root,text='Quit',command=root.destroy,style='S.TButton')

                        #cmd_placer
                        y_button_len=420
                        for j in (find,like,progress,quit):
                               j.place(x=150,y=y_button_len)
                               y_button_len+=40

                        root.mainloop()


root_orig = tk.Tk()
AIdiet(root_orig)
root_orig.mainloop()
print('Thank you')

