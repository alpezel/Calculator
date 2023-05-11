# Ask user to choose one of the 4 math operations(+)(-)(x)(÷)
# Ask user to input 2 numbers
# use exeption if the input is not number; display error message and try again
# Display result
# Ask if the user wants to try again or not (yes or no) 
# use exeption if the input is not yes or no; display error message and try again
#if yes repeat program; if no display "Thank you!" 
boarder = "\n\033[0;39m==================================================="
def display_menu():
    print ("\n\033[0;39m===================================================")
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
            choice = int(input("\n\033[0;33mWhat Math Operation will you choose? (1-4): \033[0;39m"))
            if choice < 5 and choice >= 1:
                break
        except ValueError:
            print("\n\033[0;31m[The input is not a number!]")
        else:  
            print("\n\033[0;31m[The input is not from 1-4]")

    while True:
        try:
            n1, n2 = map(float,input("\n\033[0;33mEnter two integer number(put space in between): \033[0;39m").split())
        except ValueError:
            print("\n\033[0;31m[The input is not a number or not enough values inputted!]")
        else:
            break    

    if choice == 1:
        sum = Add()
        print("\n\033[0;36mResult:",sum)
        print(boarder)
    elif choice==2:
        diff=Subtract()
        print ("\nResult:",diff)
        print(boarder)
    elif choice==3:
        prod=Multiply()
        print ("\nResult:",prod)
        print(boarder)
    elif choice ==4:
        quot=Divide()
        print ("\nResult:",quot)
        print(boarder)

    tryagain= input("\n\033[0;32mDo you want to try again? (yes or no): \033[0;39m")
    while tryagain.lower() != "yes" and tryagain.lower() != "no":
        print ("\n\033[0;31m[The input is not (yes or no)]")
        tryagain= input("\n\033[0;32mDo you want to try again? (yes or no): \033[0;39m")
    if tryagain.lower() == "no":
        print(boarder,"\n")
        print ("\033[0;34mThank you!")
        print(boarder,"\n")
        break
