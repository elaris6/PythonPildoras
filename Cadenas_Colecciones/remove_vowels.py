#Pyhon pgrogram to remove vowels from a given string

def removeVowels(workString):
    vowels = ('a','e','i','o','u')
    for c in workString:
        if c.lower() in vowels:
            workString = workString.replace(c,'*')
    return workString

while True:
    print ('Enter the desired string to operate (press X to exit): ')
    userString=input ()

    if userString == 'x' or userString == 'X':
        break
    else:
        workString = removeVowels(userString)
        print('Replacemente completed.')
        print('Input string: '+userString)
        print('Output string: '+workString)
