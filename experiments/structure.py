from dbscode_minecraft import *
bulldoze()

def branch(chance,pos,d,depth):
	if random_range(0,100)<chance:
		tree(pos,point(depth*8*d.x,
                               depth*8*d.y,
                               depth*8*d.z),depth-1)

def tree(pos,d,depth):
	if depth>0:
		box(AIR,pos,d+point(depth*3,depth*3,depth*3))
		branch(50,pos+d,point(1,0,0),depth)
		branch(50,pos+d,point(-1,0,0),depth)
		branch(50,pos+d,point(0,0,1),depth)
		branch(50,pos+d,point(0,0,-1),depth)
		branch(25,pos+d,point(0,-1,0),depth)

#i_am_lost()
#box(SANDSTONE,point(-100,0,-100),point(200,-200,200))
tree(point(0,0,0),point(0,5,0),5)
