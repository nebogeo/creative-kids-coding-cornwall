from dbscode_minecraft import *

# what happens when you chop a planet up

bulldoze()

def planet(pos,size):
	sphere(DIAMOND_BLOCK,pos,size)  
	sphere(LAVA,pos,size*0.75)
	sphere(WOOD,pos,size*0.3)  
	box(AIR,pos+point(0,-size,0),pos+point(size,size,size)) 
	
planet(point(0,10,0),10)

