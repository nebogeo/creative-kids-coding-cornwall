from dbscode_minecraft import *

bulldoze()

def house(roof,walls,size,pos,flip):
	box(AIR,pos,point(10,22,10))
	toblerone(roof,pos+point(0,5+size,0),point(10,6,8))
	toblerone(AIR,pos+point(0,3+size,0),point(10,6,8))
	box(walls,pos+point(2,0,1),point(7,7+size,6))
	box(walls,pos+point(4,7+size,1),point(3,2,6))
	box(AIR,pos+point(3,0,2),point(5,7+size,4))
	doorpos=6
	if flip: doorpos=1
	box(AIR,pos+point(4,0,doorpos),point(3,4,1))

def street(pos,length,side):
	for i in range(0,10):
		house(choose_one(MELON,GOLD_BLOCK,WOOD,COBBLESTONE),
			choose_one(BRICK_BLOCK,COBBLESTONE,BEDROCK,SANDSTONE,LAPIS_LAZULI_BLOCK),
			random_range(-3,5),pos+point(-40+i*10,0,-15),
			side)

street(point(0,0,0),6,True)
street(point(0,0,-20),6,False)

