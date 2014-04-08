# Make a street of houses

Before you start:

Launch Minecraft and create a new world.
Launch Geany

## Step 1

1. Open a new file, call this `house.py` 2. First we need to import the
dBsCode commands we'll be using and clear an area in the Minecraft world
for working in. Create this program:

    from dbscode_minecraft import *
    bulldoze()

3. **Test** Press F5 to run the program (this will also save your
program for you). After a few seconds you should see a "flatworld" type
of environment.

4. Build a cube by adding this to the end of your script:

    box(BRICK_BLOCK,point(0,0,0),point(10,10,10))

5. **Test** Press F5 and navigate to the centre of the world (using the
coordinates at the top left of the Minecraft window). You should see a
cube of bricks.

## Step 2
