from finite_automata import FiniteAutomata


def main():
    fa = FiniteAutomata("Lab6/FA.in")

    while True:
        print_menu()
        choice = input("\nPlease choose:")
        match choice:
            case "1":
                print(fa.states)
            case "2":
                print(fa.alphabet)
            case "3":
                print(fa.transitions)
            case "4":
                print(fa.initial_state)
            case "5":
                print(fa.final_states)
            case "6":
                seq = input("Enter a sequence:").strip()
                seq = seq.split(' ')
                fa.check_seq(seq)
            case _:
                pass


def print_menu():
    print('1.Set of states')
    print('2.Alphabet')
    print('3.Transitions')
    print('4.Initial State')
    print('5.Final States')
    print('6.Enter and check sequence')


if __name__ == "__main__":
    main()
