from dbscode_minecraft import *

bulldoze()

current_brick = STONE_BRICK

def battlement_x(p, length, height):
	box(current_brick,p,point(length,height,1))
	box(current_brick,p+point(0,height,-1),point(length,2,3))
	for i in range(0,length/2):
		box(current_brick,p+point(i*2,height+2,-1),point(1,1,3))

def battlement_y(p, length, height):
	box(current_brick,p,point(1,height,length))
	box(current_brick,p+point(-1,height,0),point(3,2,length))
	for i in range(0,length/2):
		box(current_brick,p+point(-1,height+2,i*2),point(3,1,1))

def walls(p,size):
	battlement_x(p,size.x, size.y)
	battlement_y(p,size.z, size.y)
	battlement_x(p+point(0,0,size.z),size.x, size.y)
	battlement_y(p+point(size.x,0,0),size.z, size.y)

def tower(p,height):
	walls(p,point(5,height,5))

  
def castle(p,size):
	walls(p,size)
	tower(p+point(-2,0,-2),size.y*2)	
	tower(p+point(size.x-2,0,size.z-2),size.y*2)	
	tower(p+point(-2,0,size.z-2),size.y*2)	
	tower(p+point(size.x-2,0,-2),size.y*2)	

current_brick=SANDSTONE
castle(point(0,0,0),point(40,2,40))
current_brick=GLASS
castle(point(8,0,8),point(24,5,24))
current_brick=IRON_BLOCK
castle(point(15,0,15),point(10,8,10))
