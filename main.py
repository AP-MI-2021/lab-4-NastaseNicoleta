def printMenu():
    print("1. citire lista")
    print("2. Toate numerele negative nenule din lista")
    print("3. Cel mai mic numar care are ultima cifra egala cu un numar citit de la tastatura")
    print("4. Toate elementele din lista care sunt superprime")
    print("5. Listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu"
          "CMMDC-ul lor și numerele negative au cifrele în ordine inversă ")
    print("x. Iesire")

def citire_termeni():
    list = []
    n = int(input(" dati numarul de termeni din lista, n = "))
    for i in range(n):
        list.append(int(input("list[ " + str(i) + " ] = ")))
    return list

#problema 2

def numere_negative_nenule(n: int):
    if n != 0 and n < 0:
        return True
    return False

def test_numere_negative_nenule():
    assert numere_negative_nenule(-7) is True
    assert numere_negative_nenule(0) is False

def numere_negative_nenule_lista(l: list):
    rezultat = []
    for x in l:
        if numere_negative_nenule(x):
            rezultat.append(x)
    return rezultat

def test_numere_negative_nenule_lista():
    assert numere_negative_nenule_lista([-5, 0, -3, -16]) ==[ -5, -3, -16]
    assert numere_negative_nenule_lista([-25, -187, 6, 8, -10]) == [-25, -187, -10]

# problema 3

def numar_cu_ultima_cifra_egala_cu_k(n: int, k: int):
    if n % 10 == k :
        return True
    return False

def test_numar_cu_ultima_cifra_egala_cu_k():
    assert numar_cu_ultima_cifra_egala_cu_k(123, 3) == True
    assert numar_cu_ultima_cifra_egala_cu_k(673, 3) == True

def cel_mai_mic_nr_din_lista_cu_ultima_cifra_egala_cu_k(l: list, k: int):
    m = 10000
    for x in l:
        if numar_cu_ultima_cifra_egala_cu_k(x, k) is True and x < m :
            m = x
    return m

def test_cel_mai_mic_nr_din_lista_cu_ultima_cifra_egala_cu_k():
    assert cel_mai_mic_nr_din_lista_cu_ultima_cifra_egala_cu_k([123, 63, 13], 3) == 13
    assert cel_mai_mic_nr_din_lista_cu_ultima_cifra_egala_cu_k([456, 1676, 386], 6) == 386


#problema 5

def cmmdc(x: int, y: int):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x

def test_cmmdc():
    assert cmmdc(8, 4) == 4
    assert cmmdc(18, 6) == 6

def lista_noua(l: list):
    rezultat = []
    cifre = []
    for x,y in l:
        if x > 0 and y != 0:
            rezultat.append(cmmdc(x,y))
        elif x < 0:
            cifre.append(x % 10 / 10)
            cifre.sort(reverse=False)
            rezultat.append(cifre)
    print(rezultat)


def main():

    l =[]
    while True:
        printMenu()
        optiune = input("dati optiunea: ")
        if optiune == '1':
            list = citire_termeni()
        elif optiune == '2':
            print(numere_negative_nenule_lista(l))
        elif optiune == '3':
            k=int(input("Dati numarul: "))
            print(cel_mai_mic_nr_din_lista_cu_ultima_cifra_egala_cu_k(l, k))
        elif optiune == '5':
            print(lista_noua(l))
        elif optiune == 'x':
            break
        else:
            print("Optiune gresita! Reincercati: ")


if __name__ == '__main__':
    test_numere_negative_nenule()
    test_numere_negative_nenule_lista()
    test_numar_cu_ultima_cifra_egala_cu_k()
    test_cel_mai_mic_nr_din_lista_cu_ultima_cifra_egala_cu_k()
    test_cmmdc()

    main()
