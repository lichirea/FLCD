import re
import string
from SymbolTable import SymbolTable


class Scanner:
    def __init__(self, tokens, program):
        self.st = SymbolTable()

        self.keywords = []
        for token in tokens.splitlines():
            self.keywords.append(token)

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
        
        if token in self.keywords:
            index = self.keywords.index(token)
            self.pif.write(token + " -> " + "-1" + '\n')
        else:
            index = self.st.find(token)
            if index == None:
                if(self.constant_or_identifier(token) == -1):
                    print('ERROR at token \'' + token +
                        '\' on line ' + str(self.lineindex))
                    return False
                else:
                    index = self.st.insert(token, index)
                    self.variable_count += 1;
                
            id = self.constant_or_identifier(token)
            self.pif.write(str(id) + " -> " + str(index) + '\n')
            
        return True

    def constant_or_identifier(self, token):
        if set(token) <= set(string.digits):
            return 'constant'
        elif set(token) <= self.allowedchars:
            return 'identifier'
        else:
            return -1