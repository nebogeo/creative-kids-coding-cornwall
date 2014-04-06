# Copyright (C) 2014 Dave Griffiths for dBsCode
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

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
	mc.postToChat(str(msg))

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

def random_range(a,b):
	return random.randint(a,b)

def choose_one(*argv):
	return argv[random.randint(0,len(argv)-1)]

def i_am_lost():
	move_me_to(point(0,20,0))

def bulldoze():
	size=100
	height=100
	print("bulldozing")
	mc.setBlocks(-size/2,0,-size/2,size/2,height,size/2,AIR)
	box(GRASS,point(-size/2,-1,-size/2),point(size,1,size))
	print("finished bulldozing")
