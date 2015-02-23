from dbscode_minecraft import *
bulldoze()

def chance(percent):
	return random_range(0,100)<percent

def tree(pos,d,count):
	if count>0:
		box(SANDSTONE,pos,d+point(count,count,count))
		if chance(50): tree(pos+d,point(-4*count,0,0),count-1)
		if chance(50): tree(pos+d,point(4*count,0,0),count-1)
		if chance(50): tree(pos+d,point(0,0,-4*count),count-1)
		if chance(50): tree(pos+d,point(0,0,4*count),count-1)
		if chance(50): tree(pos+d,point(0,4*count,0),count-1)

tree(point(0,0,0),point(0,1,0),7)


