class Node:
	def __init__(self, elm):
		self.elm = elm
		self.next = []
		self.id = []

	def getElm(self):
		return self.elm

	def addNext(self, next):
		self.next.append(next)

	def getNext(self, i):
		return self.next[i]

	def addId(self, newId):
		self.id.append(newId)

	def checkId(self, i):
		return i in self.id

	"""
	def checkElm(self, elm):
		return self.elm == elm
	"""
class List:
	def __init__(self):
		self.root = None
		self.id = 0
		self.first = False
		self.bestMatchIndex = []
		self.countMatch = []

	def addFirstTime(self, elm):
		if (self.root == None):
			self.root = Node(elm)
			self.root.addId(self.id)
			return

		node = self.root
		t = False
		while (not t):
			if not node.next:
				#list empty
				node.addNext(Node(elm))
				node.next[0].addId(self.id) #Do it general
				t = True
			else:
				#list not empty
				node = node.getNext(self.id)

	def checkForSimilarity(self, word, temp):
		index = 0
		while (temp != None):
			temp2 = temp
			
			count = 0
			for i in range(len(word)):
				if (word[i] == temp2.getElm()):
					count += 1

					if (not temp2.next):
						if (count != 0):
							self.bestMatchIndex.append(index)
							self.countMatch.append(count)
						return

					temp2 = temp2.next[0]
				else:
					if (count != 0):
						self.bestMatchIndex.append(index)
						self.countMatch.append(count)
					break

			if (not temp.next):
				break

			if (temp.next[0] != None): #Do it general
				index += 1
				temp = temp.next[0]

	def bestSimilarity(self, index, values):
		bestIndex = 0
		bestValue = 0

		for i in range(len(index)):
			if (values[i] > bestValue):
				bestValue = values[i]
				bestIndex = index[i]

		return bestIndex, bestValue

	def chainNodes(self, index, value, newId, word):
		#['h', 'u', 'r', 'r', 'a', 'm', 'e', 'g', h', 'e', 'i']
		temp = self.root
		
		#Get to the start position
		for i in range(index):
			temp = temp.next[0] #Do it general

		count = 0
		lastPointer = None
		#Link the first matches nodes together
		while (temp != None and count < value):
			temp.addId(newId)
			lastPointer = temp
			#print temp.getElm(), temp.id
			
			if (not temp.next):
				break

			if (temp.next[0] != None): #Do it general
				#print count, temp.getElm()
				temp = temp.next[0]

			count += 1

		#print "Last:", lastPointer.getElm()

		#Chain the remaining nodes
		finishChain = False

		while (temp != None):
			if (value >= len(word)):
				#print value
				return

			#print temp.getElm()
			elm = word[value]
			if (not temp.next):
				temp.addNext(Node(elm))
				temp.next[0].addId(newId)
				
				#print temp.getElm(), temp.id
				temp = temp.next[0]
			else:
				#print "lastPointer:", lastPointer.getElm(), "|temp:", temp.elm, "|word:", elm
				#print lastPointer.getNext(0).getElm()
				if (finishChain):
					temp.next[-1].addId(newId)
					temp = temp.next[-1]
				elif (temp.getElm() == elm):
					lastPointer.addNext(temp)
					lastPointer.next[-1].addId(newId)
					finishChain = True
				else:
					lastPointer.addNext(Node(elm))
					lastPointer.next[-1].addId(newId)
					lastPointer = lastPointer.next[-1]
				
			value += 1

	def insertChar(self, word):
		if (self.first):
			temp = self.root
			self.checkForSimilarity(list(word), temp)
			
			maxIndex, maxValue = self.bestSimilarity(self.bestMatchIndex, self.countMatch)
			self.chainNodes(maxIndex, maxValue, self.id, list(word))

			self.id += 1
			self.bestMatchIndex = []
		else:
			for elm in word:
				self.addFirstTime(elm)

			self.id += 1
			self.first = True
			self.bestMatchIndex = []

	def printOut2(self, i):
		temp = self.root
		endThePath = False

		while (temp != None):
			if (endThePath == True):
				return

			if (temp.checkId(i)):
				print temp.getElm(), temp.id#, temp.next, temp.id.index(i)

				if (not temp.next):
					break

				if (len(temp.next) > 1): #Do it general
					
					temp = temp.next[1]
				else:
					temp = temp.next[0]
			else:
				if (not temp.next):
					break

				if (temp.next[0] != None):
					temp = temp.next[0]
				else:
					endThePath = True


	def printOut(self):
		temp = self.root
		while (temp != None):
			print temp.getElm(), temp.id
			
			"""
			if (len(temp.next) > 1):
				temp2 = temp.next[1]
				while (not temp2):
					print temp2.next[1].getElm(), temp.next[1].id
			"""


			if (not temp.next):
				break

			if (temp.next[0] != None):
				temp = temp.next[0]

				#if (not temp.next):
				#	break
				
		#print temp.getElm()
			

l = List()
l.insertChar("hipphurra")
l.insertChar("hurrahei")
l.insertChar("hurrameghei")

print "List printed out:"
#l.printOut()
l.printOut2(0)
print "---------"
l.printOut2(1)
print "---------"
l.printOut2(2)