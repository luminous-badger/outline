#!/usr/bin/python

# For 1, L, and I images, use integers. For RGB images, use a 3-tuple containing integer values. 
# For F images, use integer or floating point values.
# Print outline of brot.
# JM Sat 24 Mar 2018 12:59:19 GMT

import numpy as nm
import cmath
from timeit import default_timer as timer

start = timer()

X_MIN = -2.0
X_MAX =  1.0
Y_MIN = -1.4
Y_MAX =  1.4
offset     = 0.1
maxiter    = 50
calc_count = 0
rnum       = 73

# create a new X*Y pixel image surface
# make the background white (default bg=black)
X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1

X_SIZE = int( X_SIZE )
Y_SIZE = int( Y_SIZE )

print 'X: ', X_SIZE ,' Y: ', Y_SIZE 

prev_iter = 0
x_pixel = 0
# Have to do for X, for Y in ascii, to print horizontally.
for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
	y_pixel = 0
	for X in nm.arange ( X_MIN, X_MAX, offset ):
		Z = complex ( 0, 0 )
		C = complex ( X, Y )
		iter_count = 0

		#prev_iter = 0
		while ( abs ( Z**2 ) < 4 and iter_count < maxiter ):
			Z = Z**2 + C
			iter_count = iter_count + 1
			calc_count = calc_count + 1  
		'''
		print 'I:{0:3d}'.format( iter_count ),
		print 'P:{0:3d}'.format( prev_iter ),
		'''
		if ( prev_iter == iter_count ):
			print ' ',
			#print '{0:3d}'.format( iter_count ),
		else: 
			print '.', 
			#print '{0:3d}'.format( iter_count ),
		prev_iter = iter_count
		#print 'P2:{0:3d}'.format( prev_iter ),
		y_pixel += 1

	x_pixel += 1
	print

dt = timer() - start

MsgText = 'Brot for X:' + str( X_MIN ) + str( X_MAX ) + ' ,Y:' + str( Y_MIN ) + str( Y_MAX ) + ' rnum:' + str( rnum )

print 'Brot for X:', X_MIN, X_MAX, ',Y:', Y_MIN, Y_MAX, 'and Rand:', rnum, 'created in %f s' % dt
print 'pixel:', x_pixel, y_pixel
print 'Calc: ', calc_count

