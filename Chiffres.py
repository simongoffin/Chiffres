# -*-coding:utf-8 -*
#!/usr/bin/python

import re
import string
import sys

sys.path.append('/Users/simongoffin/Desktop/BOX/MAIN/Outils/Python files/Puzzle/aima-python')
from search import *

class ChiffresProblem(Problem):


    def __init__(self,init,goal):
        self.proche=0
        Problem.__init__(self, init, goal)

    
    def goal_test(self, state):
        for result in state:
            if abs(self.proche-self.goal)>abs(result-self.goal):
                self.proche=result
                if result==self.goal:
                    return True
        return False
            
    def successor(self, state):
        for valeur1 in state:
            temp=state[:]
            temp=temp[0:temp.index(valeur1)]+temp[temp.index(valeur1)+1:len(temp)]
            for valeur2 in temp:
                for operation in [1,2,3,4]:
                    check=possible(valeur1,valeur2,operation)
                    if check[0]:
                        newmove=temp[:]
                        newmove=newmove[0:newmove.index(valeur2)]+newmove[newmove.index(valeur2)+1:len(newmove)]
                        newmove=newmove+(check[1],)
                        #print newmove
                        etape=str(valeur1)+' '+check[2]+' '+str(valeur2)+' '+'='+' '+str(check[1])
                        yield (etape,newmove)
                    else: continue
                    
def possible(valeur1,valeur2,operation):
    #1==+
    if operation==1:
        return [True,valeur1+valeur2,'+']
    #2==-
    elif operation==2:
        return [valeur1-valeur2>0,valeur1-valeur2,'-']
    #3==*
    elif operation==3:
        return [True,valeur1*valeur2,'*']
    #4==/
    elif operation==4:
        return [valeur1%valeur2==0,valeur1/valeur2,'/']

if __name__ == "__main__":    
    tuple=(1,4,7,5,10,50)
    solution=916
    problem=ChiffresProblem(tuple,solution)
    #example of bfs search
    node=breadth_first_graph_search(problem)
    sol=problem.proche
    if node==None:
        problem=ChiffresProblem(tuple,sol)
        node=breadth_first_graph_search(problem)
    path=node.path()
    path.reverse()
    for n in path:
        print(n.action)
        print(n.state)
        
