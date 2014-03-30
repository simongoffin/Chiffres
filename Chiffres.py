# -*-coding:utf-8 -*
#!/usr/bin/python

import re
import string
import sys

sys.path.append('/Users/simongoffin/Desktop/MAIN/Outils/Python files/Puzzle/aima-python')
from search import *

class PuzzleProblem(Problem):

    def __init__(self,init,goal):
        goal1 = re.compile(goal)
        Problem.__init__(self, init, goal1)

    
    def goal_test(self, state):
        return self.goal.search(state) != None

    mapping = string.maketrans('345789','222666')
    dico={}
    #dico[self.initial.translate(self.mapping)]=1
    
    def canonical(self, state):
        canonical_state=state.translate(self.mapping)
        return canonical_state

    invalidpos = { (0,-4):None, (1,-4):None, (2,-4):None, (3,-4):None,
              (16,4):None, (17,4):None, (18,4):None, (19,4):None,
              (0,-1):None, (4,-1):None, (8,-1):None, (12,-1):None, (16,-1):None,
              (3,1):None, (7,1):None, (11,1):None, (15,1):None, (19,1):None, }
                 
    def successor(self, state):
        pos1 = state.find('0')
        pos2 = state.find('0',pos1+1)
        l = []
        for pos in [pos1, pos2]:
            for sw in [-4,-1,1,4]:
                if (pos,sw) in self.invalidpos: continue
                square = state[pos+sw]
                if square == '0': continue
                newmove = state.replace(square, '0')
                for i in range(20):
                    if 0 <= i+sw < 20 and state[i+sw]==square:
                        newmove = newmove[:i] + square + newmove[i+1:]
                if newmove.count('0') != 2: continue
                symetrie=newmove.translate(self.mapping)
                if symetrie not in self.dico:
                    self.dico[symetrie]=1
                    yield (sw, newmove)
                else: continue

def formatstate(stri):
    out = '\n'
    #pos = stri.replace( '0', '.' )
    for i in [0,4,8,12,16]:
        for x in range(i,i+4):
            out = out + stri[x] + ' '
        out = out + '\n'
    return out

if __name__ == "__main__":    
    problem=PuzzleProblem('211321130AA046754895','.................11.')
    #example of bfs search
    node=breadth_first_graph_search(problem)
    #example of print
    print(node)
    path=node.path()
    path.reverse()
    i=0
    for n in path:
        print(formatstate(n.state))
        i+=1
    print(i)
