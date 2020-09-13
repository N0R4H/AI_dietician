from tkinter import*
from tkinter.ttk import*
import tkinter as tk
from tkinter import ttk
from collections import Counter
from random import choices,randint
import random

#diets
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
              'Nuts(almonds,walnuts,apricots,figs)':607,
              'Detox tea':2,
              'Coffee':1,
              'Omlete':188,
              'Pohe':250,
              'Upma':192}
Lunch = {'Rice':111,
          'Chappati':300,
          'Pulse':81,
          'Pasta':131,
          'Fish':206,
          'Meat':170,
          'Paneer':220,
          'Salad':235,
          'cruciferous vegetable':31,
          'Vegetables':65,
          'Curd':98,
          'Cheese':402,
          'Soy bean':446,
          'Egg curry':156}


Dinner = {'Curd Rice':350,
           'Fruit':75,
           'Yoghurt':59,
           'Granola':471,
           'Peanut butter':588,
           'vegetable':65,
           'Pasta':131,
           'Cold Milk':150,
           'Fruit Salad':123,
           }

Snacks = {'Granola bar':471,
          'Greek Yoghurt':59,
           'Bhel':289,
          'Cottage Cheese':98,
          'Dark Chocolate with Almond':150,
          'hummus':166,
          'Hard Boiled egg':80,
          'Fruit Salad':50,
          'Pistachio bar':500,
              }


root = tk.Tk()
root.title("what's your diet?")
root.geometry('450x500')
#root.configure(bg='white')
style = Style()

#Style
style.configure('C.TButton',font=('calibri',10,'bold'),foreground='red')
style.configure('Q.TButton',font=('calibri',10,'bold'),foreground='green')

#incon
p1 = PhotoImage(file='diet.png')
root.iconphoto(True,p1)

def bmi():
      height = float(h.get())
      weight = float(w.get())
      age =  int(a.get())
      gender = g.get()
      disorder = d.get()
      #work = o.get()
      #diet = y.get()
      BMI = weight/(height)**2
      if BMI<18.5:
           cal = int(BMI*random.randint(140,190))
           BMI_label_ans.config(text = str(round(BMI,2))+' (Underweight)')
      elif 18.5<BMI<22.9:
           cal = int(BMI*random.randint(120,160))
           BMI_label_ans.config(text = str(round(BMI,2))+' (Normal)')
      elif 22.9<BMI<25:
            cal = int(BMI*random.randint(100,140))
            BMI_label_ans.config(text = str(round(BMI,2))+' (Perfect)')
      else:
            cal = int(BMI*random.randint(40,80))
            BMI_label_ans.config(text = str(round(BMI,2))+' (Overweight)')
      food(cal,Breakfast)
      food(cal,Lunch)
      food(cal,Snacks)
      food(cal,Dinner)



def food(cal,plan):
    sum = 0
    i=0
    b = []
    while sum<cal:
          b.append(random.choice(list(plan)[:]))
          i+=1
          sum+=plan.get(b[0])
    food = [str(food) if no==1 or food =='Sprouts'or'Tumeric Milk'or'Pohe'or'Soy Milk'or'hummus' else str(no)+' '+str(food)+'s' for food ,no in Counter(b).items()]
    if plan == Breakfast:
        Breakfast_Label_ans.config(text = ', '.join(food))
    elif plan == Lunch:
         Lunch_Label_ans.config(text = ', '.join(food))
    elif plan ==Snacks:
         Snacks_label_ans.config(text = ', '.join(food))
    else:
         Dinner_Label_ans.config(text = ', '.join(food))







#labels

age_label = Label(root,text='Age')
gender_label = Label(root,text='Gender')
height_label = Label(root,text='Height(m)')
weight_label = Label(root,text ='Weight(kg)')
disorder_label = Label(root,text = 'Disorder')
#diet_label = Label(root,text = 'Diet type')
#work_label = Label(root,text = 'Workout')
BMI_label = Label(root,text='BMI')
Breakfast_label = Label(root,text = 'Breakfast:')
Lunch_label = Label(root,text = 'Lunch:')
Snacks_label = Label(root,text = 'Snacks:')
Dinner_label = Label(root,text = 'Dinner:')

#label_placer
y_label_len = 40
for i in (age_label,gender_label,height_label,weight_label,disorder_label,BMI_label):
      i.place(x=100,y=y_label_len)
      y_label_len+=30

#food_label
y_food_lab=250
for _ in (Breakfast_label,Lunch_label,Snacks_label,Dinner_label):
            _.place(x=100,y=y_food_lab,width=600,height=20)
            y_food_lab+=30

#str to strvar
a = StringVar()#age
g = tk.StringVar()#gender
h = StringVar()#height strvar
w = StringVar()#weight strvar
d = StringVar()#disorder strvar
#y = StringVar()#diet strvar
#o = StringVar()#work strvar


gender = ttk.Combobox(root,textvariable=g)
gender['values'] = ('male','female','other')

disorder = ttk.Combobox(root,textvariable=d)
disorder['values'] = ('Diabetes','Cardio-vascular','liver','kidney')

'''
diet = ttk.Combobox(root,textvariable=y)
diet['values'] = ('Veg','Non-Veg','Jain','Vegan')

work = ttk.Combobox(root,textvariable=o)
work['values'] = ('low','medium','high')
'''

#entries
age_entry = Entry(root,textvariable=a)
height_entry = Entry(root,textvariable = h)
weight_entry = Entry(root,textvariable = w)



#label_ans
BMI_label_ans = Label(root)
Breakfast_Label_ans=Label(root)
Lunch_Label_ans = Label(root)
Snacks_label_ans = Label(root)
Dinner_Label_ans = Label(root)




#food_entry
y_food_en = 250
for j in (Breakfast_Label_ans,Lunch_Label_ans,Snacks_label_ans,Dinner_Label_ans):
            j.place(x=170,y=y_food_en,width=600,height=20)
            y_food_en+=30


#entry_placer
y_entry_len=40
for m in (age_entry,gender,height_entry,weight_entry,disorder,BMI_label_ans):
           m.place(x=170,y=y_entry_len,width=120,height=20)
           y_entry_len+=30

#cmds
find = Button(root,text = 'calculate',command = bmi,style = 'C.TButton')
quit = Button(root,text='quit',command=root.destroy,style='Q.TButton')

#cmd_placer
y_button_len=400
for j in (find,quit):
       j.place(x=150,y=y_button_len)
       y_button_len+=40

root.mainloop()
