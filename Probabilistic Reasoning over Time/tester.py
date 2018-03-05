from robot import Robot
from HiddenMarkovModel import hmm
import numpy as np 
import matplotlib.pyplot as plt

class tester():
    def __init__(self, m, n ):
        self.m = m # amount of rows
        self.n = n #amount of columns
        self.newrobot = Robot(m, n)
        self.newrobot.init_robot()        
        dimension =  m * n * 4
        start_probability = 1/(dimension)
        self.f_old = np.array([[start_probability] for y in range(dimension)])

        #print(self.f_old)
        self.HiddenMM = hmm(m,n)


    def one_step(self):
        field = self.newrobot.ret_field()
        #for x in range(0,self.newrobot.row):
         #   print("", end="\n")
          #  for y in range(0, self.newrobot.column):
           #      print(field[x][y], end=" ")
        #print("\n")   
        evidence = self.newrobot.sensor()
        #print(evidence[0],evidence[1])
        #print("EVIDENCE")
        self.f_old = self.HiddenMM.forward_filtering(self.f_old, evidence)
     
        self.newrobot.move()
        #print(self.newrobot.return_pos())
       
        return field, self.f_old


def final_test(m,n):
    test = tester(4,4)
    while True:
        x = input("1 to make a move")
        y = int(x)
   
        if y == 1:
            field, onestep = test.one_step()
            maximal = 0
            t = 0
            j = 0
            i = 0
            visualisation = np.zeros((m,n))
            for x in np.nditer(onestep):
                if x > maximal:
                    maximal = x
                
                t += 1
                if t == 4:
                    visualisation[i,j] = maximal
                    maximal= 0
                    j+=1        
                    t=0
                    if j == 4: 
                        j =0
                        i += 1
            
            visualisation = visualisation/ visualisation.sum()


                    
            plt.imshow(visualisation,interpolation='nearest', cmap = 'Blues')
            plt.xlabel('HMM Guess')
            plt.colorbar()
            plt.show()

            plt.imshow(field, cmap = 'Blues', interpolation='nearest')
            plt.xlabel('Robot')
            plt.colorbar()
            plt.show()

final_test(4,4)
#test = tester(4,4)




      #  print(onestep)
        #for x in range(0,4):
         #   print("\n")
          #  for y in range(0,4):
           #     print('  ',end="")
            #    for z in range(0,4):
             #       print(onestep[x][0], end="")
        

        


