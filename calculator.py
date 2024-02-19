
w = True

def getInput():
    test = True
    while test: 
       number = input("Enter number : ")
       if not number.isnumeric():
            print("Please enter a valid number:")
       else:
            test = False
    return float(number)


while w: 
    
    x = getInput()
        
    y = getInput()
            
    result = x + y

    print("Your answer is: ", end=" ")
    print(result)
    
    wTest = input("\nTo exit enter q or any key to continue: ")
    
    if wTest == 'q':
        w = False