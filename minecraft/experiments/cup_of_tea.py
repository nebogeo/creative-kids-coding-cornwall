from dbscode_minecraft import *

bulldoze()

# cup of tea made from melon
cylinder(MELON,point(0,0,0),5,10)
cylinder(AIR,point(0,0,0),4,10)
cylinder(NETHER_REACTOR_CORE,point(0,0,0),4,10)  

box(STONE_BRICK,point(4,0,-2),point(3,8,5))
box(STONE_BRICK,point(4,0,-2),point(5,5,5))
box(STONE_BRICK,point(4,0,-2),point(8,2,5))

box(AIR,point(4,9,0),point(1,1,1))
