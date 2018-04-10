#!/usr/bin/python

# Plot 'brot using PIL / Pillow. Plots x,y, not y,x as does pylab.
# JM Mon  5 Jan 2015 15:11:32 GMT
# For 1, L, and I images, use integers. For RGB images, use a 3-tuple containing integer values. 
# For F images, use integer or floating point values.
# Julias for Z^3
# JM Thu 26 Oct 2017 16:17:55 BST

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list
import sys

start = timer()

X_MIN = -1.3
X_MAX =  1.3 
Y_MIN = -1.3
Y_MAX =  1.5
offset     = 0.01
maxiter    = 195
calc_count = 0
rnum       = 93
#rnum       = int( sys.argv[ 1 ] )
ZPower     = 3
CInput     = float( sys.argv[ 1 ] )
#C          = complex ( CInput, 0.211  )
#C          = complex ( CInput,  0.0  )
C          = complex ( 0.0, CInput   )
#C          = complex ( 0.601, 0.301 )

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
randcolour = (255,218,255)
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )
lenlc      =  len( colour_list ) 

mycolour = ( 100, 150, 200 ) 
prev_iter = 0
x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( X, Y )
		iter_count = 0
		#print 'XYZ:', X,Y,Z

		while ( abs ( Z**ZPower ) < 4 and iter_count < maxiter ):
			Z = Z**ZPower + C
			iter_count = iter_count + 1
			#print X, Y , Z
			calc_count = calc_count + 1  
		if ( prev_iter == iter_count ):
			img.putpixel( ( x_pixel,  y_pixel ), white ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		prev_iter = iter_count
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

MsgText = 'Outline Julia for Z^' + str( ZPower ) + ' ' + str( C ) 

draw = ImageDraw.Draw(img)
font = ImageFont.truetype( "/Library/Fonts/Arial.ttf", 12 )
draw.text( ( 0, 0 ),  MsgText, ( 0,0,0 ), font=font )

#print 'Julia for:', C, 'created in %f s' % dt
print MsgText , 'created in %f s' % dt
print  'X: ' + str( X_MAX ) + ' ' + str( X_MIN ) + ' Y: ' + str( Y_MAX ) + ' ' + str( Y_MIN ) 
print 'Calc: ', calc_count

fname = 'Outline_Julia_Z3:' + str( C ) + '_X:' + str( X_MAX ) + str( X_MIN ) + '_Y:' + str( Y_MAX ) + str( Y_MIN ) + '.png'
print 'Fname:', fname

img.show()
#img.save( fname )

