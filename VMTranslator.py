import os
import sys

ERROR = -1
C_RETURN = 0
C_PUSH = 1
C_POP = 2
C_ARITHMETIC = 3
C_FUNCTION = 4
C_CALL = 5
C_GOTO = 6
C_IF = 7
C_LABEL = 8

segment_label = {'stack': 'SP', 'local': 'LCL', 'argument': 'ARG', 'this': 'THIS', 'that': 'THAT'}

class Parser():

	def __init__(self, inputFile):
		self.lines = []
		self.fileName = inputFile.split('/')[-1]
		self.line_number = 0
		self.f = open(inputFile, "r")

	def readNextLine(self):
		self.line = self.f.readline()
		if self.hasMoreCommands() == False:
			self.closeFile()
			return 0
		while self.line == '\n' or self.line[0:2] == "//":
			self.line = self.f.readline()
		self.lines.append(self.line)
		self.line_number = self.line_number + 1
		return 1

	def hasMoreCommands(self):
		if self.line:
			return (True)
		return (False)

	def jumpComments(self):
		while self.commandType() == ERROR and self.hasMoreCommands():
			self.printCurrentLine()
			self.readNextLine()

	def commandType(self):
	
		arithmetic_commands = ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]

		while (self.line == '\n'):
			self.readNextLine()
		self.command = self.line.split()
		
		if self.command[0] == "push":
			return C_PUSH
		elif self.command[0] == "pop":
			return C_POP
		elif self.command[0] in arithmetic_commands:
			return C_ARITHMETIC
		elif self.command[0] == "goto":
			return C_GOTO
		elif self.command[0] == "if-goto":
			return C_IF
		elif self.command[0] == "label":
			return C_LABEL
		elif self.command[0] == "call":
			return C_CALL
		elif self.command[0] == "function":
			return C_FUNCTION
		elif self.command[0] == "return":
			return C_RETURN
		else:
			return ERROR

	def arg1(self):

		if self.commandType() == C_RETURN:
			raise Exception("Don't work with C_RETURN")
		elif self.commandType() == C_ARITHMETIC:
			return(self.command[0])
		else:
			return(self.command[1])			

	def arg2(self):

		proper_types = ["push", "pop", "function", "call"]

		if self.command[0] in proper_types:
			return(self.command[2])
		else:
			raise Exception("Cannot return with this specific type")

	def printCurrentLine(self):
		print(self.line, end = '')
		return (self.line)
	
	def closeFile(self):
		self.f.close()

class CodeWriter():
	
	def __init__(self, inputFile):
		# Check if argv is Dir or File
		# Set output filename
		if os.path.isdir(inputFile):
			print('Directory')
			outputFile = inputFile + '.asm'
		elif inputFile[-2:] == 'vm':
			print('File')
			outputFile = inputFile.split('/')[-1].split('.')[0] + '.asm'
		else:
			raise Exception('Input should be Directory of VM File')
		
		# open outputFile with w permission
		self.f = open(outputFile, "w")
		self.lineNumber = 0
		self.functionNumber = 0
		if os.path.isdir(inputFile):
			self.writeInit()

	def setFileName(self, File):
		self.fileName = File.fileName

	def writeInit(self):
		self.f.write(
		'@256\n' + 
		'D=A\n' + 
		'@SP\n' + 
		'M=D\n')
		self.writeCall('Sys.init', 0)

	def writeLine(self, File):
		self.lineNumber += 1 
		self.f.write('//' + File.line)
		print('//' + File.line)
		if File.commandType() == C_PUSH or File.commandType() == C_POP:
			self.writePushPop(File.command[0], File.arg1(), int(File.arg2()))
		elif File.commandType() == C_ARITHMETIC:
			self.writeArithmetic(File.command[0])
		elif File.commandType() == C_GOTO:
			self.writeGoto(File.arg1())
		elif File.commandType() == C_IF:
			self.writeIf(File.arg1())
		elif File.commandType() == C_LABEL:
			self.writeLabel(File.arg1())
		elif File.commandType() == C_CALL:
			self.writeCall(File.arg1(), int(File.arg2()))
		elif File.commandType() == C_FUNCTION:
			self.writeFunction(File.arg1(), int(File.arg2()))
		elif File.commandType() == C_RETURN:
			self.writeReturn(File)
		else:
			raise Exception('Unknown command type')

	def writeArithmetic(self, command):
		''' Translate logical and arithmetical VM commands to Assembly and write to file'''

		def SP_increment():
			self.f.write('@SP\nM=M+1\n')
		def continue_loop():
			self.f.write(
			'@CONTINUE' + str(self.lineNumber) + '\n' + 
			'0;JMP\n')
		
		if command == 'add' or command == 'sub':
			self.f.write('@SP\n')
			self.f.write('M=M-1\n')
			self.f.write('A=M\n')
			self.f.write('D=M\n')
			self.f.write('@SP\n')
			self.f.write('M=M-1\n')
			self.f.write('A=M\n')
			if command == 'add':
				self.f.write('M=M+D\n')
			else:
				self.f.write('M=M-D\n')
			self.f.write('@SP\n')
			self.f.write('M=M+1\n')
		elif command == 'eq' or command == 'gt' or command == 'lt':
			self.f.write(
			'@SP\n' + 
			'AM=M-1\n' + 
			'D=M\n' + 
			'@SP\n' + 
			'AM=M-1\n' + 
			'D=D-M\n')
			if command == 'eq':
				self.f.write('@EQUAL' + str(self.lineNumber) + '\n')
				self.f.write('D;JEQ\n')
			elif command == 'lt':
				self.f.write('@GREATER' + str(self.lineNumber) + '\n')
				self.f.write('D;JGT\n')
			else:
				self.f.write('@LESS' + str(self.lineNumber) + '\n')
				self.f.write('D;JLT\n')
			self.f.write(
			'@SP\n' + 
			'A=M\n' + 
			'M=0\n')
			SP_increment()
			continue_loop()
			if command == 'eq':
				self.f.write('(EQUAL' + str(self.lineNumber) + ')\n')
			elif command == 'lt':
				self.f.write('(GREATER' + str(self.lineNumber) + ')\n')
			else:
				self.f.write('(LESS' + str(self.lineNumber) + ')\n')
			self.f.write(
			'@SP\n' + 
			'A=M\n' + 
			'M=-1\n')
			SP_increment()
			self.f.write('(CONTINUE' + str(self.lineNumber) + ')\n')
		elif command == 'not' or  command == 'neg':
			self.f.write(
			'@SP\n' + 
			'A=M-1\n')
			if command == 'not':
				self.f.write('M=!M\n')
			else:
				self.f.write('M=-M\n')
			self.f.write(
			'@SP\n' + 
			'A=M\n' + 
			'M=M-1\n')	
		elif command == 'and' or command == 'or':
			self.f.write(
			'@SP\n' + 
			'AM=M-1\n' + 
			'D=M\n' + 
			'@SP\n' + 
			'AM=M-1\n')
			if command == 'or':
				self.f.write('M=M|D\n')
			else:
				self.f.write('M=M&D\n')
			SP_increment()
		else:
			raise Exception('Unknown command')

	def writePushPop(self, command, segment, index):
		''' Translate push or pop VM commands to Assembly and write to file'''
		
		dinamic_segments = ['local', 'that', 'this', 'argument']

		def Dregister_save_index():
			self.f.write('@' + str(index) + '\nD=A\n')
		def SP_push_and_increment():
			self.f.write('@SP\nA=M\nM=D\n@SP\nM=M+1\n')

		if command == 'push':
			if segment == 'constant':
				# Save index in D register
				Dregister_save_index()
				# Atualize and increment SP
				SP_push_and_increment()
			elif segment in dinamic_segments:
				# Save index in D register
				Dregister_save_index()
				# Look for value in segment
				self.f.write(
				'@' + segment_label[segment] + '\n' + 
				'A=D+M\n' + 
				'D=M\n')
				# Atualize and increment SP
				SP_push_and_increment()
			elif segment == 'static':
				self.f.write(
				'@' + self.fileName + str(index) + '\n' + 
				'D=M\n')
				SP_push_and_increment()
			elif segment == 'temp':
				# Save index in D register
				Dregister_save_index()
				# Look for value in segment
				self.f.write(
				'@5\n' + 
				'A=A+D\n' + 
				'D=M\n')
				# Atualize and increment SP
				SP_push_and_increment()
			elif segment == 'pointer':
				# Save index in D register
				Dregister_save_index()
				# Look for base address in segment
				self.f.write(
				'@3\n' + 
				'A=A+D\n' + 
				'D=M\n')
				# Atualize and increment SP
				SP_push_and_increment()
			else:
				raise Exception('Inexistent Memory Segment')
		elif command == 'pop':
			if segment in dinamic_segments:
				# Atualize segment value with new base address
				self.f.write(
				'@' + str(index) + '\n' + 
				'D=A\n' + 
				'@' + segment_label[segment] + '\n' + 
				'M=D+M\n')
				# Walk back and save SP value in D register
				self.f.write(
				'@SP\n' + 
				'M=M-1\n' + 
				'A=M\n' + 
				'D=M\n')
				# Go to segmenet addres and save D register
				self.f.write('@' + segment_label[segment] + '\n' + 
				'A=M\n' + 
				'M=D\n' + 
				'A=M\n')
				# Reset base address in segment
				self.f.write('@' + str(index) + '\n' + 
				'D=A\n' + 
				'@' + segment_label[segment] + '\n' + 
				'M=M-D\n')
			elif segment == 'static':
				self.f.write(
				'@' + self.fileName + str(index) + '\n' + 
				'D=A\n' + 
				'@R13\n' + 
				'M=D\n' + 
				'@SP\n' + 
				'AM=M-1\n' + 
				'D=M\n' + 
				'@R13\n' + 
				'A=M\n' + 
				'M=D\n')
			elif segment == 'temp' or segment == 'pointer':
				# Save temp + i address in D register
				if segment == 'temp':
					self.f.write('@5\n')
				else:
					self.f.write('@3\n')
				self.f.write(
				'D=A\n' + 
				'@' + str(index) + '\n' + 
				'D=A+D\n')
				# Save temp + i address in *SP
				self.f.write(
				'@SP\n' + 
				'A=M\n' + 
				'M=D\n')
				# Save *SP-- in D register
				self.f.write(
				'@SP\n' + 
				'A=M-1\n' + 
				'D=M\n')
				# Go to temp + i address (saved in *SP) and save D register in memory
				self.f.write(
				'@SP\n' + 
				'A=M\n' + 
				'A=M\n' + 
				'M=D\n')
				# Walk back *SP
				self.f.write(
				'@SP\n' + 
				'M=M-1\n')
			else:
				raise Exception('Inexistent Memory Segment')

	def writeCall(self, functionName, nArgs):
		
		returnAddress = 'RETURN_ADDR' + str(self.functionNumber)
		self.functionNumber = self.functionNumber + 1

		def SP_push_and_increment():
			self.f.write('@SP\nA=M\nM=D\n@SP\nM=M+1\n')

		# push retAddrLabel
		self.f.write(
		'@' + str(returnAddress) + '\n' + 
		'D=A\n')
		SP_push_and_increment()
		# push local
		for i in ['local', 'argument', 'this', 'that']:
			self.f.write(
			'@' + segment_label[i] + '\n' + 
			'D=M\n')			
			SP_push_and_increment()
		# ARG = SP - 5 - nArgs
		self.f.write(
		'@SP\n' + 
		'D=M\n' + 
		'@5\n' + 
		'D=D-A\n' + 
		'@' + str(nArgs) + '\n' + 
		'D=D-A\n' + 
		'@ARG\n' + 
		'M=D\n')
		# LCL = SP
		self.f.write(
		'@SP\n' + 
		'D=M\n' + 
		'@LCL\n' + 
		'M=D\n')
		# goto functionName
		self.writeGoto(functionName)
		# (retAddrLabel)
		self.f.write('(' + str(returnAddress) + ')\n')

	def writeFunction(self, functionName, nArgs):
		
		self.f.write('(' + functionName + ')\n')
		while nArgs > 0:
			self.writePushPop('push', 'constant', 0)
			nArgs = nArgs - 1

	def writeReturn(self, File):

		def restoreSegments(segment):
			self.f.write(
			'@R11\n' + 
			'D=M-1\n' +
			'AM=D\n' +
			'D=M\n' +
			'@' + segment + '\n' +
			'M=D\n'
			)

		self.f.write(
		'@LCL\n' + 
		'D=M\n' + 
		'@R11\n' + 
		'M=D\n' + 
		'@5\n' + 
		'A=D-A\n' + 
		'D=M\n' + 
		'@R12\n' + 
		'M=D\n')
		self.writePushPop('pop', 'argument', 0)
		self.f.write(
		'@ARG\n' + 
		'D=M\n' + 
		'@SP\n' + 
		'M=D+1\n')
		restoreSegments('THAT')
		restoreSegments('THIS')
		restoreSegments('ARG')
		restoreSegments('LCL')
		self.f.write(
		'@R12\n' + 
		'A=M\n' + 
		'0;JMP\n')

	def writeGoto(self, label):
		
		self.f.write('@' + label + '\n' + 
		'0;JMP\n')

	def writeIf(self, label):
		
		self.f.write(
		'@SP\n' + 
		'AM=M-1\n' + 
		'D=M\n' + 
		'@' + label + '\n' + 
		'D;JNE\n')

	def writeLabel(self, label):
		
		self.f.write('(' + label + ')\n')

	def closeFile(self):
		print('Closing file')
		self.f.close()

def main():
		
	file_path = sys.argv[1]

	def parseFile(file):
		f = Parser(file)
		f.readNextLine()
		f.jumpComments()
		Output.setFileName(f)
		while f.line:
			Output.writeLine(f)
			f.readNextLine()

	Output = CodeWriter(file_path)
	if os.path.isdir(file_path):
		VMfiles = [f for f in os.listdir(file_path) if f[-2:] == 'vm']
		if 'Sys.vm' not in VMfiles:
			raise Exception("There is no Sys file in your directory")
		VMfiles.remove('Sys.vm')
		VMfiles.append('Sys.vm')
		for i in VMfiles:
			parseFile(file_path + '/' + i)
	elif file_path[-2:] == 'vm':
		parseFile(file_path)
	else:
		raise Exception("VM Tranlator only accepts directories or VM Files")
	Output.closeFile()

if __name__ == '__main__':
    main()