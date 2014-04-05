# functions

###debug("hello")

Sends "hello" to the Minecraft chat. Useful for debugging your programs.

###bulldoze()

Flattens a large area in the middle of the world for you to work on.  A
good idea to call this all the time, so the world is cleared before you
run your program.



## primitives

###box(blocktype, postion_point, size_point)
###box(CLAY, point(0,0,0), point(10,10,10))

Will create a 10x10x10 block of clay in the middle of the world (0,0,0)

###sphere(blocktype, centre_point, radius)
###sphere(MELON, point(0,10,0), 10)

Will create a sphere of melon slightly above the centre of the world
with a radius of 10 blocks.




## maths

point(x,y,z) : returns a new point

Points can be added or substracted eg:
newpoint = point(10,0,2) + point(1,2,3)

Will result in newpoint containing x=11 y=2 z=5

# block types

AIR
STONE
GRASS
DIRT
COBBLESTONE
WOOD_PLANKS
SAPLING
BEDROCK
WATER_FLOWING
WATER
WATER_STATIONARY
LAVA_FLOWING
LAVA
LAVA_STATIONARY
SAND
GRAVEL
GOLD_ORE
IRON_ORE
COAL_ORE
WOOD
LEAVES
GLASS
LAPIS_LAZULI_ORE
LAPIS_LAZULI_BLOCK
SANDSTONE
BED
COBWEB
GRASS_TALL
WOOL
FLOWER_YELLOW
FLOWER_CYAN
MUSHROOM_BROWN
MUSHROOM_RED
GOLD_BLOCK
IRON_BLOCK
STONE_SLAB_DOUBLE
STONE_SLAB
BRICK_BLOCK
TNT
BOOKSHELF
MOSS_STONE
OBSIDIAN
TORCH
FIRE
STAIRS_WOOD
CHEST
DIAMOND_ORE
DIAMOND_BLOCK
CRAFTING_TABLE
FARMLAND
FURNACE_INACTIVE
FURNACE_ACTIVE
DOOR_WOOD
LADDER
STAIRS_COBBLESTONE
DOOR_IRON
REDSTONE_ORE
SNOW
ICE
SNOW_BLOCK
CACTUS
CLAY
SUGAR_CANE
FENCE
GLOWSTONE_BLOCK
BEDROCK_INVISIBLE
STONE_BRICK
GLASS_PANE
MELON
FENCE_GATE
GLOWING_OBSIDIAN
NETHER_REACTOR_CORE
