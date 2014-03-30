# -*-coding:utf-8 -*
#!/usr/bin/python

import re
import string
import sys

sys.path.append('/Users/simongoffin/Desktop/BOX/MAIN/Outils/Python files/Puzzle/aima-python')
from search import *

class ChiffresProblem(Problem):

    def __init__(self,init,goal):
        Problem.__init__(self, init, goal)

    
    def goal_test(self, state):
        for result in state:
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
                        yield (operation,newmove)
                    else: continue
                    
def possible(valeur1,valeur2,operation):
    #1==+
    if operation==1:
        return [True,valeur1+valeur2]
    #2==-
    elif operation==2:
        return [valeur1-valeur2>0,valeur1-valeur2]
    #3==*
    elif operation==3:
        return [True,valeur1*valeur2]
    #4==/
    elif operation==4:
        return [valeur1%valeur2==0,valeur1/valeur2]

if __name__ == "__main__":    
    problem=ChiffresProblem((1,2,3,4),10)
    #example of bfs search
    node=breadth_first_graph_search(problem)
    #example of print
    print(node)
    path=node.path()
    path.reverse()
    for n in path:
        print(n.state)
        
