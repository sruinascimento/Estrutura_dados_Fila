from nodefila import Node 

class Queue(object):

	def __init__(self):
		self.first = None
		self.last = None
		self.len = 0

	def noEmpty(self):
		# Returna true caso a fila não esteja vazia
		return self.len > 0

	def push(self, element):
		#1º método: Inserção de element
		node_aux = Node(element)
		if not self.first:
			self.first = node_aux
			self.last = node_aux
		else:
			self.last.next = node_aux
			self.last = node_aux
		self.len += 1
		return node_aux.data

	def pop(self):
		#2º método: Remoção do 1º fila
		if self.noEmpty():
			node_aux = self.first
			self.first = self.first.next
			self.len -= 1
			return node_aux.data
		raise IndexError('The queue is empty')

	def peek(self):
		#3º método: retorna o primeiro da fila
		if self.noEmpty():
			return self.first.data

	def __len__(self):
		return self.len

	def __repr__(self):
		# Representação dos dados
		if self.noEmpty():
			data = ''
			pointer = self.first
			while pointer:
				data += str(pointer.data) + '\t'
				pointer = pointer.next
			return data
		return 'The queue is empty'

	def __str__(self):
		return self.__repr__()