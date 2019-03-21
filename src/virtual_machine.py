class VirtualMachine:

    def increment(self):
        pass

    def decrement(self):
        pass

    def jump(self):
        pass

    def write(self):
        pass

    def __init__(self):

        __instructions = {
            0: self.increment,
            1: self.decrement,
            2: self.jump,
            3: self.write
        }


    def run_program(self):
        pass