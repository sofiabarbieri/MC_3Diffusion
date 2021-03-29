import random
import math


class particle:
  random.seed(None)
  
  def __init__(self, v):
    self.x = 0
    self.y = 0
    self.z = 0

    self.vx = 0
    self.vy = 0
    self.id = 0
    
    self.v = v
    
  def Move(self, dt, limits):

      
    theta = random.uniform(0, 2*math.pi)
    phi = random.uniform(0, math.pi)

    x = (self.x + self.v*math.cos(theta)*math.sin(phi)*dt)
    y = (self.y + self.v*math.sin(theta)*math.sin(phi)*dt)
    z = (self.z + self.v*math.cos(phi)*dt)
    self.x = x
    self.y = y
    self.z = z

    
  def Shuffle(self, limits):
    
    #the shuffling is done according to a fixed initial percentage
    
    
    x = random.uniform(limits[0][0], limits[1][0])
    y = random.uniform(limits[0][1], limits[1][1])

    self.x = x
    self.y = y
    