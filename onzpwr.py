#!/usr/bin/python

# Attempt to do a Newton fractal outline in Python.
# For any value of ZPower.
# JM Thu 16 Aug 2018 14:02:49 BST

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list

start = timer()

X_MIN   = -2.0
X_MAX   =  2.0
Y_MIN   = -2.0
Y_MAX   =  2.0
offset  =  0.01
epsilon = 0.01
maxiter = 50
calc_count = 0
rnum       = 93
lenlc      = len( colour_list )  
ZPower     = 3.5

X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1
X_SIZE  = int( X_SIZE )
Y_SIZE  = int( Y_SIZE )
print 'X: ', X_SIZE ,' Y: ', Y_SIZE 

white      = (255,255,255)
randcolour = ( 190, 190, 190 )
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )
mycolour   = ( 100, 150, 200 ) 

prev_iter = 0
x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		#Z = complex ( 0, 0 )
		Z = complex ( X, Y )
		iter_count = 0

		while ( abs ( Z**ZPower - 1 ) > epsilon and iter_count < maxiter ):
			if ( Z ):
				Z =  Z - ( Z**ZPower - 1 ) / ( ZPower * Z**( ZPower - 1 ) ) 

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

MsgText = 'Outline Newton for Z^' + str( ZPower ) 
if ( X_SIZE < 1000 ):
	print 'Less'
	fontsize = 12
else:
	print 'Grts'
	fontsize = 32

draw = ImageDraw.Draw(img)
font = ImageFont.truetype( "/Library/Fonts/Arial.ttf", fontsize )
draw.text( ( 0, 0 ),  MsgText, ( 139,0,0 ), font=font )

fname = 'Outline_Newton_Z' + str( ZPower ) + '_' + str( offset ) + '.png'
print 'Newton for Z^', ZPower, ' and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count
print 'Fname:', fname

img.show()
#img.save( fname )

