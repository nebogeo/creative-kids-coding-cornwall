from dbscode_minecraft import *
bulldoze()

def row(pos,count):
	if count>0:
		box(SANDSTONE,pos,point(1,1,1))
		row(pos+point(3,0,0),count-1)

row(point(0,0,0),5)



