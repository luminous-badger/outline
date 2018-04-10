#!/usr/bin/python

# Plot 'brot using PIL / Pillow. Plots x,y, not y,x as does pylab.
# JM Mon  5 Jan 2015 15:11:32 GMT
# For 1, L, and I images, use integers. For RGB images, use a 3-tuple containing integer values. 
# For F images, use integer or floating point values.
# Attempt to print outline of brot. Zoom in to top.
# JM Fri 30 Mar 2018 11:46:23 BST

from PIL import Image
import numpy as nm
import cmath
from timeit import default_timer as timer

start = timer()

X_MIN = -0.4
X_MAX =  0.2
Y_MIN = -1.3
Y_MAX = -0.5
offset     = 0.001
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

print 'X: ', X_SIZE ,' Y: ', Y_SIZE 

white      = (255,255,255)
randcolour = ( 190, 190, 190 )
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )

mycolour = ( 0, 0, 0 ) 
prev_iter = 0
x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( 0, 0 )
		C = complex ( X, Y )
		iter_count = 0

		while ( abs ( Z**2 ) < 4 and iter_count < maxiter ):
			Z = Z**2 + C
			iter_count = iter_count + 1
			calc_count = calc_count + 1  
		if ( prev_iter == iter_count ):
			img.putpixel( ( x_pixel,  y_pixel ), white ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		prev_iter = iter_count
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

fname = 'Outline_Brot_:' + '_X:' + str( X_MAX ) + str( X_MIN ) + '_Y:' + str( Y_MAX ) + str( Y_MIN ) + '_' + str( offset ) + '.png'

print 'Mandelbrot and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count
print 'Fname:', fname

img.show()
#img.save( fname )

