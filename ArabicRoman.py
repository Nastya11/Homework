def to_roman(n): #перевод в римские
    roman = ''
    for arabic, keys in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        roman += n // arabic * keys
        n %= arabic
    return roman


def to_arabic(roman): #перевод в арабские
    number = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    arabic = 0
    for i in range(len(roman)):
        try:
            if number[roman[i]]<number[roman[i+1]]:
                arabic-=number[roman[i]]
            else:
                arabic+=number[roman[i]]
        except IndexError:
            arabic+=number[roman[i]]
    return arabic
   
    
def get_multiplier(unit): #попытка заменить switch/case, которого нет в питоне
    if unit == '1':
        print ('enter roman number:')
        a=to_arabic(str(input()))
        return a
    if unit == '2':
        print ('enter arabic number:')
        r=to_roman(int(input()))
        return r
   
        
print ('Type 1 if you want to convert to arabic. Type 2 if you want to convert to roman')
result=get_multiplier(str(input()))
print(result)
