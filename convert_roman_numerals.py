# convert_roman_numerals.py
# Description:
# Converts between integers and roman numerals.
# At any time we expect the value to be between 1 and 3999 inclusive

NumberDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
SymbolDict = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}

class RomanNumerals:
    
    # to_roman(val): converts an integer 'val' to roman numerals, output as a string
    @staticmethod
    def to_roman(val):
        str = ''
        while val != 0:
            n = max(m for m in SymbolDict.keys() if m <= val)
            str += SymbolDict[n]
            val -= n
        return str

    # from_roman(roman_num): converts a roman numeral 'roman_num' (type str) to integer value.
    @staticmethod
    def from_roman(roman_num):
        #read from left to right
        return sum([-NumberDict[roman_num[x]] if NumberDict[roman_num[x]] < NumberDict[roman_num[x+1]] else NumberDict[roman_num[x]] for x in range(len(roman_num)-1)] + [NumberDict[roman_num[-1]]])

def main():
    rn = RomanNumerals()
    print(rn.to_roman(49))
    print(rn.from_roman('XLIX'))

if __name__ == '__main__':
    main()