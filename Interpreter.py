# https://www.cs.rit.edu/~wrc/documents/mano-rtl/
# https://en.wikipedia.org/wiki/Instruction_set
# https://en.wikipedia.org/wiki/Load–store_unit_(computing)

from enum import Enum


class InstructionType(Enum):
    HALT = 1
    ADD = 2
    STORE = 3
    CLEAR = 4
    LOAD = 5


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
        5: InstructionType.LOAD
    }

    def interpret(self, memory, starting_address):
        self.memory = memory
        self.PC = starting_address

        while self.run_bit:
            self.instr = self.memory[self.PC]

            # print(self.instr)

            self.instr_type = self.get_instr_type(self.instr)

            if self.instr_type != InstructionType.HALT \
                    and self.instr_type != InstructionType.STORE \
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
        for i in range(self.PC, len(memory)):
            if self.get_instr_type(instr) == type:
                return i + 1

        return -1

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

    def status(self):
        print("PC:", self.PC)
        print("AC:", self.AC)
        self.print_memory()

    def print_memory(self):
        for i in self.memory:
            print(i, "| ", end='')


interpreter = Interpreter()

memory = [5, 19, 2, 28, 2, 2, 3, 4, 1]

interpreter.interpret(memory, 0)

interpreter.status()

# interpreter.memory = memory;

# instr_type = interpreter.get_instr_type(1)
# data_loc = interpreter.find_data(1, instr_type)

# print(interpreter.memory[data_loc])

# for i in range(len(memory)):
#   print(i)

# interpreter.interpret(memory, 0)
