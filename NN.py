if __name__!='__main__':

    class Nn:
            def cache(self):
                 self.height = float(h.get())
                 self.weight = float(w.get())
                 self.age =  int(a.get())
                 self.gender = g.get()
                 self.disorder = d.get()
                 self.work = o.get()
                 self.diet = y.get()
                 self.x1 = self.age/1000
                 self.x2 = (self.weight/(self.height)**2)
                 self.x2 = self.x2/1000
                 if self.disorder == '':
                       self.x3 = 0
                 elif self.disorder == 'Diabetes' or self.disorder =='liver':
                       self.x3 = 1
                 else:
                       self.x3 = random.choice([0.2,0.6,0.8])
                 if self.work == 'high':
                       self.x4 = 1
                 else:
                       self.x4 = random.choice([0.2,0.6,0.8])
                 if self.gender == 'male':
                       cal = (66.4730 +(13.7516*self.weight)+(5.0033*self.height*100)-(6.7550*self.age))/4
                 else:
                       cal = (65.4730 +(9.7516*self.weight)+(2*self.height*100)-(4.67*self.age))/4
                 self.y = cal/10000
                 x_input.append([self.x1,self.x2,self.x3,self.x4])
                 y_input.append(self.y)
                 if len(x_input)>=5:#n param
                          self.x = np.array(x_input).T
                          self.y = np.array(y_input).T
                          return self.learn()

            def learn(self):

                  epoch = 0
                  self.alpha = (0.08)*(0.95)**epoch    #dynamic learning rate
                  if len(x_input)==5:
                       self.w1 = np.random.randn(4,4) #layer 1
                       self.w2 = np.random.randn(3,4) #layer 2
                       self.w3 = np.random.randn(2,3) #layer 3
                       self.w4 = np.random.randn(1,2) #layer 4

                       self.b1 = np.random.randn()
                       self.b2 = np.random.randn()
                       self.b3 = np.random.randn()
                       self.b4 = np.random.randn()

                  print('old parameters are\n w1 = {} \n w2 = {} \n w3 = {} \n w4 = {} \n b1 = {} \n b2 = {} \n b3 = {} \n b4 = {}\n o/p = {} \n\n '.format(self.w1,self.w2,self.w3,self.w4,self.b1,self.b2,self.b3,self.b4,10000*self.y))
                  Flag = True
                  while Flag:
                         epoch+=1
                         self.forwardprop()
                         if self.loss()<0.0001:
                                Flag = False
                                print(epoch)
                                print('new parameters are\n w1 = {} \n w2 = {} \n w3 = {} \n w4 = {} \n b1 = {} \n b2 = {} \n b3 = {} \n b4 = {}\n o/p = {} \n\n '.format(self.w1,self.w2,self.w3,self.w4,self.b1,self.b2,self.b3,self.b4,10000*self.a4))
                                self.calc()
            def forwardprop(self):
                      self.z1 = np.dot(self.w1,self.x)+self.b1
                      self.a1 = self.activation(self.z1)

                      self.z2 = np.dot(self.w2,self.a1)+self.b2
                      self.a2 = self.activation(self.z2)

                      self.z3 = np.dot(self.w3,self.a2)+self.b3
                      self.a3 = self.activation(self.z3)

                      self.z4 = np.dot(self.w4,self.a3)+self.b4
                      self.a4 = self.activation(self.z4)

                      self.backprop()
            def loss(self):
                      return (np.sum(((self.y-self.a4)**2))/len(self.y))
            def backprop(self):
                      #self.vdw = self.beta1*self.vdw +(1-self.beta1)*self.dw.T
                      #self.sdw = self.beta2*self.sdw +(1-self.beta2)*self.dw.T
                      #self.vdb = self.beta1*self.vdb +(1-self.beta1)*self.db        #adam optim
                      #self.sdb = self.beta2*self.sdb +(1-self.beta2)*self.db

                      self.dz4 = (self.a4-self.y)
                      self.dw4 = np.dot(self.a3,self.dz4.T)*(2/len(self.y))
                      self.db4 = np.sum(self.dz4)*(2/len(self.y))


                      self.dz3 = (self.a3-self.y)
                      self.dw3 = np.dot(self.a2,self.dz3.T)*(2/len(self.y))
                      self.db3 = np.sum(self.dz3)*(2/len(self.y))

                      self.dz2 = (self.a2-self.y)
                      self.dw2 =  np.dot(self.a1,self.dz2.T)*(2/len(self.y))
                      self.db2 = np.sum(self.dz2)*(2/len(self.y))

                      self.dz1 = (self.a1-self.y)
                      self.dw1 =  np.dot(self.x,self.dz1.T)*(2/len(self.y))
                      self.db1 = np.sum(self.dz1)*(2/len(self.y))
                      self.change()
            def change(self):
                      self.w1-=self.alpha*self.dw1.T
                      self.w2-=self.alpha*self.dw2.T
                      self.w3-=self.alpha*self.dw3.T
                      self.w4-=self.alpha*self.dw4.T

                      self.b1-=self.alpha*self.db1
                      self.b2-=self.alpha*self.db2
                      self.b3-=self.alpha*self.db3
                      self.b4-=self.alpha*self.db4
            def activation(self,z):
                       return z
            def calc(self):
                 self.z1 = np.dot(self.w1,self.x)+self.b1
                 self.a1 = self.activation(self.z1)

                 self.z2 = np.dot(self.w2,self.a1)+self.b2
                 self.a2 = self.activation(self.z2)

                 self.z3 = np.dot(self.w3,self.a2)+self.b3
                 self.a3 = self.activation(self.z3)

                 self.z4 = np.dot(self.w4,self.a3)+self.b4
                 self.a4 = self.activation(self.z4)
                 cal_hist.append(40000*np.average(self.a4))
