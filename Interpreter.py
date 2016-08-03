from enum import Enum

class InstructionType(Enum):
    HALT = 1
    ADD = 2

class Interpreter(object):

    PC = None
    AC = 0
    instr = None
    instr_type = None
    data_loc = None
    data = None
    run_bit = True
    memory = []

    def interpret(self, memory, startingAddress):
        self.memory = memory;

        PC = startingAddress;

    def get_instr_type(self, opcode):
        print("")

    def find_data(self, instr, instrType):
        print("")

    def execute(self, instrType, data):
        print("")


interpreter = Interpreter()

memory = ["ADD 1", "HALT"]

interpreter.interpret(memory, 0)