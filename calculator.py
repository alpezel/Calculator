# Ask user to choose one of the 4 math operations(+)(-)(x)(÷)
# Ask user to input 2 numbers
# use exeption if the input is not number; display error message and try again
# Display result
# Ask if the user wants to try again or not (yes or no) 
# use exeption if the input is not yes or no; display error message and try again
#if yes repeat program; if no display "Thank you!" 

def display_menu():
    print ("===================================================")
    print ("                      MENU                         ")
    print ("===================================================")
    print ("\n     1.Add (+)")
    print ("     2.Subtract (-)")
    print ("     3.Multiply (x)")
    print ("     4.Divide (÷)")
    print ("\n===================================================")

def Add():
    result = n1 + n2
    return result
def Subtract():
    result = n1 - n2
    return result
def Multiply():
    result = n1 * n2
    return result
def Divide():
    result = n1 / n2
    return result



while True:
    display_menu()
    while True:
        try:
            choice = int(input("What Math Operation will you choose? (1-4):"))
        except ValueError:
            print("\n[The input is not a number!]\n")
        else:
            if 1 <= choice < 5:
                break
            else:
                print("\n[The input is not from 1-4]\n")
                try:
                    choice = int(input("What Math Operation will you choose? (1-4):"))
                except ValueError:
                    print("\n[The input is not a number!]\n")
                    
    while True:
        try:
            n1, n2 = map(float,input("\nEnter two integer number(put space in between):").split())
        except ValueError:
            print("\n[The input is not a number or not enough values inputted!]\n")
        else:
            break    
    if choice == 1:
        sum = Add()
        print("\nResult:",sum)
    elif choice==2:
        diff=Subtract()
        print ("\nResult:",diff)
    elif choice==3:
        prod=Multiply()
        print ("\nResult:",prod)
    elif choice ==4:
        quot=Divide()
        print ("\nResult:",quot)

        


    
    
         
       