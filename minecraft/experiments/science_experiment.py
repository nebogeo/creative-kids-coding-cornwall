from dbscode_minecraft import *

bulldoze()

def container(liquid,p,flip):
	# cup of tea made from melon
	cylinder(MELON,p+point(0,0,0),5,10)
	cylinder(AIR,p+point(0,0,0),4,10)
	cylinder(liquid,p+point(0,0,0),4,10)  

	xf=1  
	if flip: xf=-1
	
	box(STONE_BRICK,p+point(xf*4,0,-2),point(xf*3,8,5))
	box(AIR,p+point(xf*5,7,-1),point(xf*5,1,3))
	box(STONE_BRICK,p+point(xf*4,0,-6),point(xf*8,6,13))


container(LAVA,point(0,0,0),False)
container(WATER,point(25,0,0),True)
sphere(AIR,point(12,6,0),6)
box(AIR,point(4,9,-1),point(1,1,3))
box(AIR,point(21,9,-1),point(1,1,3))
