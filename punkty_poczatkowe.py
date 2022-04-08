# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 18:38:06 2021

@author: patry
"""

import random
import os

def start_points():
    path = r'D:\Dokumenty\KURSY\PYTHON\Odpowiedzi\PROJEKT_KONCOWY'
    for filename in files:
        filepath = os.path.join(path,filename)
        file = open(filepath, 'w')
        list = random_wsp()
        for x in list:
            file.write(x+'\n')
        file.close()

def random_wsp():    
    max = 100
    list = []
    for i in range(3):
        x = random.randint(1,max)
        y = random.randint(1,max)
        wsp = [x,y]
        wsp_file = str(wsp[0])+' '+str(wsp[1])
        list.append(wsp_file)
    return list

pets = ['cats_pussys', 'cats_lazy', 'cats_casual', 'mice']
txt = '.txt'
files = []
for pet in pets:
    filename = pet+txt
    files.append(filename)

start_points()