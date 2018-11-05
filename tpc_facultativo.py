# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 00:13:17 2018

@author: 30000794 Ricardo Clemente Informática de Gestão
"""

def recebe_string(string):
    count=0
    soma=0
    sub=0    
    for i in range (len(S)):
        
        
        count=count+1
        if S[i]=='+':
            for c in range(1,count):
                
                soma=soma+int(S[i-c])
                
            count=0
            
        if S[i]=='-':
            for c in range(1,count):
                
                sub=sub+int(S[i-c])
                
            count=0
            
    return (soma-sub)

if __name__ == "__main__":

    S="356+6-"

        
    print("O resultado é ",recebe_string(S))                
            
            