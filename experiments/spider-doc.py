from dbscode_minecraft import *

bulldoze()

def leg(pos, flip, colour):
	if(flip):
		box(colour, pos+point(-7, 0, 0), point(8, 1, 1))
		box(colour, pos+point(-7, -1, 0), point(1, -7, 1))
	else:
		box(colour, pos, point(8, 1, 1))
		box(colour, pos+point(7, -1, 0), point(1, -7, 1))

def eyes(pos, colour):
	draw = True
	for x in range(-2, 3):
		for y in range(-1, 2):
			if True == draw:
				box(colour, point(pos.x + x, pos.y + y, pos.z), point(1, 1, 1))
			draw = ~draw

def spider(body_colour, leg_colour, pos):
	sphere(body_colour, pos, 8)
	sphere(body_colour, pos+point(0, 0, 13), 6) 
	for i in range(-2, 2):
		leg(pos+point(8, 0, i * 2 + 1), False, leg_colour)
		leg(pos+point(-8, 0, i * 2 + 1), True, leg_colour)

	eyes(pos+point(0, 0, 19), leg_colour)
	
spider(OBSIDIAN, GOLD_BLOCK, point(0, 10, 0))
