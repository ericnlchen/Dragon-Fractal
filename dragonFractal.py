import turtle
import random
'''
n=0   0==>2
e=1   1==>0
w=2   2==>3
s=3   3==>1
'''
turtle.colormode(255)
t1=turtle.Turtle()
t1.speed(100)
t1.hideturtle()
t1.pensize(4)
segmentLength=20
prev=[]
current=[]

def north():
 t1.pencolor(random.randint(100,240), random.randint(100,240), random.randint(100,240))
 t1.setheading(90)
 t1.forward(segmentLength)
 prev.append(0)
def east():
 t1.setheading(0)
 t1.forward(segmentLength)
 prev.append(1)
def west():
 t1.setheading(180)
 t1.forward(segmentLength)
 prev.append(2)
def south():
 t1.setheading(270)
 t1.forward(segmentLength)
 prev.append(3)

def transform(l):
 if l==[]:
   return []
 elif l[0]==0:
   return [2]+transform(l[1:])
 elif l[0]==1:
   return [0]+transform(l[1:])
 elif l[0]==2:
   return [3]+transform(l[1:])
 elif l[0]==3:
   return [1]+transform(l[1:])

def go(l):
 #takes in the prev list and goes where it says to go
 if l==[]:
   north()
 else:
   for x in range (0,len(l)):
     if l[x]==0:
       north()
     elif l[x]==1:
       east()
     elif l[x]==2:
       west()
     elif l[x]==3:
       south()
     x=x+1
'''
def dragon():
 current=transform(prev)
 current.reverse()
 go(current)
 dragon()
dragon()
'''

while(True):
 current=transform(prev)
 current.reverse()
 go(current)
 


#end

