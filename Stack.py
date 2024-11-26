from random import shuffle, randint
from math import ceil
from time import time

class structure:
	def __init__(self, capacity = None):
		self.items = []
		self.capacity = capacity


	def isEmpty(self):
		return len(self.items) == 0

	def isFull(self):
		if self.capacity == None:
			return False

		return len(self.items) >= self.capacity


	def push(self, item):
		if self.isFull():
			errorMessage = 'cannot push to a full ' + self.type
			raise OverflowError(errorMessage)

		self.items.append(item)


	def size(self):
		return len(self.items)


	def print(self):
		for i in range(len(self.items)):
			print(self.items[i], end = ' ')



class basic_list(structure):
	def __init__(self, capacity = None):
		self.type = 'basic_list'
		super().__init__(capacity)


	def __quicksortArray__(self, arr):
		if len(arr) <= 1:
			return arr

		else:
			pivot = arr[0]
			left = [x for x in arr[1:] if x < pivot]
			right = [x for x in arr[1:] if x >= pivot]
			return self.__quicksortArray__(left) + [pivot] + self.__quicksortArray__(right)

	def __mergesortArray__(self, arr):
		if len(arr) > 1:
			mid = len(arr)//2
			sub_array1 = arr[:mid]
			sub_array2 = arr[mid:]
			self.__mergesortArray__(sub_array1)
			self.__mergesortArray__(sub_array2)
			i = j = k = 0
			while i < len(sub_array1) and j < len(sub_array2):
				if sub_array1[i] < sub_array2[j]:
					arr[k] = sub_array1[i]
					i += 1

				else:
					arr[k] = sub_array2[j]
					j += 1

				k += 1

			while i < len(sub_array1):
				arr[k] = sub_array1[i]
				i += 1
				k += 1

			while j < len(sub_array2):
				arr[k] = sub_array2[j]
				j += 1
				k += 1

		return arr



	def bubble_sort(self):
		while True:
			switches = 0
			for i in range(len(self.items) - 1):
				if self.items[i] > self.items[i + 1]:
					temp = self.items[i]
					self.items[i] = self.items[i + 1]
					self.items[i + 1] = temp
					switches += 1

			if switches == 0:
				return self.items

	def insertion_sort(self):
		sortedArray = []
		for i in range(len(self.items)):
			inserted = False
			for j in range(len(sortedArray)):
				if self.items[i] < sortedArray[j]:
					sortedArray.insert(j, self.items[i])
					inserted = True
					break

			if not inserted:
				sortedArray.append(self.items[i])

		self.items = sortedArray
		return sortedArray

	def quicksort(self):
		self.items = self.__quicksortArray__(self.items)
		return self.items

	def mergesort(self):
		self.items = self.__mergesortArray__(self.items)
		return self.items

	def bogosort(self):
		sorted = False
		while sorted == False:
			sorted = True
			shuffle(self.items)
			for i in range(len(self.items) - 1):
				if not self.items[i] <= self.items[i + 1]:
					sorted = False
					break

		return self.items



	def linearsearch(self, item):
		length = len(self.items)
		for i in range(ceil(length / 2)):
			k = length - i - 1
			if self.items[i] == item or self.items[k] == item:
				if self.items[i] == item:
					return i

				else:
					return k

		return None

	def binarysearch(self, item):
		low = mid = 0
		high = len(self.items) - 1
		while low <= high:
			mid = (high + low) // 2
			if self.items[mid] < item:
				low = mid + 1

			elif self.items[mid] > item:
				high = mid - 1

			else:
				return mid
	 
		return None

	def bogosearch(self, item):
		while True:
			i = randint(0, len(self.items) - 1)
			if self.items[i] == item:
				return i



class stack(basic_list):
	def __init__(self, capacity = None):
		self.type = 'stack'
		super().__init__(capacity)


	def pop(self):
		if self.isEmpty():
			errorMessage = 'cannot pop from a empty ' + self.type
			raise OverflowError(errorMessage)

		return self.items.pop()


	def peek(self):
		if self.isEmpty():
			errorMessage = 'cannot peek from a empty ' + self.type
			raise OverflowError(errorMessage)
		
		return self.items[-1]			



class queue(basic_list):
	def __init__(self, capacity = None):
		self.type = 'queue'
		super().__init__(capacity)


	def pop(self):
		if self.isEmpty():
			errorMessage = 'cannot pop from a empty ' + self.type
			raise OverflowError(errorMessage)

		return self.items.pop(0)


	def peek(self):
		if self.isEmpty():
			errorMessage = 'cannot peek from a empty ' + self.type
			raise OverflowError(errorMessage)

		return self.items[0]
			


class linked_list(structure):
	def __init__(self, capacity = None):
		self.type = 'linkedList'
		super().__init__(capacity)
		self.pointers = [] 
		self.start = None


	def __find_next__(self):
		for i in range(len(self.items)):
			if self.items[i] == None:
				return i

		self.items.append(None)
		self.pointers.append(None)
		return len(self.items) - 1


	def push(self, item):
		if self.isFull():
			errorMessage = 'cannot push to a full ' + self.type
			raise OverflowError(errorMessage)

		newIndex = self.__find_next__()
		self.items[newIndex] = item
		if self.start == None:
			self.start = newIndex

		else:
			currentIndex = self.start
			while self.pointers[currentIndex] is not None:
				currentIndex = self.pointers[currentIndex]

			self.pointers[currentIndex] = newIndex


	def popIndex(self, index):
		if self.isEmpty():
			errorMessage = 'cannot pop from a empty ' + self.type
			raise OverflowError(errorMessage)
		
		current_index = self.start
		prev_index = None
		while current_index is not None:
			if current_index == index:
				if prev_index is None:
					self.start = self.pointers[current_index]

				else:
					self.pointers[prev_index] = self.pointers[current_index]

				temp = self.items[current_index]
				self.items[current_index] = None
				self.pointers[current_index] = None
				return temp
			
			prev_index = current_index
			current_index = self.pointers[current_index]

	def popItem(self, item):
		if self.isEmpty():
			errorMessage = 'cannot pop from a empty ' + self.type
			raise OverflowError(errorMessage)

		current_index = self.start
		prev_index = None
		while current_index is not None:
			if self.items[current_index] == item:
				if prev_index is None:
					self.start = self.pointers[current_index]

				else:
					self.pointers[prev_index] = self.pointers[current_index]

				temp = self.items[current_index]
				self.items[current_index] = None
				self.pointers[current_index] = None
				return temp

			prev_index = current_index
			current_index = self.pointers[current_index]

		errorMessage = 'item not found in ' + self.type
		raise OverflowError(errorMessage)


	def peekIndex(self, index):
		if self.isEmpty():
			errorMessage = 'cannot peek from a empty ' + self.type
			raise OverflowError(errorMessage)

		if (len(self.items) - 1) < index:
			errorMessage = 'cannot peek index outside of range in ' + self.type
			raise OverflowError(errorMessage)

		return self.items[index]

	def peekItem(self, item):
		if self.isEmpty():
			errorMessage = 'cannot peek from a empty ' + self.type
			raise OverflowError(errorMessage)
		
		if not item in self.items:
			errorMessage = 'cannot peek item not in ' + self.type
			raise OverflowError(errorMessage)


	def print(self):
		current_index = self.start
		while current_index is not None:
			print(self.items[current_index], end = ' ')
			current_index = self.pointers[current_index]

		return self.items.index(item)







testList = [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 
			10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
			20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
			30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 
			40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 
			50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 
			60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 
			70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 
			80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 
			90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
shuffle(testList)

test = stack()

for i in range (len(testList)):
	test.push(testList[i])
	


test.print()