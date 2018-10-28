# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 16:52:03 2018

@author: Nº 30000794 Nome: Ricardo Clemente Curso: Informática de Gestão
"""

from collections import Counter


baralho = {
        0:"1C",
        2:"1E",
        3:"1O",
        4:"1P",
        5:"2C",
        6:"2E",
        7:"2O",
        8:"2P",
        9:"3C",
        10:"3E",
        11:"3O",
        12:"3P",
        13:"4C",
        14:"4E",
        15:"4O",
        16:"4P",
        17:"5C",
        18:"5E",
        19:"5O",
        20:"5P",
        21:"6C",
        22:"6E",
        23:"6O",
        24:"6P",
        25:"7C",
        26:"7E",
        27:"7O",
        28:"7P",
        29:"8C",
        30:"8E",
        31:"8O",
        32:"8P",
        33:"9C",
        34:"9E",
        35:"9O",
        36:"9P",
        37:"10C",
        38:"10E",
        39:"10O",
        40:"10P",
        41:"VC",
        42:"VE",
        43:"VO",
        44:"VP",
        45:"DC",
        46:"DE",
        47:"DO",
        48:"DP",
        49:"RC",
        50:"RE",
        51:"RO",
        52:"RP"
        
        }



def conta_baralhos(lista):
    contador=Counter(lista)
    print("Contagem de Cartas Iguais:\n",contador)
    count_baralhos=0
    terminou=0
    while terminou==0:
        for x in baralho:
            
            if baralho[x] not in contador or contador[baralho[x]]==0:
                terminou=1
                
            else:
                contador[baralho[x]]=contador[baralho[x]]-1
                
        if terminou==0:        
            count_baralhos=count_baralhos+1 
    return count_baralhos   

         
if __name__ == '__main__':
    
    A = ["10E","10C","10P","10O","10E","10C","10P","10O","1P", "1C", "1O", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE", "1P", "1C", "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE", "1P", "1C", "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE"]

    print("\nExistem",conta_baralhos(A), "baralhos completos")

         