class VirtualMachine:
    LETTERS = {
        0: 'H',
        1: 'D',
        2: 'P',
        3: 'L'
    }

    @staticmethod
    def get_instruction(current):
        """
        :param current: int
                    current memory block
        :return: int
            current instruction
        """
        return current >> 6

    @staticmethod
    def get_memory(mem_block):
        """
        :param mem_block: int
                    current memory block
        :return:
        """
        return ((1 << 6) - 1) & mem_block

    @staticmethod
    def increment_mem(mem_block):
        """
        increments whole memory block
        :param mem_block: int
        :return: int
                new memory block
        """
        if mem_block + 1 == int('0b100000000', 2):
            return 0
        else:
            return mem_block + 1

    @staticmethod
    def decrement_mem(mem_block):
        """
        decrements whole memory block
        :param mem_block: int
        :return:int
                new memory block
        """
        if mem_block == 0:
            return int('0b11111111', 2)
        else:
            return mem_block - 1

    @classmethod
    def get_letter(cls, mem_block):
        """
        :param mem_block: int
        :return: str
                returns letter that is represented by payload in memory block
        """
        return cls.LETTERS[mem_block & 3]

    def increment(self, curr):
        """
        One of basic operations, increments memory block and returns it
        :param curr: dict
                    current memory block
        :return: dict
            new memory block
        """
        incremented_value = VirtualMachine.increment_mem(curr['Memory_block'])
        curr['Memory_block'] = incremented_value
        return curr

    def decrement(self, curr):
        """
        basic operation, decrements memory block
        :param curr: dict
                    current memory block
        :return: dict
        new memory block
        """
        decremented_value = VirtualMachine.decrement_mem(curr['Memory_block'])
        curr['Memory_block'] = decremented_value
        return curr

    def jump(self, curr, program):
        """
        Basic operation, jumps to another position
        :param curr: dict
        :param program: list
                whole program
        :return:
            returns dict
            new memory block
        """
        new_address = VirtualMachine.get_memory(curr['Memory_block'])
        curr['Address'] = new_address
        curr['Memory_block'] = program[new_address ]
        return curr

    def write(self, curr):
        """
        Basic operation
        :param curr: dict
        :return: str
            letter to be writen
        """
        return VirtualMachine.get_letter(curr['Memory_block'])

    def __init__(self, limit):

        self.LIMIT = limit

    def run_program(self, program):
        """
        Main method of vm class, runs given program and as generator yields letters to be used in fitness fuction
        :param program: list
                list of commands
        :return: str
            yields letters
        """
        try:
            curr = {
                'Address': 0,
                'Memory_block': program[0]
            }
        except TypeError:
            print(program)
            return

        for i in range(0, self.LIMIT):
            instruction = VirtualMachine.get_instruction(curr['Memory_block'])
            if instruction == 1:
                curr = self.increment(curr)
                program[curr['Address']] = curr['Memory_block']
            elif instruction == 0:
                curr = self.decrement(curr)
                program[curr['Address']] = curr['Memory_block']
            elif instruction == 2:
                curr = self.jump(curr, program)
            elif instruction == 3:
                yield VirtualMachine.get_letter(curr['Memory_block'])

            if instruction != 2 and curr['Address'] != 63:
                curr['Address'] += 1
                curr['Memory_block'] = program[curr['Address']]

            elif curr['Address'] == 63:
                return

            if curr['Memory_block'] == 0:
                return

        return



def test_get_intruction():
    assert VirtualMachine.get_instruction(int('0b11101001', 2)) == int('0b11', 2)
    assert VirtualMachine.get_instruction(int('0b101001', 2)) == 0
    assert VirtualMachine.get_instruction(int('0b11101001', 2)) == int(3)


def test_get_memory():
    assert VirtualMachine.get_memory(int('0b11101001', 2)) == int('0b101001', 2)
    assert VirtualMachine.get_memory(int('0b01101111', 2)) == int('0b101111', 2)


def test_increment():
    assert VirtualMachine.increment_mem(int('0b11101001', 2)) == int('0b11101010', 2)
    assert VirtualMachine.increment_mem(int('0b11111111', 2)) == 0
    assert VirtualMachine.increment_mem(int('0b00000000', 2)) == int('0b00000001', 2)


def test_decrement():
    assert VirtualMachine.decrement_mem(int('0b11101001', 2)) == int('0b11101000', 2)
    assert VirtualMachine.decrement_mem(int('0b11111111', 2)) == int('0b11111110', 2)
    assert VirtualMachine.decrement_mem(int('0b00000000', 2)) == int('0b11111111', 2)


def test_get_letters():
    assert VirtualMachine.get_letter(int('0b11101001', 2)) == 'D'
    assert VirtualMachine.get_letter(int('0b11111111', 2)) == 'L'
    assert VirtualMachine.get_letter(int('0b00000000', 2)) == 'H'
    assert VirtualMachine.get_letter(int('0b00000010', 2)) == 'P'


