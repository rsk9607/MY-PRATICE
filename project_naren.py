#!/usr/bin/env python
'''
To plot animation of the planet system.
'''
import os
import sys
import numpy as np
import pylab
from matplotlib.animation import FuncAnimation

r_e = 1 # in au
r_m = 1.5 # in au
a = 1.25

t_e = 1 # in yr
t_m = 1.5**(3/2) # in yr
t_r = 1.25**(3/2) # in yr

scaling = 5 # in sec

t_es = t_e*scaling # in sec
t_ms = t_m*scaling # in sec
t_rs = t_r*scaling # in sec

omega_e = 2*np.pi/t_es # angular speed rad/sec
omega_m = 2*np.pi/t_ms # angular speed rad/sec
omega_r = 2*np.pi/t_rs # angular speed rad/sec

t_tot = 15 # sec
t = np.linspace(0., t_tot, 1000) # 

phi_e = 0.
#phi_m = np.pi/4.
phi_m = 11*np.pi/45
phi_r = 0.

theta_e = omega_e*t + phi_e
theta_m = omega_m*t + phi_m
theta_r = omega_r*t + phi_r

#r_r = (0.96*a)/(1+0.2*np.cos(theta_r))


'''
figure = pylab.figure()
ax = figure.add_subplot(111)

ax.set_xlim(0., t_tot)
ax.set_ylim(0., np.max(theta_e))

point, = ax.plot(0., 0.0, marker='o', color='r', ms=9)

x = []
y = []

def animation_function(i):
#	x.append(t[i])
#	y.append(theta_e[i])

	point.set_xdata(t[i])
	point.set_ydata(theta_e[i])
	
	return point,

animation = FuncAnimation(figure, func=animation_function, frames=np.arange(t.size), interval=t_tot)

pylab.show()

sys.exit()

'''

fig = pylab.figure()
ax = fig.add_subplot(111, projection='polar')
#ax.set_rticks([1., 1.5, 2])
#ax.grid(True)

point, = ax.plot(phi_e, r_e, marker='o', color='b', ms=9)
point2, = ax.plot(phi_m, r_m, marker='o', color='r', ms=9)
point3, = ax.plot(phi_r,a, marker = '<', color='g', ms=9)

ax.set_rmax(2.)
ax.set_rticks([1., 1.5, 2])

def animation_function(i):
	tx = r_e
	ty = theta_e[i]

	ttx = r_m
	tty = theta_m[i]

	tttx=1
	ttty=0
 
	if t[i]>t_rs/2:
		tttx = ttx
		ttty = tty
	else:
		tttx = (0.96*a)/(1+0.2*np.cos(theta_r[i]))
		ttty = theta_r[i]
	
   
	point.set_xdata(ty)
	point.set_ydata(tx)

	point2.set_xdata(tty)
	point2.set_ydata(ttx)
	
	point3.set_xdata(ttty)
	point3.set_ydata(tttx)
	
	
	
	return point,

animation = FuncAnimation(fig, func=animation_function, frames=np.arange(t.size), interval=t_tot)

pylab.show()

sys.exit()

























'''
fig = pylab.figure()
ax = fig.add_subplot(111)

ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.axvline(x=0, color='k', ls='-', lw=2)
ax.axhline(y=0, color='k', ls='-', lw=2)

point, = ax.plot(r_e, phi_e, marker='o', color='r', ms=9)
point2, = ax.plot(r_m, phi_m, marker='o', color='b', ms=9)




def animation_function(i):
#	x.append(r_e)
#	y.append(theta_e[i])

	tx = r_e*np.cos(theta_e[i] + phi_e)
	ty = r_e*np.sin(theta_e[i] + phi_e)

	ttx = r_m*np.cos(theta_m[i] + phi_m)
	tty = r_m*np.sin(theta_m[i] + phi_m)


#	x.append()
	 

	point.set_xdata(tx)
	point.set_ydata(ty)

	point2.set_xdata(ttx)
	point2.set_ydata(tty)
	
	return point,

animation = FuncAnimation(fig, func=animation_function, frames=np.arange(t.size), interval=t_tot)

pylab.show()
'''