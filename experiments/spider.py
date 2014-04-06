from dbscode_minecraft import *

bulldoze()

def leg(t, pos, size, flip):
	for y in range(0, size):
		x = min(y, size / 2)
		if(flip):
			x *= -1
		pt = point(pos.x + x, pos.y - y, pos.z)
		write_block(t, pt)
		#write_block(t, point(pos.x + 2, pos.y - 4, pos.z))
	
def spider(t, leg_t, pos):
	size = 8
	head = int(size * 0.6)
	#eyes - fixme - draw 1 depth box, punch out with head except corners,
	#repeat with box-size - 1 to create 8 blocks.
	eye_size = 2 * (head - 1) #eek rounding errors.
	#position is wrong centres vs corners, yuck.
	#box(leg_t, point(pos.x - head, pos.y - head, pos.z + size + head), point(eye_size, eye_size, 1))
	sphere(t, pos, size)
	sphere(t, point(pos.x, pos.y, pos.z + size + head / 2), head)
	for z in range(-2, 2):
		leg(leg_t, point(pos.x + size, pos.y, pos.z + 2 * z), size, False)
		leg(leg_t, point(pos.x - size, pos.y, pos.z + 2 * z), size, True)
	
spider(OBSIDIAN, GOLD_BLOCK, point(0, 10, 0))
	
