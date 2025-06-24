class Solution:
    def intToRoman(self, num: int) -> str:

        
        roman={1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}        #first, create a dictionary for all the basic roman numerals

        number=str(num)     #convert num from integer(num) to string(number)
        power=10**(len(number)-1)       #the length of the number -1 will be the power of the digit ex.(number=1234, first digit 1 = 1*10**power(4-1=3f) = 1000)
        result=''       #to add the converted result one by one

        for digit in number:        #walk through each digit in string(number)
            digit=int(digit)        #convert string(digit) into integer(digit). digit represent the sigle value of each digit we walk through ex.(number=1234, first digit = 1)
            i=digit*power       #create a variable i, i=the actual value of the digit's position, ex.(number = 1234, first i = digit(1) * power(10**3) = 1000)
            comp=digit-5        #create a variable comp(complement), to determine if the digit is greater than 5, for the later calculation


            if i in roman:      #first condition: result add the roman numerals directly if the first i is in dictionary ex.(i = 1000, roman[1000] == 'M', result += M)
                print('1')      #trace for debugging
                result+=roman[i]        #result add the matching roman numeral

            elif digit>0 and i+power in roman:      #second condition: if the digit is greater than 0 ( 0+1=1, result will add additional value, we want to avoid adding that) only 1 + power diffrence in dictionary ex.(4+1 = 5('V'), 90 + 10 = 100('D'))
                print('2')      #trace for debugging
                result+=roman[power]        #result first add the 1**power
                result+=roman[i+power]      #than add the complete number ex.(4 = 'I', 'V' = IV)
                
            
            elif digit>5:       #third condition: if the digit is greater than 5
                print('3')      #trace for debugging
                print(f'i:{i}-(5*power){5*power}')      #trace for debugging
                print(f'comp={comp}')       #trace for debugging
                result+=roman[5*power]      #result first add the base number (5)
                result+=(roman[1*power]*comp)       #than result add the extra number depends on the complement we created in the begining ex.(8 = 5, 1, 1, 1 = 'V', 'I', 'I', 'I', = VIII)
            
            elif digit<4:       #last condition: digit is lower than 4
                print('4')      #trace for debugging
                result+=roman[power]*digit      #result directly add the single roman numeral ex.('I', 'X' times the number 30 = 'X'*3 = 'XXX'. if digit = 0 than 'I'*0 = '')

            print(f'i={i}, digit={digit}, result={result}')     #trace for debugging
            power//=10      #lastly, devide the power by 10, so we can calculate the next number correctly
            

        return result       #return the result at the end of loop
        

            
