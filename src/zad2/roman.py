class Roman:
    def roman(number):
        roman = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        arabic = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        result = []
        for i in range(len(arabic)):
            count = int(number / arabic[i])
            result.append(roman[i] * count)
            number -= arabic[i] * count
        return ''.join(result)