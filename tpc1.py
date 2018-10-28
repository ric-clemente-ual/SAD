# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:10:20 2018

@author: 30000794 Ricardo Clemente Informática de Gestão
"""

def Solution(S):
    
    parenteses = 0
    parenteses_recto = 0
    chavetas=0
    
    for i in range (len(S)):
        if parenteses==-1 or chavetas==-1 or parenteses_recto==-1:
            return 0
        if S[i] == "(":
            parenteses = parenteses + 1
        if S[i] == ")":
            parenteses = parenteses - 1
        if S[i] == "[":
            parenteses_recto = parenteses_recto + 1
        if S[i] == "]":
            parenteses_recto = parenteses_recto - 1            
        if S[i] == "{":
            chavetas = chavetas + 1
        if S[i] == "}":
            chavetas = chavetas - 1 
            
    #print (parenteses,parenteses_recto,chavetas)  
          
    if parenteses != 0 or parenteses_recto!=0 or chavetas!=0:
        return 0
    else: 
        return 1
    

if __name__ == '__main__':
    
    S="{[() ()]}"
    #S="{[( ()]}"
    #S="{[) (]}"
    
    resultado=Solution(S)
    print(resultado)