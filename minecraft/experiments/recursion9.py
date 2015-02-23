from dbscode_minecraft import *
bulldoze()

def chance(percent):
	return random_range(0,100)<percent

def tree(pos,d,count):
	if count>0:
		box(AIR,pos,d+point(count,count,count))
		if chance(50): tree(pos+d,point(-4*count,0,0),count-1)
		if chance(50): tree(pos+d,point(4*count,0,0),count-1)
		if chance(50): tree(pos+d,point(0,0,-4*count),count-1)
		if chance(50): tree(pos+d,point(0,0,4*count),count-1)
		if chance(50): tree(pos+d,point(0,-4*count,0),count-1)

box(SANDSTONE,point(-100,-101,-100),point(200,100,200))
tree(point(0,0,0),point(0,-5,0),5)


