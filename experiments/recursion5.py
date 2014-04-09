from dbscode_minecraft import *
bulldoze()

def tree(pos,d,count):
	if count>0:
		box(SANDSTONE,pos,d+point(1,1,1))
		tree(pos+d,point(-2,0,0),count-1)
		tree(pos+d,point(2,0,0),count-1)
		tree(pos+d,point(0,2,0),count-1)

tree(point(0,0,0),point(0,1,0),5)



