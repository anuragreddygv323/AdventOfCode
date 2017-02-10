"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. 
Of course, the list is encrypted and full of decoy data, but the 
instructions to decode the list are barely hidden nearby. 
Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) 
followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters 
in the encrypted name, in order, with ties broken by alphabetization. 
For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters 
are a (5), b (3), and then a tie between x, y, and z, which are listed 
alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters 
are all tied (1 of each), the first five are listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.
Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?

"""
import re
class EncryptedName(object):
	def __init__(self):
		self.name = None
		self.sector_id = None
		self.checksum = None
		self.name_list = None

	def read_encryption(self, filename):
		name_list = filename.split('-')
		self.name_list = name_list[:-1]
		self.name = '-'.join(self.name_list)

		self.sector_id = re.findall("\d+", filename)[0]
		last_word = name_list[-1]

		self.checksum = last_word[last_word.find('[')+1:last_word.find(']')]

	def get_valid_sector_id(self):
		numbers = []
		num = 1000
		prev_letter = ''
		for idx, letter in enumerate(self.checksum):
			count = self.name.count(letter)
			if count <= num:
				numbers.append(count)
				if (num == count):
					if prev_letter > letter:
						return 0
				num = count
				prev_letter = letter
			else:
				return 0
		return int(self.sector_id)

def main():
	test_input = ['aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', \
	'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]']
	file = open('input4.txt', 'r') 

	ename = EncryptedName()
	sumz = 0
	for name in file.readlines():
		ename.read_encryption(name)
		number = ename.get_valid_sector_id()
		sumz += number

	print('sum of the sector IDs of the real rooms is %d' % sumz)

if __name__ == "__main__":
	main()


#file = open('input4.txt', 'r') 
#for line in file.readlines(): 
