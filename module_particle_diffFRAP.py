import random
import math


class particle:
  
  def __init__(self, v, i):
    self.x = 0
    self.y = 0
    self.z = 0

    random.seed(i)

    self.vx = 0
    self.vy = 0
    self.id = 0
    
    self.v = v
  
  def isinside(self, x,y,z):
    if (x<self.limits[1][0] and x>self.limits[0][0] and y<self.limits[1][0] and y>self.limits[0][1] and z<self.limits[1][2] and z>self.limits[0][2]):
      return True
    else:
      return False
      
  def Move(self, dt, limits):



    it = True
    
    while(it):
      
      theta = random.uniform(0, 2*math.pi)
      phi = random.uniform(0, math.pi)
      
      x = (self.x + self.v*math.cos(theta)*math.sin(phi)*dt)
      y = (self.y + self.v*math.sin(theta)*math.sin(phi)*dt)
      z = (self.z + self.v*math.cos(phi)*dt)

      
      if (self.isinside(x,y,z)):
        
        it = False
        self.x = x
        self.y = y
        self.z = z

    
  def Shuffle(self, limits):
    
    #the shuffling is done according to a fixed initial percentage
    
    self.limits = limits
    
    x = random.uniform(limits[0][0], limits[1][0])
    y = random.uniform(limits[0][1], limits[1][1])
    z = random.uniform(limits[0][2], limits[1][2])

    self.x = x
    self.y = y
    self.z = z
  
  def FRAP(self):
    if (self.x**2+self.y**2<0.04):
      return True
    else:
      return False
    