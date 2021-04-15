import secrets

pw = ""
syntax = ""
zeichen = ""

zeichenBuchstaben = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
zeichenZahlen = "0123456789"
zeichenSymbole = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


def program():
    global pw
    syntax = int(input("Bitte Inhalt des Passwort festlegen.\n"
                       "Für Buchstaben = '1'\n"
                       "Für Zahlen     = '2'\n"
                       "Für Symbole    = '3'\n"
                       "Hier Eintragen:"))

    if syntax   == 1:
        zeichen = zeichenBuchstaben

    elif syntax == 2:
        zeichen = zeichenZahlen

    elif syntax == 3:
        zeichen = zeichenSymbole

    elif syntax == 12:
        zeichen = zeichenBuchstaben + zeichenZahlen

    elif syntax == 21:
        zeichen = zeichenBuchstaben + zeichenZahlen

    elif syntax == 13:
        zeichen = zeichenBuchstaben

    elif syntax == 31:
        zeichen = zeichenBuchstaben + zeichenSymbole

    elif syntax == 23:
        zeichen = zeichenZahlen + zeichenSymbole

    elif syntax == 32:
        zeichen = zeichenZahlen + zeichenSymbole

    laenge = int(input("Bitte Passwortlänge eingeben: "))
    for _ in range(laenge):
        pw = pw + secrets.choice(zeichen)

program()

print("Dein generiertes Passwort lautet: " +pw)
print("Beliebige Taste drücken, um das Fenster zu schließen.")
input()
