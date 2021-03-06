# https://www.cs.rit.edu/~wrc/documents/mano-rtl/
# https://en.wikipedia.org/wiki/Instruction_set
# https://en.wikipedia.org/wiki/Load–store_unit_(computing)
# https://www.cs.umd.edu/class/sum2003/cmsc311/Notes/Mips/load.html
# https://en.wikibooks.org/wiki/A-level_Computing/AQA/Computer_Components,_The_Stored_Program_Concept_and_the_Internet/Machine_Level_Architecture/Machine_code_and_processor_instruction_set

from enum import Enum
import sys

class InstructionType(Enum):
    HALT = 1
    ADD = 2 #42 ;adds the number 42 to the contents of the accumulator 
    STORE = 3 #34  ;save the accumulator result to the memory address 34
    CLEAR = 4
    LOAD = 5 #23 ;loads the number 23 into the accumulator
    AND = 6 #boolean algebra function
    INC = 7 #increment a number by 1
    MUL = 8 #multiply numbers together


class Interpreter(object):
    PC = None
    AC = 0
    instr = None
    instr_type = None
    data_loc = None
    data = None
    run_bit = True
    memory = []
    instructions = {
        1: InstructionType.HALT,
        2: InstructionType.ADD,
        3: InstructionType.STORE,
        4: InstructionType.CLEAR,
        5: InstructionType.LOAD,
        6: InstructionType.AND,
        7: InstructionType.INC,
        8: InstructionType.MUL
    }

    def interpret(self, memory, starting_address):
        self.memory = memory
        self.PC = starting_address

        while self.run_bit:
            self.instr = self.memory[self.PC]

            #print("self",self.instr)

            self.instr_type = self.get_instr_type(self.instr)

            if self.instr_type != InstructionType.HALT \
                    and self.instr_type != InstructionType.STORE \
                    and self.instr_type != InstructionType.INC \
                    and self.instr_type != InstructionType.CLEAR:

                self.data_loc = self.find_data(self.instr, self.instr_type)

                if self.data_loc >= 0:
                    self.data = self.memory[self.data_loc]
                    self.PC += 1

            self.execute(self.instr_type, self.data)
            self.PC += 1

    def get_instr_type(self, opcode):
        return self.instructions.get(opcode)

    def find_data(self, instr, type):
                  
                return self.PC + 1

        
    def execute(self, type, data):
        if type == InstructionType.HALT:
            self.run_bit = False
        elif type == InstructionType.ADD:
            self.AC += data
        elif type == InstructionType.STORE:
            self.memory.append(self.AC)
        elif type == InstructionType.CLEAR:
            self.AC = 0
        elif type == InstructionType.LOAD:
            self.AC = data
        elif type == InstructionType.AND:
        	temp = 0
        	if self.AC == data:
        		temp = 1
        	
        	self.AC = temp
        elif type == InstructionType.INC:
        	self.AC += 1
        elif type == InstructionType.MUL:
        	self.AC *= data
        	
    def status(self):
        print("PC:", self.PC)
        print("AC:", self.AC)
        self.print_memory()

    def print_memory(self):
        for i in self.memory:
            print(i, "| ", end='')


interpreter = Interpreter()
memory = []
file_path = sys.argv[1]
#print (file_path)
file_input = open(file_path, "r")

for line in file_input.readlines():
    buffer = line.rstrip().split(" ")

    instr = buffer[0]
    instr_opcode = InstructionType[instr].value
    memory.append(instr_opcode)

    if len(buffer) > 1:
        operand = int(buffer[1])

        if operand is not None:
            memory.append(operand)

    print(memory)

interpreter.interpret(memory, 0)
interpreter.status()

# memory = [5, 19, 2, 28, 2, 2, 3, 4, 1]

# interpreter.interpret(memory, 0)

# interpreter.status()

# interpreter.memory = memory;

# instr_type = interpreter.get_instr_type(1)
# data_loc = interpreter.find_data(1, instr_type)

# print(interpreter.memory[data_loc])

# for i in range(len(memory)):
#   print(i)

# interpreter.interpret(memory, 0)
