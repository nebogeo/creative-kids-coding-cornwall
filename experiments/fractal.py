from dbscode_minecraft import *
bulldoze()

def tree(pos,size):
	if size>0:
		box(SANDSTONE ,pos,point(3,2,size))
		box(AIR,pos+point(1,1,1),point(1,1,size))
		tree(pos+point(1,-1,size),size-1)
		tree(pos+point(-1,-1,size),size-1)

tree(point(0,6,0),7)
box(WATER,point(1,8,1),point(1,1,1))



