#!/usr/bin/python

# Plot 'brot using PIL / Pillow. Plots x,y, not y,x as does pylab.
# JM Mon  5 Jan 2015 15:11:32 GMT
# For 1, L, and I images, use integers. For RGB images, use a 3-tuple containing integer values. 
# For F images, use integer or floating point values.
# Print X,Y Co-ords & iter_count.
# JM Wed 27 May 2015 09:39:22 BST

#from PIL import Image
import numpy as nm
import cmath
from timeit import default_timer as timer

start = timer()

X_MIN = -2.0
X_MAX =  1.0
Y_MIN = -1.4
Y_MAX =  1.4
offset     = 0.01
maxiter    = 50
calc_count = 0
rnum       = 3

# create a new X*Y pixel image surface
# make the background white (default bg=black)
X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1

X_SIZE = int( X_SIZE )
Y_SIZE = int( Y_SIZE )

#print 'X: ', X_SIZE ,' Y: ', Y_SIZE 
print X_SIZE ,',', Y_SIZE 

x_pixel = 0
for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
	y_pixel = 0
	for X in nm.arange ( X_MIN, X_MAX, offset ):
		Z = complex ( 0, 0 )
		C = complex ( X, Y )
		iter_count = 0

		while ( abs ( Z**2 ) < 4 and iter_count < maxiter ):
			Z = Z**2 + C
			iter_count = iter_count + 1
			#print X, Y , Z
			calc_count = calc_count + 1  
		print  x_pixel, ',', y_pixel, ',', iter_count 
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

#print 'Mandelbrot and Rand:', rnum, 'created in %f s' % dt
#print 'Calc: ', calc_count
#img.show()
#img.save( 'Pillow_brot.png' )

