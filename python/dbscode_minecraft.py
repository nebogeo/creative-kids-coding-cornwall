# Minecraft API wrapper for dBsCode taster course

import sys

# locate api so we can run frm anywhere
sys.path.append("/home/pi/mcpi/api/python/mcpi")

import minecraft
from block import *
import math
import random
from vec3 import Vec3

mc = minecraft.Minecraft.create()
point = Vec3

def debug(msg):
	mc.postToChat(msg)

def my_pos():
	t = mc.player.getPos()
	return point(t.x,t.y,t.z)

def move_me_to(p):
	mc.player.setPos(p)

def read_block(p):
	mc.getBlock(p)
	
def write_block(blocktype,p):
	mc.setBlock(p.x,p.y,p.z,blocktype)

def box(t,pos,size):
	mc.setBlocks(pos.x,pos.y,pos.z,
				pos.x+size.x-1,pos.y+size.y-1,
				pos.z+size.z-1,
				t)
	#for y in reversed(range(0,int(size.y))):
	#	for z in range(0, int(size.z)):
	#		for x in range(0, int(size.x)):
	#			write_block(t,point(pos.x+x,pos.y+y,pos.z+z))

def sphere(t,pos,radius):
	radius=int(radius)
	for y in range(-radius, radius):
		for z in range(-radius, radius):
			for x in range(-radius, radius):
				if math.sqrt(x*x+y*y+z*z)<radius:
					write_block(t,point(pos.x+x,pos.y+y,pos.z+z))   

def cylinder(t,pos,radius,height):
	radius=int(radius)
	height=int(height)
	for y in range(0, height):
		for z in range(-radius, radius):
			for x in range(-radius, radius):
				if math.sqrt(x*x+z*z)<radius:
					write_block(t,point(pos.x+x,pos.y+y,pos.z+z))   

def cone(t,pos,radius,height):
	radius=int(radius)
	height=int(height)
	for y in range(0, height):
		for z in range(-radius, radius):
			for x in range(-radius, radius):
				if math.sqrt(x*x+z*z)<(radius*(1-y/float(height))):
					write_block(t,point(pos.x+x,pos.y+y,pos.z+z))   


def toblerone(t,pos,size):
	for y in reversed(range(0,int(size.y))):
		for z in range(0, int(size.z)):
			for x in range(0, int(size.x)):
				a = size.x*(1-y/float(size.y))*0.5
				if x>size.x/2.0-a and x<a+size.x/2.0:
					write_block(t,point(pos.x+x,pos.y+y,pos.z+z))


def mag(p):
	return math.sqrt(p.x*p.x+p.y*p.y+p.z*p.z)

def distance(a,b):
	return mag(a-b)
	
def random_point(a,b):
	return point(random.randrange(a.x,b.x),
				 random.randrange(a.y,b.y),
				 random.randrange(a.z,b.z))

def choose(l):
	return l[random.randint(0,len(l)-1)]

def i_am_lost():
	move_me_to(point(0,20,0))

def bulldoze(size,height):
	print("bulldozing")
	mc.setBlocks(-size/2,0,-size/2,size/2,height,size/2,AIR)
	box(GRASS,point(-size/2,-1,-size/2),point(size,1,size))
	print("finished bulldozing")


def planet(pos,size):
	sphere(DIAMOND_BLOCK,pos,size)  
	sphere(REDSTONE_ORE,pos,size*0.5)
	sphere(WOOD,pos,size*0.2)  
	box(AIR,pos+point(0,-size,0),pos+point(size,size,size)) 

#bulldoze(200,200)

#box(GOLD_BLOCK,point(20,0,0),point(4,4,4))
#cone(GOLD_BLOCK,point(10,0,0),5,10)
#sphere(GOLD_BLOCK,point(0,5,0),4)
#cylinder(GOLD_BLOCK,point(-10,0,0),4,8)#
#toblerone(GOLD_BLOCK,point(-24,0,0),point(8,8,4))

def house(roof,walls,size,pos,flip):
	box(AIR,pos,point(10,22,10))
	toblerone(roof,pos+point(0,5+size,0),point(10,6,8))
	toblerone(AIR,pos+point(0,3+size,0),point(10,6,8))
	box(walls,pos+point(2,0,1),point(7,7+size,6))
	box(walls,pos+point(4,7+size,1),point(3,2,6))
	box(AIR,pos+point(3,0,2),point(5,7+size,4))
	doorpos=6
	if flip:
		doorpos=1
	box(AIR,pos+point(4,0,doorpos),point(3,4,1))

def street(pos,length,side):
	for i in range(0,10):
		house(choose([MELON,GOLD_BLOCK,WOOD,COBBLESTONE]),
			choose([BRICK_BLOCK,COBBLESTONE,BEDROCK,SANDSTONE,LAPIS_LAZULI_BLOCK]),
			random.randint(-3,5),pos+point(-40+i*10,0,-15),
			side)

street(point(0,0,0),6,True)
street(point(0,0,-20),6,False)

#toblerone(WOOD,point(30,0,0),point(20,10,10))
#toblerone(AIR,point(30,-1,0),point(20,10,10))

#i_am_lost()
#cylinder(MELON,point(0,0,0),5,10)
#cylinder(AIR,point(0,0,0),4,10)
#cylinder(WATER,point(0,0,0),4,8)  

#box(AIR,point(0,0,0),point(20,20,20))
