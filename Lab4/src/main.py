from scanner import Scanner
from SymbolTable import SymbolTable


def main():

    file = open('Lab4/Input/token.in', 'r')
    tokens = file.read()

    file = open('Lab4/Input/p1.rtl')
    p1 = file.read()
    scanner = Scanner(tokens, p1)
    print('scanning p1.rtl...')
    scanner.scan()

    file = open('Lab4/Input/p1err.rtl')
    p1err = file.read()
    scanner = Scanner(tokens, p1err)
    print('scanning p1err.rtl...')
    scanner.scan()

    file = open('Lab4/Input/p2.rtl')
    p2 = file.read()
    scanner = Scanner(tokens, p2)
    print('scanning p2.rtl...')
    scanner.scan()

    file = open('Lab4/Input/p3.rtl')
    p3 = file.read()
    scanner = Scanner(tokens, p3)
    print('scanning p3.rtl...')
    scanner.scan()


if __name__ == "__main__":
    main()
