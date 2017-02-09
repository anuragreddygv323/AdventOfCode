"""
You're airdropped near Easter Bunny Headquarters in a city somewhere. 
"Near", unfortunately, is as close as you can get - the instructions on the
Easter Bunny Recruiting Document the Elves intercepted start here, and
nobody had time to work them out further.

The Document indicates that you should start at the given coordinates
(where you just landed) and face North. Then, follow the provided sequence: 
either turn left (L) or right (R) 90 degrees, then walk forward the given 
number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, 
so you take a moment and work out the destination. Given that you can only 
walk on the street grid of the city, how far is the shortest path to the 
destination?


--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?

"""

import numpy as np

class Walk(object):
	"""
	A class that keeps updating coordinates as you walk in a city grid
	"""
	
	def __init__(self, bearing = 'N'):
		self.distance = 0
		self.direction = None  
		self.bearing = bearing
		self.coordinates = (0,0)
		self.compass = 'NESW'	

	def parse_location(self, direction):
		"""
		Extracts the directions from an instruction.
		If the instruction is L1, it returns 
		lr : 'L' or 'R' left or right direction
		num_blocks: how many blocks to walk
		"""
		self.direction = direction
		lr = self.direction[0]
		num_blocks = int(self.direction[1:])
		return lr, num_blocks

	def move(self, num_blocks):
		"""
		Depending on the bearing and the current coordinates, it moves the
		stated number of blocks and updates the current coordinates
		"""
		x, y = self.coordinates[0], self.coordinates[1]
		if self.bearing == 'N':
			y += num_blocks 
		elif self.bearing == 'S':
			y -= num_blocks
		elif self.bearing == 'E':
			x += num_blocks
		elif self.bearing == 'W':
			x -= num_blocks
		self.coordinates = (x,y)

	def update_bearing(self, lr):
		"""
		Given a direction, it updates bearing and initiates a move
		"""
		index = self.compass.index(self.bearing)
		if lr == 'L':
			index -= 1
			self.bearing = self.compass[index]
		elif lr == 'R':
			index += 1
			if index > (len(self.compass)-1):
				index = 0
			self.bearing = self.compass[index]

	def taxi_cab_distance(self):
		"""
		Calculates the taxi_cab_distance which, it the origin is (0,0)
		is |x|+|y|
		"""
		self.distance = np.absolute(self.coordinates[0]) +\
		np.absolute(self.coordinates[1])
		return self.distance

	def get_coordinates(self):
		return self.coordinates

	def __repr__(self):
		print("You are at (%d, %d)" % self.coordinates)

def calc_distance_to_HQ(inplist):
	walk = Walk()
	for direction in inplist:
		lr, num_blocks = walk.parse_location(direction)
		walk.update_bearing(lr)
		walk.move(num_blocks)
	distance = walk.taxi_cab_distance()
	print('Easter bunny HQ is %d blocks away' % distance)


def first_repeated_position(inplist):
	walk = Walk()
	old_coords = (0,0)
	coords = [old_coords]
	for direction in inplist:
		lr, num_blocks = walk.parse_location(direction)
		walk.update_bearing(lr)
		for i in xrange(num_blocks):
			walk.move(1)
			current_coords = walk.get_coordinates()
			#print direction, current_coords
			if current_coords in coords:
				distance = walk.taxi_cab_distance()
				return distance
			coords.append(current_coords)
	


def main():
	inp = "R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5"
	#inp = 'R8, R4, R4, R8'
	inplist = inp.split(', ')
	calc_distance_to_HQ(inplist)
	distance = first_repeated_position(inplist)
	print('first location you visit twice is %d away' % distance)


if __name__ == '__main__':
	main()




			



