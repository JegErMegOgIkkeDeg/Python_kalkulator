heltall_1 = int(input("Skriv inn det første heltallet: "))
heltall_2 = int(input("Skriv inn det andre heltallet: "))
sammensetting = input("Skriv inn hvordan du vil sette tallene sammen (+, -, *, /, **): ")

if sammensetting == "+":
    print(heltall_1, "+", heltall_2, "=", heltall_1 + heltall_2)
elif sammensetting == "-":
    print(heltall_1, "-", heltall_2, "=", heltall_1 - heltall_2)
elif sammensetting == "*":
    print(heltall_1, "*", heltall_2, "=", heltall_1 * heltall_2)
elif sammensetting == "/":
    print(heltall_1, "/", heltall_2, "=", heltall_1 / heltall_2)
elif sammensetting == "**":
    print(heltall_1, "**", heltall_2, "=", heltall_1 ** heltall_2)
else:
    print("Ugyldig operasjon.")