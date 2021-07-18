import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.animation import FuncAnimation
import numpy as np
from scipy import optimize
from scipy.stats import norm
import matplotlib.mlab as mlab

class plot2D():
  
  def __init__(self, number, limits):
    
    self.x = [0] * number
    self.y = [0] * number

    self.limits = limits
    self.list_m_fit_pre = []
    
    self.D = 0.0
    self.D_std = 0.0
    self.D_arr = []
    
    global fig, fig1, fig2
    fig = plt.figure()
    fig1 = plt.figure()

    self.ax1 = fig.add_subplot(1,1,1)
    self.ax2 = fig1.add_subplot(1,1,1)
    fig2 = plt.figure()


    
    plt.grid(True)
    plt.subplots_adjust(hspace = 1,wspace = 0.6)
    

  def Update(self, particles, t):

    del self.x[:]
    del self.y[:]

  
    for index, item in enumerate (particles):
        self.x.append(item.x)
  
    self.Plot(t)

  def Plot(self, t):
    
    fig.clf()
    fig1.clf()

    self.ax1 = fig.add_subplot(1,1,1)

    self.ax2 = fig1.add_subplot(1,1,1)
    
    
    (mu, sigma) = norm.fit(self.x)

    
    n, bins, patches = self.ax2.hist(self.x, 600, normed=1, facecolor='green', alpha=0.75)
    sigma_sq = sigma**2
    
    y = mlab.normpdf( bins, mu, sigma)
    l = self.ax2.plot(bins, y, 'r--', linewidth=2)

    
    D = sigma_sq/2/t

    print("--")
    print sigma
    print sigma_sq
    print D
    
    print("--")
    
    self.list_m_fit_pre.append(sigma_sq**2)
    
    self.D = D
    self.D_arr.append(D)
    self.D_std = np.std(np.array(self.D_arr[-7:]))
    
    
    fig2.clf()

    t_pre = np.arange(len(self.list_m_fit_pre))
    self.ax3 = fig2.add_subplot(1,1,1)
    self.ax3.plot(t_pre, self.D_arr, marker='', linewidth=1, alpha=0.9)



    fig.canvas.draw()

    plt.show(block=False)
    plt.pause(0.1)
    #

  def gaus(self, x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))
  def close(self):
    plt.close('all')
    plt.close()
