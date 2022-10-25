from SymbolTable import SymbolTable


def main():
    st = SymbolTable()

    st.insert('a', 5)

    print('a = ' + str(st.find('a')))

    st.remove('a');
    print(st.find('a'));

if __name__ == "__main__":
    main()
