import secrets

pw = ""
zeichen = "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
laenge = int(input("Bitte Passwortlänge eingeben: "))

for _ in range(laenge):
    pw = pw+secrets.choice(zeichen)
print(pw)