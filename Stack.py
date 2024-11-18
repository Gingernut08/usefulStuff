class structure:
	def __init__(self, capacity = None):
		self.items = [None] * capacity
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
		self.items.append(str(item))

	def size(self):
		return len(self.items)

	def print(self):
		print(', '.join(self.items))

class stack(structure):
	def __init__(self, capacity = None):
		self.type = 'stack'
		super().__init__(capacity)

	def pop(self):
		if not self.isEmpty():
			return self.items.pop()
		else:
			errorMessage = 'cannot pop from a empty ' + self.type
			raise OverflowError(errorMessage)

	def peek(self):
		if not self.isEmpty():
			return self.items[-1]
		else:
			errorMessage = 'cannot peek from a empty ' + self.type
			raise OverflowError(errorMessage)

class queue(structure):
	def __init__(self, capacity = None):
		self.type = 'queue'
		super().__init__(capacity)

	def pop(self):
		if not self.isEmpty():
			return self.items.pop(0)
		else:
			errorMessage = 'cannot pop from a empty ' + self.type
			raise OverflowError(errorMessage)

	def peek(self):
		if not self.isEmpty():
			return self.items[0]
		else:
			errorMessage = 'cannot peek from a empty ' + self.type
			raise OverflowError(errorMessage)








class linked_list(structure):
	def __init__(self, capacity = 128):
		super().__init__(capacity)
		self.type = 'linked_list'
		self.pointer = [None] * capacity
		self.length = 0
		self.nextFree = 0

		self.start = 0
		self.end = 0


	def next_free(self):
		for i in range(len(self.items)):
			if self.items[i] == None:
				return i

	def push(self, item):
		self.nextFree = self.next_free()
		temp = self.nextFree

		if self.pointer[temp + 1] != None:
			self.pointer[temp] = temp + 1
		else:
			self.pointer[temp] = None
		self.items[self.nextFree] = item

		self.end += 1
		self.length += 1
		



test = linked_list(10)
test.push(10)
test.push(9)
test.push(8)
print(test.items)
print(test.pointer)


#print(self.items[self.start])
#for i in range(length - 1):
#	temp = self.pointer[i]
#	print(self.items[temp])
