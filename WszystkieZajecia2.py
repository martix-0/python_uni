print(f"Zadanie 1")
x = 5
if x > 10:
    print("Ta wartość jest większa niż 10")

print(f"Zadanie 2")
x = "Martyna"
if len(x) > 10:
    print("Za długie imię!")
else:
    print("Prawidłowa długość imienia!")

print(f"Zadanie 3")
x = 10
y = 15
if x + y > 20:
    print("Suma liczb jest większa niż 20")
else:
    print("Suma liczb nie przekracza 20")

print(f"Zadanie 4")
a = 15
if a % 2 == 0:
    print(f"Liczba {a} jest parzysta")
else:
    print(f"Liczba {a} nie jest parzysta")

print(f"Zadanie 5")
a = int(input("Podaj całkowitą liczbę: "))
print(f"Podano liczbę {a}.")
if a % 2 == 0:
    print(f"Liczba {a} jest podzielna na 2.")
else:
    print(f"Liczba {a} nie jest podzielna na 2.")
if a % 3 == 0:
    print(f"Liczba {a} jest podzielna na 3.")
else:
    print(f"Liczba {a} nie jest podzielna na 3.")
if a % 4 == 0:
    print(f"Liczba {a} jest podzielna na 4.")
else:
    print(f"Liczba {a} nie jest podzielna na 4.")

print(f"Zadanie 6")
temperatura = 15

if temperatura < 10:
    print("Jest zimno")
elif 10 <= temperatura <= 20:
    print("Może być")
else:
    print("Jest ciepło")

print(f"Zadanie 7")
imie = input("Podaj imię: ")
if len(imie) > 10:
    print("Imię jest za długie!")

nazwisko = input("Podaj nazwisko: ")
if len(nazwisko) > 15:
    print("Nazwisko jest za długie!")

rokUrodzenia = int(input("Podaj rok urodzenia: "))
wiek = 2025 - rokUrodzenia
if wiek < 18:
    print("Wiek osoby jest mniejszy niż 18 lat!")

login = input("Podaj login: ")
if login in ["marek123", "karolinka5", "bobek99"]:
    print("Login jest już zajęty!")

haslo = input("Podaj hasło: ")
haslo_powtorzone = input("Powtórz hasło: ")
if haslo != haslo_powtorzone:
    print("Hasło i hasło powtórzone są różne!")

if len(imie) <= 10 and len(nazwisko) <= 15 and wiek >= 18 and login not in ["marek123", "karolinka5", "bobek99"] and haslo == haslo_powtorzone:
    print(f"Witaj {imie} {nazwisko}, Twoje konto zostało utworzone!")

print(f"Zadanie 8")
a = int(input("Podaj pierwszą liczbę (a): "))
b = int(input("Podaj drugą liczbę (b): "))

if a > b and a % b == 0:
    print(f"Liczba {a} jest podzielna na liczbę {b}")
elif b > a and b % a == 0:
    print(f"Liczba {b} jest podzielna na liczbę {a}")
else:
    print("Brak podzielności")

print(f"Zadanie 9")
a = 10
b = 15

if a > b and a < 100:
    print("A")
elif a < b or b % 2 == 0:
    print("B")
elif (a + b > 10) and (b - a < 0):
    print("C")

print(f"Zadanie 10")
temperatura = 26

if temperatura > 25:
    print("Jest gorąco!")
else:
    print("Jest zimno!")
print(f"Temperatura wynosi {temperatura} stopni")