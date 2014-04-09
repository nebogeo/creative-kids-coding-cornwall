# A Minecraft spider generator

![Spider](https://github.com/glenpike/dbscode/raw/master/doc/images/spider.jpg "A spider")

Before you start:

* Launch Minecraft and create a new world.
* Launch Geany

## Step 1 Make a body

* In Geany, from the file menu select "new", and then save as `spider.py` in the "pi"
  directory.

* We need to import the dBsCode commands we'll be using and clear an
area in the Minecraft world for working in. Create this program:

        from dbscode_minecraft import *
        bulldoze()

* **Test** Press F5 to run the program (this will also save your
program for you). After a few seconds you should see a "flatworld" type
of environment.

* Our spider will consist of a body, a head and some legs.

* Lets start with the body. Build a sphere by adding this to the end of your script:

	sphere(DIAMOND_BLOCK, point(0, 10, 0), 8)

* **Test** Press F5 and navigate to the centre of the world (using the 
coordinates at the top left of the Minecraft window).  You should see a
sphere shape.  This shape has it's centre at 0, 10, 0 and a radius of 8.
The diameter of the sphere is actually 15 blocks 2 smaller than 2 * radius,
remembering this maybe helpful later on.

* Not very exciting yet, lets add a head, we make it a bit smaller than the body:

	sphere(DIAMOND_BLOCK, point(0, 10, 8 + 6), 6)

* **Test** Press F5 and make sure there are 2 spheres drawn.  We've positioned
the smaller one in front of the large sphere by moving it's centre by the radius
of each sphere.  Can you see the gap?  Remember the diameter of a sphere is 2 blocks
less than the radius.  See if you can fix it.  The correct code is shown further on.

## Step 2 Make a leg

* Okay, we need to draw some legs, we could draw a line straight down, 
but let's give the spider some knees too.  We will draw a horizontal line out from the body
at point(8, 10, 0), this is 8 blocks long and one thick, point(8, 1, 1)

	box(OBSIDIAN, point(8, 10, 0), point(8, 1, 1))

* Then we draw a vertical line down. We position this underneath the last horizontal block
at point(15, 9, 0) and draw 7 blocks down using point(1, -7, 1)

	box(OBSIDIAN, point(15, 9, 0), point(1, -7, 1))

//Testme
## Step 3 Make a function for drawing legs

* But you need to draw 8 legs, 4 on each side.  This is where we can use something 
very useful in programming called a 'function'.
Functions let you write some code that you can use over and over again by 'calling'
the function repeatedly.

* You are going to write a function that draws the 2 boxes above.

* We use 'def' to build functions. Collect together the 2 lines beginning
with "box" that you've just written so it looks like this 
- the spaces at the start of the lines are important - there are 4 of them, 
or just press the "tab" key once:

	def leg():
		box(OBSIDIAN, point(8, 10, 0), point(8, 1, 1))
		box(OBSIDIAN, point(15, 9, 0), point(1, -7, 1))

		
Now we can "call" this function by simply adding this to the bottom of your
program.  Your code should now look something like this:

	def leg():
		box(OBSIDIAN, point(8, 10, 0), point(8, 1, 1))
		box(OBSIDIAN, point(15, 9, 0), point(1, -7, 1))


	sphere(DIAMOND_BLOCK, point(0, 10, 0), 8)
	sphere(DIAMOND_BLOCK, point(0, 10, 7 + 6), 6)
	leg()	
	
* Press F5 - your spider should appear with one leg, now we need to make
it draw the other 7.

* We can add a position "parameter" to the function. We use parameters
to pass information into a function by adding them to the brackets at
the top and refering to them inside. Change your existing function and
add "pos" to all of the positions of the shapes:

	def leg(pos):
		box(OBSIDIAN, pos, point(8, 1, 1))
		box(OBSIDIAN, pos+point(7, -1, 0), point(1, -7, 1))

* We can now pass in the position when we call the function to draw a leg
in any position. This will draw 4 legs on one side of the body, spaced apart by a block.

	leg(point(8, 10, 1))
	leg(point(8, 10, 3))
	leg(point(8, 10, 5))
	leg(point(8, 10, 7))

* Press F5 - your spider should appear with 4 legs on one side, but they may
be slightly out of position.  See if you can fix this.  (Remember the middle
of the sphere is at "0")

## Step 4 Loop the loop.

* Programmers are lazy...  We don't want to write the same thing over and over,
so we made functions, but we also made loops which allow us to do the same thing
over and over again, maybe changing one small thing.  See above where we make
4 legs - the only thing that changes is the last number (the "z" position) of the
leg.

* To do this we need a "for" loop.  Remove the 4 leg() "calls" and replace with this:

	for i in range(0, 4):
		leg(point(8, 10, i * 2))

* This will repeat the `leg` line 4 times (make sure you add 4 spaces
before), each time with i being a number described by the `range`
function - so 0 to 4 in this case. We set the z position of the leg
by multiplying this by 2 (so each house in the row appears spaced by 2
blocks)

* But the position is still wrong.  We can change our range above so that it
positions the legs with negative and positive z positions, change the above
for loop to do this:

	for i in range(-2, 2):
		leg(point(8, 10, i * 2 + 1))

* Press F5 to test again - your legs should now be positioned either side
of the vertical centre line of the sphere.



