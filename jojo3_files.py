import os
import sys
import random
import threading
import time


true = True
false = False

class scene:
    def __init__(self,name,func):
        self.name = name
        self.function = func

class item:
    def __init__(self,name,description = "Нет описания.",types = "none"):
        self.name = name
        self.description = description
        self.type = types

class man:
    def __init__(self):
        self.hunger = 100
        self.drunk = 100
        self.sleepness = 100
        self.health = 100
        self.items = []
        self.bag_level = 8;
        self.money = 0

class house:
    def __init__(self):
        self.fridge = []


class prg:
    def __init__(self,engine_name):
        self.isworking = true
        
        self.engine_name = engine_name
        self.scenes = []

    def add_scene(self,sc):
        self.scenes.append(sc)

    def save(self):
        pass

    def clear(self):
        if(os.name == "dos" or os.name == "nt"):
            os.system("cls")
        else:
            try:
                os.system("clear")
            except:
                print("Произошла ошибка. Приложение не смогло определить Вашу систему!")
                input(">")
                exit(0) 

    def critical_error(self):
        print("В " + self.engine_name + " произошла критическая ошибка.")
        self.isworking = false;
        self.save()
        input(">")
        exit(0)

    def find_scene(self,name):
        id = -1
        for i in range(len(self.scenes)):
            if(self.scenes[i].name == name):
                id = i
                break
        return id
    
    def load_scene(self,name):
        
        self.scenes[self.find_scene(name)].function()




