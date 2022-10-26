from SymbolTable import SymbolTable


def main():
    st = SymbolTable()

    st.insert('a', 5)

    print('a = ' + str(st.find('a')))

    print('This was just removed: ' + str(st.remove('a')))

    print('Trying to find \'a\' now: ' + str(st.find('a')))

if __name__ == "__main__":
    main()
