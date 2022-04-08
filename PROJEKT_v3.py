# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 18:11:45 2022

@author: patry
"""

import random
import matplotlib.pyplot as plt
import os

class Pets(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coord = (x, y)         # współrzędne początkowe
        self.coords = [self.coord]  # lista współrzędnych
        
    def start_point(self):
        plt.scatter(self.coord[0], self.coord[1], c=self.color)
        
    def move(self):
        while True:
            x = self.x + random.randint(-self.move, self.move)
            y = self.y + random.randint(-self.move, self.move)
            if self.limit(x, y) == True:
                self.x = x
                self.y = y
                self.coords.append((self.x, self.y))
                return self.coords
            elif self.limit(x, y) == 'cat casual nearby':
                self.x = self.coords[0][0]
                self.y = self.coords[0][1]
                self.coords.append((self.x, self.y))
                return self.coords
            elif self.limit(x, y) == 'cat lazy nearby':
                self.x = self.coords[0][0]
                self.y = self.coords[0][1]
                self.coords.append((self.x, self.y))
                return self.coords
            else:
                continue


class cats_pussys(Pets):
    color = 'red'    
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.move = 5
    
    def start_point(self):
        super().start_point()
        
    def move(self):
        super().move()
    
    def limit(self, x, y):
        if x <= 100 and x >= 0 and y <= 100 and y >= 0:
            return True
        else:
            return False


class cats_lazy(Pets):
    color = 'orange'
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.move = 10
    
    def start_point(self):
        super().start_point()
        
    def move(self):
        super().move()
        
    def limit(self, x, y):
        if x <= 100 and x >= 0 and y <= 100 and y >= 0:
            return True
        else:
            return False
        
        
class cats_casual(Pets):
    color = 'yellow'
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.move = 10
    
    def start_point(self):
        super().start_point()
        
    def move(self):
        super().move()
        
    def limit(self, x, y):
        if x <= 100 and x >= 0 and y <= 100 and y >= 0:
            return True
        else:
            return False        
        
        
class mice(Pets):
    color = 'magenta'
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.move = 1
    
    def start_point(self):
        super().start_point()
        
    def move(self):
        super().move()
    
    def limit(self, x, y):
        if x <= 100 and x >= 0 and y <= 100 and y >= 0:  # warunek ogródka 100x100
            for instance in cats_casual_instances:
                cat_x = instance.coords[-1][0]
                cat_y = instance.coords[-1][1]
                
                # powinno być odwołanie do kolejnej funkcji sprawdzającej następny warunek
                
                if abs(x-cat_x) < 4 and abs(y-cat_y) <4: # warunek zbliżenia do kota zwykłego
                    return 'cat casual nearby'
                else:
                    continue
            
            for instance in cats_lazy_instances:
                cat_x = instance.coords[-1][0]
                cat_y = instance.coords[-1][1]
                if abs(x-cat_x) < 4 and abs(y-cat_y) <4: # warunek zbliżenia do kota leniwego
                    return 'cat lazy nearby'
                else:
                    return True
                
        else:
            return False
        
        # cat_x = cats_casual.coords[-1][0]
        # cat_y = cats_casual.coords[-1][1]
        # print(cat_x)
        # print(cat_y)
        # if 
        
        
        
# utworzenie macierzy (ogródka)
def plot(max_x, max_y, min_x=0, min_y=0):
    plt.grid()
    plt.ylim(min_x-10, max_x+10)
    plt.xlim(min_y-10, max_y+10)
    
    
# odczytanie współrzędnych z plików
def points(pet):
    # {0} = pet name    
    source = '''
global {0}_points
{0}_points = []
filepath = os.path.join(os.getcwd(), 'pets', '{0}.txt')
with open(filepath, 'r') as file:
    for line in file:
        point = line.split(' ')
        point = (int(point[0]), int(point[1]))
        {0}_points.append(point)
'''.format(pet)
    return exec(source)


# utworzenie instacji podając współrzędne początkowe
def create_pet(pet):
    # {0} = pet name
    source = '''
global {0}_instances
{0}_instances = []          # lista instancji danej klasy
for point in {0}_points:
    x = point[0]
    y = point[1]
    {0}_instance = {0}(x, y)
    {0}_instances.append({0}_instance)
    {0}(x, y).start_point()
'''.format(pet)
    return exec(source)
  

# ruchy zwierzakow
def pets_moves(pet):
    source = '''
for instance in {0}_instances:
    {0}.move(instance)
'''.format(pet)
    return exec(source)


def pets_moves_show(pet):
    source = '''
for instance in {0}_instances:
    X = []
    Y = []
    for coord in instance.coords:
        X.append(coord[0])
        Y.append(coord[1])
    plt.plot(X, Y, c = instance.color)
'''.format(pet)
    return exec(source)


max_x = 100
min_x = 0
max_y = 100
min_y = 0

plot(max_x, max_y, min_x, min_y)

pets = []
path = os.path.join(os.getcwd(), 'pets')
for root, dirs, files in os.walk(path):
    for name in files:
        pet = name.replace('.txt','')
        pets.append(pet)# utworzenie listy typów zwierząt
        points(pet)     # odczytanie współrzędnych z plików - zapisanie w listach _points
        create_pet(pet) # utworzenie instacji klas i wrzucenie na macierz


i = 0
max = 100

while i < max:
    for pet in pets:
        pets_moves(pet)  
    i += 1
    
for pet in pets:
    pets_moves_show(pet)


# points()        # odczytanie współrzędnych z plików - zapisanie w listach _points
# create_pet()    # utworzenie instacji klas i wrzucenie na macierz
# pets_moves()    # rozpoczęcie pętli ruchów