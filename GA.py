if __name__!='__main__':

    class Ga:
          def find(self):
               self.height = float(h.get())
               self.weight = float(w.get())
               self.age =  int(a.get())
               self.gender = g.get()
               self.disorder = d.get()
               self.work = o.get()
               self.diet = y.get()
               self.recom = random.choice([notify_label1,notify_label2,notify_label3,notify_label4,notify_label5,notify_label6])

               if len(cal_hist)==0:
                   if self.gender == 'male':
                        cal = (66.4730 +(13.7516*self.weight)+(5.0033*self.height*100)-(6.7550*self.age))//4
                        cal_ga.append(4*cal)
                        self.create_food(cal,Breakfast)
                        self.create_food(cal,Lunch)
                        self.create_food(cal,Snacks)
                        self.create_food(cal,Dinner)
                        self.notif2()

                   else:
                        cal = (65.4730 +(9.7516*self.weight)+(2*self.height*100)-(4.67*self.age))//4
                        cal_ga.append(4*cal)
                        self.create_food(cal,Breakfast)
                        self.create_food(cal,Lunch)
                        self.create_food(cal,Snacks)
                        self.create_food(cal,Dinner)
                        self.notif2()
               else:
                    self.create_food(cal_hist[-1]//4,Breakfast)
                    self.create_food(cal_hist[-1]//4,Lunch)
                    self.create_food(cal_hist[-1]//4,Snacks)
                    self.create_food(cal_hist[-1]//4,Dinner)
                    self.notif2()
                    self.notify1()

          def notify1(self):
               notify_label.place(x=130,y=390)


          def notif2(self):
               self.recom.place(x=500,y=400)
               self.recom.after(3000,lambda: self.recom.destroy())

          def progress(self):
              plt.xlim(0,40)
              plt.xlabel('Months')

              plt.ylim(0,3000)
              plt.ylabel('Calories')

              cal_ga.extend(cal_hist)
              plt.plot(cal_ga)
              plt.show()


          def create_food(self,cal,plan):
               gene_size = 7
               population = []
               population_size = 10
               dup = plan.copy()
               bad_food = []
               if plan == Breakfast:
                     if self.disorder!='' or self.diet!='Non-Veg':
                            bad_food = ['Dairy Products','Honey','Yoghurt','Coffee','Upma','Cereal','Egg white','Soft Boiled Egg','Bacon fried','Omelette']
               elif  plan == Lunch:
                      if self.disorder!='' or self.diet!='Non-Veg':
                           bad_food = ['Fish','Meat','Prawns','Egg curry','Curd','Cheese','Paneer','Rice']
               elif plan == Dinner:
                      if self.disorder!='' or self.diet!='Non-Veg':
                            bad_food = ['Peanut butter','Meat','Fish','Prawns','Egg curry']
               elif plan == Snacks:
                       if self.disorder!='' or self.diet!='Non-Veg':
                          bad_food= ['Bhel','Jam','Mars bar','Dark Chocolate','Cottage Cheese','Hard Boiled egg']
               for item in bad_food:
                     del dup[item]
               for _ in range(population_size):
                    population.append([random.choice(list(dup)[:]) for _ in range(gene_size)])

               return self.genetic(cal,population,dup,plan)
          def fitness(self,group,plan):
             fit=0
             for item in group:
                    fit+=plan.get(item)
             return fit

          def cross(self,pool,dup):
             child=[]
             parent1 = random.choice(pool)
             pool.remove(parent1)
             parent2 = random.choice(pool)
             for child1,child2 in zip(parent1,parent2):
                   if random.random()<0.5:
                       child.append(child1)
                   elif random.random()<0.7:
                       child.append(child2)
                   else:
                        child.append(random.choice(random.choice(pool))) #mutation
             return child

          def genetic(self,cal,population,dup,plan):
               while self.fitness(population[0],plan)<=cal:
                    population = sorted(population,key = lambda group:self.fitness(group,plan))
                    new_gen = []
                    new_gen.extend(population[0:3])
                    for _ in range(7):
                          new_gen.append(self.cross(population[3:9],dup))
                    population = new_gen
               if plan == Breakfast:
                    Breakfast_Label_ans.config(text = ',\n'.join(set(population[0])))
               elif plan == Lunch:
                    Lunch_Label_ans.config(text = ',\n'.join(set(population[0])))
               elif plan ==Snacks:
                    Snacks_label_ans.config(text = ',\n'.join(set(population[0])))
               else:
                    Dinner_Label_ans.config(text = ',\n'.join(set(population[0])))
