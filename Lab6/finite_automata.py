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

        alphabet = file[1].split(' ')
        for letter in alphabet:
            self.alphabet.append(letter)

        self.initial_state = file[2]

        final_states = file[3].split(' ')
        for state in final_states:
            self.final_states.append(state)

        deterministic = True
        for i in range(4, len(file)):
            line = file[i].split(' ')
            if self.transitions.get((line[0], line[1])):
                self.transitions[(line[0], line[1])].append(line[2])
                deterministic = False
            else:
                self.transitions[(line[0], line[1])] = [line[2]]

        if deterministic:
            print("The FA is a DFA!!!")
        else:
            print("THE FA is NOT a DFA")

    def check_seq(self, seq):
        state = self.initial_state
        next_state = None
        for s in seq:
            if self.transitions.get((state, s)):
                next_state = self.transitions.get((state, s))[0]
            if next_state != None:
                state = next_state
                next_state = None
        if state in self.final_states:
            print("ACCEPTED")
        else:
            print("NOT ACCEPTED")
