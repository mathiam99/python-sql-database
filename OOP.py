# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 02:58:01 2020

@author: mathiam
"""
class player:
    def __init__(self, prenom, nom, age, wage, position):
        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.wage = wage
        self.position = position
        
    def get_prenom(self):
        print(self.prenom)
    
    def set_prenom(self, prenom):
        self.prenom = prenom
        
    def get_nom(self):
        print(self.nom)
        
    def set_nom(self, nom):
        self.nom = nom
        
    def get_age(self):
        print(self.age)
    
    def set_age(self, age):
        self.age = age
        
    def get_wage(self):
        print(self.wage)
    
    def set_wage(self, wage):
        self.wage = wage
    
    def get_position(self):
        print(self.position)
    
    def set_position(self, position):
        self.position = position