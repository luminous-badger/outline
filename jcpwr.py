#!/usr/bin/python

# Julia set for C close to Zero.
# JM Mon  9 Jan 2017 20:38:39 GMT

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list 

start = timer()

X_MIN = -1.5
X_MAX =  1.5
Y_MIN = -1.5
Y_MAX =  1.5
offset     = 0.01
maxiter    = 100
calc_count = 0
rnum       = 93
ZPower     = 4
C          = complex (  -1.17, -0.0 )

lenlc      = len( colour_list ) 

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
randcolour =  ( 135,206,250) 
blue       = (0,0,255) 
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )

mycolour = ( 100, 150, 200 ) 
prev_iter = 0
x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( X, Y )
		iter_count = 0

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

MsgText = 'Outline Julia for Z^' + str( ZPower ) + str( C ) + ' and rnum: ' + str( rnum )
fname = 'Julia_X:' + str( X_MAX ) + str( X_MIN ) + '_Y:' + str( Y_MAX ) + str( Y_MIN ) + str( C ) + '.png'

draw = ImageDraw.Draw(img)
font = ImageFont.truetype( "/Library/Fonts/Arial.ttf", 12 )
draw.text( ( 0, 0 ),  MsgText, ( 139,0,0 ), font=font )

print MsgText, 'created in %f s' % dt
print 'Calc: ', calc_count
print 'Fname:', fname

img.show()
#img.save( fname )

