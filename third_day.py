"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways 
and office furniture that makes up this part of Easter Bunny HQ. This must be 
a graphic design department; the walls are covered in specifications for 
triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, 
but... 5 10 25? Some of these aren't triangles. You can't help but mark the 
impossible ones.

In a valid triangle, the sum of any two sides must be larger than the 
remaining side. For example, the "triangle" given above is impossible, 
because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?

--- Part Two ---

Now that you've helpfully marked up their design documents, it occurs to you that 
triangles are specified in groups of three vertically. Each set of three 
numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same 
hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
In your puzzle input, and instead reading by columns, how many of the 
listed triangles are possible?

"""
import numpy as np 

def is_triangle(full_input, a, b, c):
	valid_inputs = full_input[:, a] + full_input[:, b] > full_input[:,c]
	return full_input[valid_inputs]

def num_valid_triangles(full_input):
	sub_input = is_triangle(full_input, 0, 1, 2)
	sub_input = is_triangle(sub_input, 1, 2, 0)
	sub_input = is_triangle(sub_input, 0, 2, 1)
	return sub_input.shape[0]

def groups_of_3(full_input, a):
	return full_input[:,a].reshape(full_input.shape[0]/3, 3)

def main():
	full_input = np.loadtxt('input3.txt')
	print('Answer 1: Num of valid traingles are %d' %\
	 num_valid_triangles(full_input))

	num_triangles = 0
	for i in xrange(3):
		tri_stack = groups_of_3(full_input, i)
		num_triangles += num_valid_triangles(tri_stack)
	print('Answer 2: %d' % num_triangles)


if __name__ == "__main__":
	main()


