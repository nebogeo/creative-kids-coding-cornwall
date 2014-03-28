# Minecraft API wrapper for dBsCode taster course

import sys

# locate api so we can run frm anywhere
sys.path.append("/home/pi/mcpi/api/python/mcpi")

import minecraft
import block
import math
import random

Vec3 = minecraft.Vec3
mc = minecraft.Minecraft.create()

mc.postToChat("hello")

def myPos():
	t = mc.player.getPos()
	return minecraft.Vec3(t.x,t.y,t.z)

def moveMeTo(p):
	mc.player.setPos(p)

def readBlock(p):
	mc.getBlock(p)
	
def writeBlock(p,blocktype):
	mc.setBlock(p.x,p.y,p.z,blocktype)

def writeCube(pos,size,t):
	for x in range(0, size.x):
		for y in range(0, size.y):
			for z in range(0, size.z):
				writeBlock(Vec3(pos.x+x,pos.y+y,pos.z+z),t)
	
def writeSphere(pos,radius,t):
	for x in range(-radius, radius):
		for y in range(-radius, radius):
			for z in range(-radius, radius):
				if math.sqrt(x*x+y*y+z*z)<radius:
					writeBlock(Vec3(pos.x+x,pos.y+y,pos.z+z),t)                                                                                          
	
def randPos(a,b):
	return Vec3(random.randrange(a.x,b.x),
				random.randrange(a.y,b.y),
				random.randrange(a.z,b.z))

#--------------------------------------------------------
# trying out some stuff
	
#setPos(Vec3(0,200,0))
   
pos = Vec3(0,-10,-68)

#moveMeTo(pos)

#for i in range(0,10):	
#	spos = randPos(Vec3(0,0,0),Vec3(20,1,20))
#	moveMeTo(pos+spos+Vec3(0,20,0))
#	writeSphere(pos+spos,15,0)

writeCube(pos,Vec3(100,20,100),0)

for x in range(0,10):
	for y in range(0,10):	
		spos = Vec3(x*8,5,y*8)
		moveMeTo(pos+spos+Vec3(0,20,0))
		writeSphere(pos+spos,3,20+x)






