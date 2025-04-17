print(f"Zadanie 1")
def wyswietl_imie():
    print("Martyna")
wyswietl_imie()
wyswietl_imie()

print(f"Zadanie 2")
def wyswietl_zmienna():
    print("Hello")
    print("World")

wyswietl_zmienna()
wyswietl_zmienna()

print(f"Zadanie 3")
def dodawanie():
    a = 3
    b = 5
    sum = a + b
    print(f'Suma liczb a = {a} oraz b = {b} wynosi {sum}')
dodawanie()

print(f"Zadanie 4")
def odejmowanie():
    a = 8
    b = 5
    result = a - b
    print(f'Różnica liczb {a} oraz {b} wynosi {result}')

odejmowanie()

print(f'Zadanie 5')
def czy_parzysta():
    liczba = int(input(f'Wpisz liczbę:'))
    if liczba % 2 == 0:
        print("Liczba jest parzysta")
    else:
        print("Liczba jest nieparzysta")

czy_parzysta()

print(f"Zadanie 6")
def czy_podzielna():
    liczba1 = int(input(f'Wpisz liczbę: '))
    liczba2 = int(input(f'Wpisz drugą liczbę: '))

    if liczba1 % liczba2 == 0:
        print(f"Liczba {liczba1} jest podzielna przez {liczba2}")

czy_podzielna()

print(f"Zadanie 7")
def pole_prostokata():
    a = int(input(f'Wpisz długość pierwszego boku: '))
    b = int(input(f'Wpisz długość drugiego boku: '))
    if a <= 0:
        print(f'Zmienna a jest mniejsza lub równa 0')
    if b <= 0:
        print(f'Zmienna a jest mniejsza lub równa 0')
    pole = a*b
    print(f'Pole prostokąta wynosi {pole}')

pole_prostokata()

print(f"Zadanie 8")
def obwod_trojkata_rownobocznego():
    a = int(input(f'Wpisz długość boku: '))
    trojkat = 3 * a
    print(f'Obdwód trójkąta równobocznego wynosi {trojkat}')

obwod_trojkata_rownobocznego()

print(f"Zadanie 9")
def dzielenie():
    a = int(input(f'Wpisz liczbę: '))
    b = int(input(f'Wpisz drugą liczbę: '))
    if b == 0:
        print(f'Nie można dzielić przez 0')
    result = a/b
    print(f'Wynikiem dzielenia liczby {a} przez {b} wynosi {result}')

dzielenie()

print(f"Zadanie 10")
def kim_jestem():
    imie = input(f'Podaj imię: ')
    nazwisko = input(f'Podaj nazwisko: ')
    rok = int(input(f'Podaj rok urodzenia: '))
    waga = int(input(f'Podaj wagę w kilogramach: '))

    print(f' Imię: {imie} \n Nazwisko: {nazwisko} \n Rok urodzenia: {rok} \n Waga: {waga} kg')

kim_jestem()

print(f"Zadanie 11")
def operacje_matematyczne():
    a = int(input(f'Wpisz liczbę: '))
    b = int(input(f'Wpisz drugą liczbę: '))
    sum = a + b
    result = a - b
    multiple = a * b
    divide = a / b
    print(f'Wynik dodawania liczb to: {sum}')
    print(f'Wynik odejmowania liczb to: {result}')
    print(f'Wynik dodawania liczb to: {multiple}')
    if b == 0:
        print(f'Nie można dzielić przez 0')
    else:
        print(f'Wynik dodawania liczb to: {divide}')

operacje_matematyczne()

print(f"Zadanie 12")
def witaj():
    imie = input(f'Podaj imię: ')
    nazwisko = input(f'Podaj nazwisko: ')
    print(f'Witaj, {imie} {nazwisko}!')

witaj()

print(f"Zadanie 13")
def sprawdz_pin():
    pin = 2137
    pin1 = int(input(f'Wpisz kod PIN: '))
    if pin == pin1:
        print(f'Kod PIN jest prawidłowy')
    else:
        print(f'Kod PIN jest nieprawidłowy')

sprawdz_pin()

print(f"Zadanie 14")
def czy_parzysta_i_dodatnia():
    a = int(input(f'Wpisz liczbę: '))
    if a % 2 == 0 and a > 0:
        print(f'Liczba {a} jest parzysta i dodatnia')
    else:
        print(f'Liczba {a} nie spełnia warunków')

czy_parzysta_i_dodatnia()



