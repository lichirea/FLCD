class FiniteAutomata:
    def __init__(self, file):
        self.states = []
        self.alphabet = []
        self.transitions = {}
        self.initial_state = ''
        self.final_states = []

        self.scan_input(file)

    def scan_input(self, file):
        file = open(file, 'r')
        file = file.read().splitlines()
        states = file[0].split(' ')
        for state in states:
            self.states.append(state)
        print(self.states)

        alphabet = file[1].split(' ')
        for letter in alphabet:
            if letter !=
            self.alphabet.append(letter)
        print(self.alphabet)
