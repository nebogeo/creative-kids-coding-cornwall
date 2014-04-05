import dbscode_minecraft

def planet(pos,size):
	sphere(DIAMOND_BLOCK,pos,size)  
	sphere(REDSTONE_ORE,pos,size*0.5)
	sphere(WOOD,pos,size*0.2)  
	box(AIR,pos+point(0,-size,0),pos+point(size,size,size)) 

#bulldoze(200,200)

#box(GOLD_BLOCK,point(20,0,0),point(4,4,4))
#cone(GOLD_BLOCK,point(10,0,0),5,10)
#sphere(GOLD_BLOCK,point(0,5,0),4)
#cylinder(GOLD_BLOCK,point(-10,0,0),4,8)#
#toblerone(GOLD_BLOCK,point(-24,0,0),point(8,8,4))

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

#toblerone(WOOD,point(30,0,0),point(20,10,10))
#toblerone(AIR,point(30,-1,0),point(20,10,10))

#i_am_lost()
#cylinder(MELON,point(0,0,0),5,10)
#cylinder(AIR,point(0,0,0),4,10)
#cylinder(WATER,point(0,0,0),4,8)  

#box(AIR,point(0,0,0),point(20,20,20))
