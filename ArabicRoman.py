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
    if unit == '3':
        print ('Test:')
        lst=[]
        lst.append('MDCCXXXII => {}'.format(to_arabic('MDCCXXXII')))
        lst.append('MCMXI => {}'.format(to_arabic('MCMXI')))
        lst.append('MDCCL => {}'.format(to_arabic('MDCCL')))
        lst.append('MDLXXXVIIII => {}'.format(to_arabic('MDLXXXVIIII')))
        lst.append('MDXCIII => {}'.format(to_arabic('MDXCIII')))
        lst.append('499 => {}'.format(to_roman(499)))
        lst.append('1866 => {}'.format(to_roman(1866)))
        lst.append('2095 => {}'.format(to_roman(2095)))
        lst.append('54 => {}'.format(to_roman(54)))
        lst.append('5170 => {}'.format(to_roman(5170)))
        return lst
        
print ('Type 1 if you want to convert to arabic. Type 2 if you want to convert to roman. Type 3 to see the test numbers')
result=get_multiplier(str(input()))
print(result)
