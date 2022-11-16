from finite_automata import FiniteAutomata


def main():
    fa = FiniteAutomata("Lab4/FA.in")

    while True:
        print_menu()
        choice = input("Choose:")
        match choice:
            case "1":
                pass
            case _:
                pass


def print_menu():
    print('1.Set of states')
    print('2.Alphabet')
    print('3.Transitions')
    print('4.Initial State')
    print('5.Final States')


if __name__ == "__main__":
    main()
