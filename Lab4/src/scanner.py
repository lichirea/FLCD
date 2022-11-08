import re
import string
from SymbolTable import SymbolTable


class Scanner:
    def __init__(self, tokens, program):
        self.st = SymbolTable()

        for token in tokens.splitlines():
            self.st.insert("-1", token)

        self.allowedchars = set(string.ascii_lowercase + '_' + string.digits)
        self.variable_count = 0

        self.lineindex = 1
        self.tokenindex = 1
        self.pif = open('Lab4/Output/pif.out', 'a+')
        self.pif.write('\n\nscanning a new file... \n')

        self.program = program

    def scan(self):
        separator_regex = r'([:]|[;;]+|[,]|[{]|[}]|[+]|[-]|[*]|[**]+|[/]|[%]|[<]|[>]|[<=]+|[>=]+|[==]+|[=/=]+|[::]+|[??]+)'
        program = self.program.splitlines()
        for line in program:
            line = line.split()
            for part in line:
                tokens = re.split(separator_regex, part)
                for token in tokens:
                    if token == '':
                        continue
                    if (not self.genPIF(token)):
                        return False
                    self.tokenindex += 1
            self.lineindex += 1
        print('LEXICALLY CORRECT!')
        return True

    def genPIF(self, token):

        index = self.st.has(token)
        if index == None:
            if set(token) <= self.allowedchars:
                index = self.variable_count
                self.st.insert(str(index), token)
                self.variable_count += 1
            else:
                print('ERROR at token \'' + token +
                      '\' on line ' + str(self.lineindex))
                return False

        self.pif.write(token + " -> " + str(index) + "\n")
        return True
