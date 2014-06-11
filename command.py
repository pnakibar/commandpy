class AbstractCommand:

	def __init__(self, receiver):
		self.receiver = receiver

	def execute(self): pass


class ConcreteCommand(AbstractCommand):
	def execute(self):
		self.receiver.action()



class Receiver:
	def action(self):
		print("Executado.")


class Invoker:
	command = None

	def setCommand(self, command):
		self.command = command

	def executeCommand(self):
		self.command.execute()




'''Programa principal'''
receiver = Receiver()
comm = ConcreteCommand(receiver)
invoker = Invoker()


invoker.setCommand(comm)
invoker.executeCommand()