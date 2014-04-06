from dbscode_minecraft import *

bulldoze()

def battlement_x(p, length, height):
	box(STONE_BRICK,p,point(length,height,1))
	box(STONE_BRICK,p+point(0,height,-1),point(length,2,3))
	for i in range(0,length/2):
		box(STONE_BRICK,p+point(i*2,height+2,-1),point(1,1,3))

def battlement_y(p, length, height):
	box(STONE_BRICK,p,point(1,height,length))
	box(STONE_BRICK,p+point(-1,height,0),point(3,2,length))
	for i in range(0,length/2):
		box(STONE_BRICK,p+point(-1,height+2,i*2),point(3,1,1))

def walls(p,size):
	battlement_x(p,size.x, size.y)
	battlement_y(p,size.z, size.y)
	battlement_x(p+point(0,0,size.z),size.x, size.y)
	battlement_y(p+point(size.x,0,0),size.z, size.y)

def tower(p,height):
	walls(p,point(5,height,5))


def c(p,size):
	walls(p,size)
	tower(p,size.y*2)	

c(point(0,0,0),point(15,5,15))
