import sys

def registration() :
    print("registration")

def Enrollment() :
    print("Enrollment")

def exit():
    print("bye bye")
    sys.exit()

def showMenu():
    while True:
        print("\n" + "#" * 20)
        print("Main Menu")
        print("1 -> Registration")
        print("2 -> Enrollment ")
        print("9 -> Exit")
        choice = input("Your Choice -> ")
        if choice == '1':
            registration()
        elif choice == '2':
            Enrollment()
        elif choice == '9':
            exit()
        else:
            print("Invalid Choice please try again")

showMenu()