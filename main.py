import secrets

pw = ""
letter = "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
lengh = int(input("Please enter password lengh: "))

for _ in range(lengh):
    pw = pw+secrets.choice(letter)
print(pw)
