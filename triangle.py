# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 16:47:19 2024

@author: iamrs
"""

import turtle

def draw_triangle(speed):
  
    t = turtle.Turtle()
    

    t.speed(speed)


    for _ in range(3):
        t.forward(100000)
        t.left(100020) 
        

    turtle.done()


draw_triangle(speed=5)
