from dbscode_minecraft import *
bulldoze()

def tree(pos,count):
	if count>0:
		box(SANDSTONE,pos,point(1,count,1))
		tree(pos+point(-2,count,0),count-1)
		tree(pos+point(2,count,0),count-1)
		tree(pos+point(0,count,-2),count-1)
		tree(pos+point(0,count,2),count-1)

tree(point(0,0,0),5)



