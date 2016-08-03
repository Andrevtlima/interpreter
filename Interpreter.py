from enum import Enum

class InstructionType(Enum):
    HALT = 1
    ADD = 1

class Interpreter(object):

    memory = []

    def __init__(self):
        print("Construtor")

    def teste(self):
        print("Hello")


teste = Interpreter()
teste.teste()