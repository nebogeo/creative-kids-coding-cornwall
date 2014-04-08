# An infinite house generator

Before you start:

Launch Minecraft and create a new world.
Launch Geany

## Step 1 Make a roof

1 Open a new file, call this `house.py`.

2 We need to import the dBsCode commands we'll be using and clear an
area in the Minecraft world for working in. Create this program:

        from dbscode_minecraft import *
        bulldoze()

3 **Test** Press F5 to run the program (this will also save your
program for you). After a few seconds you should see a "flatworld" type
of environment.

4 Lets start with the roof. Build a prism by adding this to the end of your script:

        toblerone(WOOD,point(0,5,0),point(10,6,8))

5. **Test** Press F5 and navigate to the centre of the world (using the
coordinates at the top left of the Minecraft window). You should see a
toblerone shape. This shape is drawn from block position 0,5,0 and is of
size 10,6,8.

6. We now need to hollow out the shape we've just drawn in order to make
space for the walls:

        toblerone(AIR,point(0,3,0),point(10,6,8))

This shape has the same dimensions but drawn 2 blocks lower, and
as the material is set to AIR, it "cuts way" from the previous shape,
leaving a roof structure.

## Step 2 Build the walls

1. Add this line so it comes after the roof toblerones:

        box(BRICK_BLOCK,point(2,0,1),point(7,7,6))

2. Press F5 to check this - it fills the area below the roof but we have
a hole just underneath the top. We can fill this with another box:

        box(BRICK_BLOCK,point(4,7,1),point(3,2,6))

3. This house is not much good as it's solid, so we can hollow it out
with an air box in the middle:

        box(AIR,point(3,0,2),point(5,7,4))

4. You can check this worked by destroying a few bricks and breaking
in. Lets quickly add a door:

        box(AIR,point(4,0,1),point(3,4,1))

## Step 3 Make a house *function*

Functions are one of the founding principles of programming - they can
amplify your actions, and allow you to solve difficult problems by
breaking them into small ones.

We use 'def' to build functions. Collect together all the code you've
just written so it looks like this - the spaces at the start of the
lines are important - there are 4 of them:

        def house():
        	toblerone(WOOD,point(0,5,0),point(10,6,8))
        	toblerone(AIR,pos+point(0,3,0),point(10,6,8))
        	box(BRICK_BLOCK,pos+point(2,0,1),point(7,7,6))
        	box(BRICK_BLOCK,pos+point(4,7,1),point(3,2,6))
        	box(AIR,pos+point(3,0,2),point(5,7+size,4))
        	box(AIR,pos+point(4,0,1),point(3,4,1))

Now we can "call" this function by simply adding this to the bottom of your
program:

        house()
