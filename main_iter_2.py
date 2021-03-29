#!/usr/bin/python
import sys, getopt
import numpy as np

from scipy import optimize
import os
import matplotlib.pyplot as plt
import time

import module_particle_diff as particle_m
import module_2Dplotter_diff_2 as plotter2D
import thread
def plotdata(plots):
  plots.Plot()

    

        
def main(argv):
#  plt.ion()
  particles = 0  
  particles_list = []
  
  try:
    opts, args = getopt.getopt(argv,"hp:",["particles="])
  except getopt.GetoptError:
    print 'test.py -p <particles>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
       print 'test.py -p <particles> '
       sys.exit()
    elif opt in ("-p", "--particles"):
       particles = int(arg)

  limits = [[0, 0],[50,30]]
  limits2 = [[50, 50],[50.001,50.001]] 
  limits3 = [[0, 100],[0,100]]

  
  outname = "outfile22.txt"
  
  f = open(outname, "w")
  f.close()
  
  
  vel_to_sim = []
  vel_to_sim = np.concatenate((vel_to_sim , np.arange(0.01, 0.1, 0.01)))
  vel_to_sim = np.concatenate((vel_to_sim , np.arange(0.1, 1, 0.1)))
  vel_to_sim = np.concatenate((vel_to_sim , np.arange(1, 9, 0.2)))
  
  # np.concatenate(vel_to_sim, np.arange(0.1, 4, 0.1))
  
  print vel_to_sim
  
  for vel in vel_to_sim:
    f = open(outname, "a")
    particles_list = []
    
    for particles in range(particles):
      particles_list.append(particle_m.particle(vel))
    

    for item in (particles_list):
      item.Shuffle(limits2)


    plots = plotter2D.plot2D(particles, limits3)

  #  thread.start_new_thread( plotdata, (plots,) )

   # plots.Update(particles_list, 0)

    for i in range(1, 2000): 
      dt = 1
      for item in (particles_list):
       item.Move(dt, limits)#PLK-1 new
      # item.Move(0.5/0.23, dt, limits)     #PLK-1
      # item.Move(4.31, dt, limits)    #fast MEX5
      #  item.Move(0.035/0.068, dt, limits) #slow MEX5
    
   #   futures = [executor.submit(try_multiple_operations, group) 
   #          for group in grouper(particles/1000, particles_list)]
   #   concurrent.futures.wait(futures)

      plots.Update(particles_list, i*dt)
      if(i>5 and plots.D_std<plots.D*0.02): 
        break
       
  
    print(plots.D)  
    plots.close()
    print "writing"
    f.write(str(vel) + "\t" + str(plots.D) + "\n")
    f.close()
    
    
  f.close()
if __name__ == "__main__":
   main(sys.argv[1:])   
