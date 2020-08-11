romans = {
    1 : "I", 2: "II", 3: "III", 4: "IV", 5: "V",
    6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",

}

x = 10
number = ""

if x >= 10:
    r = x / 10
    number = romans[10] * int(r)

print(number)
