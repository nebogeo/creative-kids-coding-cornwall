from dbscode_minecraft import *

bulldoze()

def leg(t, pos, size, flip):
	for y in range(0, size):
		x = min(y, size / 2)
		if(flip):
			x *= -1
		pt = point(pos.x + x, pos.y - y, pos.z)
		box(t, pt, point(1, 1, 1))

def eyes(t, pos):
	draw = True
	for x in range(-2, 3):
		for y in range(-1, 2):
			if True == draw:
				box(t, point(pos.x + x, pos.y + y, pos.z), point(1, 1, 1))
			draw = ~draw
			
def spider(t, leg_t, pos, size):
	head = int(size * 0.6)
	sphere(t, point(pos.x, pos.y, pos.z + 1 + size + head / 2), head)
	sphere(t, pos, size)
	for z in range(-2, 2):
		leg(leg_t, point(pos.x + size, pos.y, pos.z + 2 * z + 1), size, False)
		leg(leg_t, point(pos.x - size, pos.y, pos.z + 2 * z + 1), size, True)
	eyes(leg_t, point(pos.x, pos.y, pos.z - 2 + size + head * 2))

spider(choose_one(OBSIDIAN, GLOWING_OBSIDIAN, IRON_BLOCK), 
	choose_one(GOLD_BLOCK, LEAVES, DIAMOND_BLOCK), 
	point(0, 10, 0), 
	random_range(6, 8))
