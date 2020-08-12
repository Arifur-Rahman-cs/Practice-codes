constants = {
        1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
        6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
        40: "XL", 50: "L", 100: "C", 500: "D", 1000: "M"
    }


class convert():

    def int_to_roman(self):

        x = self
        number = ""


        if x >= 10 and x <= 39:
            r = x / 10
            number = constants[10] * int(r)
            if 0 < x % 10 < 10:
                number += constants[x % 10]


        elif x == 40:
            number = constants[x]

        elif x >= 40 and 0 < x % 40 <= 10 and x < 50:
            number += constants[40] + constants[x % 10]


        elif x == 50:
            number = constants[x]

        elif x >= 50 and 0 < x % 50 <= 10 and x < 60:

            number += constants[50] + constants[x % 10]

        elif x == 60:
            number = "LX"

        else:
            number = constants[x]
            
        return number
