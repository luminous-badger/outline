#!/usr/bin/python

# Brot with axes provided by pylab.
# Attempt to print outline of brot. Zoom in to top.
# JM Fri 30 Mar 2018 11:46:23 BST

import pylab as py
import numpy as nm
import cmath
from timeit import default_timer as timer

start = timer()

X_MIN = -0.35
X_MAX =  0.18
Y_MIN = -1.25
Y_MAX = -0.8
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
mycolour   = ( 0, 0, 0 )

py.image = nm.zeros(( Y_SIZE, X_SIZE ), dtype = nm.uint8)

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
			
			py.image[ y_pixel, x_pixel ] = iter_count
		else:
			py.image[ y_pixel, x_pixel ] = 0
		
		prev_iter = iter_count
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

MsgText = 'Brot for X:' + str( X_MIN ) + str( X_MAX ) + ' ,Y:' + str( Y_MIN ) + str( Y_MAX ) + ' rnum:' + str( rnum )

fname = 'Outline_Brot_:' + '_X:' + str( X_MAX ) + str( X_MIN ) + '_Y:' + str( Y_MAX ) + str( Y_MIN ) + '_' + str( offset ) + '.png'

print 'Mandelbrot and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count
print 'Fname:', fname

py.title( MsgText )
py.imshow( py.image, extent = [ X_MIN, X_MAX, Y_MAX, Y_MIN ] ) 
py.show()
#py.savefig( fname )

