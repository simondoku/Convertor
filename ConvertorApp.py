def main():
    intro = int(input('Welcome to MyConverter\n' 'Do you want to convert [1]Temperature [2]Currency [3]length [4]Weight 0.Quit '))
    if intro == 1:
        return Temperature()
    elif intro == 2:
        return Currency()
    elif intro == 3:
        return Length()
    elif intro == 4:
        return Weight()
    elif intro == 0:
        print('Goodbye')
    else:
        print('Choose the right option')
        main()






#Functions
def Temperature():
    temp = int(input('1. Celsius to Fahrenheit 2. Fahrenheit to Celsius 3. Return to main menu 0. Quit'))
    if temp == 1:
        celsius = int(input('Enter your temperature in Celsius'))
        converted = (celsius*9/5) + 32
        print(f'Your {celsius} Celsius temperature is {converted} in Fahrenheit')
        Temperature()
    elif temp == 2:
        fahrenheit = int(input('Enter your temperature in Fahrenheit'))
        converted2 = (fahrenheit-32)*5/9
        print(f'Your {fahrenheit} Fahrenheit temperature is {converted2} in Celsius')
        Temperature()
    elif temp == 3:
        main()
    elif temp == 0:
         print('Thank you for Using MyConvertor')
    else:
        print('Enter the right option')
        Temperature()

def Currency():
    currency = int(input('1.USD to Ghana Cedis 2. Ghana Cedis to USD 3.USD to Nigerian Naira 4. Nigerian Naira to USD 5. 0.Quit'))
    if currency == 1:
        usd = int(input('Enter the amount in USD:'))
        toCedis = usd*6
        print(f'Your $ {usd} is equivalent to {toCedis} cedis ')
        Currency()
    elif currency == 2:
        ghanaCedis = int(input('Enter the amount in Ghana Cedis:'))
        toUSD = ghanaCedis/6
        print(f'Your  {ghanaCedis} cedis is equivalent to $ {toUSD}')
        Currency()
    elif currency == 3:
        usd2 = int(input('Enter the amount in USD:'))
        toNaira = usd2 * 411
        print(f'Your $ {usd2} is equivalent to {toNaira} Naira ')
        Currency()
    elif currency == 4:
        naira = int(input('Enter the amount in Nigerian Naira:'))
        toUSD2 = naira / 411
        print(f'Your  {naira} naira is equivalent to $ {toUSD2}')
        Currency()
    elif currency == 5:
        main()
    elif currency == 0:
        print('Thank you for Using MyConvertor')
    else:
        print('Enter the right option')
        Currency()

def Length():
   length = int(input('1.cm to inches 2. inches to cm 3.feet to meters 4. meters to feet 5. return to main menu 0. Quit'))
   if length == 1:
       cm =int(input('Enter length in cm:'))
       toinches = cm/2.54
       print(f'{cm} cm = {toinches} inches')
       Length()
   elif length == 2:
       inches = float(input('Enter length in inches:'))
       tocm = inches*2.54
       print(f'{inches} inches = {tocm}cm')
       Length()
   elif length == 3:
       feet = float(input('Enter length in feet:'))
       tometers = feet / 3.281
       print(f'{feet} feet = {tometers}meters')
       Length()
   elif length == 4:
       meters = float(input('Enter length in meters:'))
       tofeet = meters * 3.281
       print(f'{meters}meters = {tofeet}feet')
       Length()
   elif length == 5:
       main()

   elif length == 0:
       print('Thank you for Using MyConvertor')

   else:
       print('Enter the right option')
       Length()

def Weight():
    weight =int(input('1.Pounds to kilogram 2. Kilogram to Pounds 3. Pounds to Grams 4. Grams to Pounds 5. return to main menu 0. Quit'))
    if weight == 1:
        pounds = float(input('Enter weight in pounds:'))
        toKilo = pounds/2.205
        print(f'{pounds}pounds = {toKilo}kg')
        Weight()
    elif weight == 2:
        kilo = float(input('Enter weight in Kilo:'))
        toPounds = kilo*2.205
        print(f'{kilo}kg = {toPounds}pounds')
        Weight()
    elif weight == 3:
        pounds2 = float(input('Enter weight in pounds:'))
        toGram = pounds2*454
        print(f'{pounds}pounds = {toGram}kg')
        Weight()
    elif weight == 4:
        grams = float(input('Enter weight in grams:'))
        toPounds2 = grams/454
        print(f'{grams}grams = {toPounds2}pounds')
        Weight()
    elif weight == 5:
        main()
    elif weight == 0:
        print('Thank you for Using MyConvertor')
    else:
        print('Enter the right option')
        Weight()


#Running Code
main()